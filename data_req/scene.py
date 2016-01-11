# _*_ coding:utf-8 _*_
from __future__ import print_function
from pymongo import MongoClient, DESCENDING
# import pickle
# from bson.objectid import ObjectId
import time
import datetime
import calendar
db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
events = db['events']
topics = db['topics']

START_DATE = datetime.datetime(2015, 12, 21)
END_DATE = datetime.datetime(2015, 12, 28)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)

START_TIMESTAMP = calendar.timegm(START_DATE_UTC.utctimetuple()) * 1000
END_TIMESTAMP = calendar.timegm(END_DATE_UTC.utctimetuple()) * 1000

print(START_TIMESTAMP, END_TIMESTAMP)
s = time.time()


# calculate weekly top 10 topics
def weeklyTopicsEnterTop10(startDate, endDate):
    pipeline = [
        {
            "$match": {
                "eventKey": "enterTopic",
                "serverTime": {
                    "$gte": startDate,
                    "$lt": endDate
                }
            }
        },
        {
            "$group": {
                "_id": "$eventValue.topicId",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": DESCENDING
            }
        }
    ]

    x = list(events.aggregate(pipeline))[:10]
    return [t['_id'] for t in x]


def topic_scene(topicId):
    res = {}
    users1 = list(events.find({
        "eventKey": "completeLearning",
        "user": {"$exists": True},
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}
    }, {'user': 1}))
    users2 = list(events.find({
        "eventKey": "startMaster",
        "user": {"$exists": True},
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}
    }, {'user': 1}))
    users3 = list(events.find({
        "eventKey": "completeMaster",
        "user": {"$exists": True},
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}
    }, {'user': 1}))

    print(len(users1), len(users2), len(users3))
    userIds1 = [u['user'] for u in users1]
    userIds2 = [u['user'] for u in users2]
    userIds3 = [u['user'] for u in users3]

    # get user ids that both have completeLearning and startMaster points
    userIds = list(set(userIds1).intersection(set(userIds2)))
    userIds2 = list(set(userIds).intersection(set(userIds3)))

    res['startMaster'] = len(userIds)
    res['completeMaster'] = len(userIds2)
    print('number of users:', res['startMaster'])

    users1 = [u for u in users1 if u['user'] in userIds]
    users2 = [u for u in users2 if u['user'] in userIds]
    users3 = [u for u in users3 if u['user'] in userIds2]

    print(len(users1), len(users2), len(users3))

    u1 = {}
    u2 = {}
    u3 = {}

    for u in users1:
        if u['user'] in u1:
            u1[u['user']].append(u['_id'])
        else:
            u1[u['user']] = [u['_id']]
    for u in users2:
        if u['user'] in u2:
            u2[u['user']].append(u['_id'])
        else:
            u2[u['user']] = [u['_id']]
    for u in users3:
        if u['user'] in u3:
            u3[u['user']].append(u['_id'])
        else:
            u3[u['user']] = [u['_id']]

    print(len(u1), len(u2))

    pipeline = [
        {
            "$match": {
                "user": {"$in": userIds},
                "eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}
            }
        },
        {
            "$sort": {
                "eventTime": 1
            }
        },
        {
            "$group": {
                "_id": "$user",
                "points": {"$push": '$_id'}
            }
        }
    ]

    users_points = list(events.aggregate(pipeline, allowDiskUse=True))

    print('points: ', len(users_points))
    res['startMasterImmediately'] = 0
    res['immediatelyCompleteCount'] = 0
    for p in users_points:
        inds1 = [p['points'].index(i) for i in u1[p['_id']]]
        inds2 = [p['points'].index(i) for i in u2[p['_id']]]
        inds3 = [p['points'].index(i) for i in u3[p['_id']]] if p['_id'] in u3 else []
        for i in inds1:
            j = inds2.index(i+1) if (i+1) in inds2 else -1
            if j > -1:
                res['startMasterImmediately'] += 1
                i1 = inds2[j]
                i2 = inds2[j+1] if j+1 < len(inds2) else 100000000
                if any([i1 < k < i2 for k in inds3]):
                    res['immediatelyCompleteCount'] += 1
                break
    res['startMasterLater'] = res['startMaster'] - res['startMasterImmediately']
    res['laterCompleteCount'] = res['completeMaster'] - res['immediatelyCompleteCount']
    return res

# top 10 topics list
# weeklyEnterTopicsTopTenList = weeklyTopicsEnterTop10(START_DATE_UTC, END_DATE_UTC)

weeklyEnterTopicsTopTenList = [
    u'54c708798bac81fccbd4bae5',
    u'56629d6057da889d40916287',
    u'54c708798bac81fccbd4bb53',
    u'564ed38c2e05ec030b0ad3c3',
    u'54c708798bac81fccbd4bb3c',
    u'563050396c21a8f0350a1ea3',
    u'5620af46b032f8db1619ee28',
    u'54c708798bac81fccbd4bae8',
    u'56399cccbdbf426a5d58ed5e',
    u'564ee8151edb0de474025bd0']
# print(weeklyEnterTopicsTopTenList)
f = open('../data/周前十知识点模块情景设定'+str(START_DATE.date())+'-'+str((END_DATE-datetime.timedelta(days=1)).date())+'.txt', 'w')
print('---------- 周前十知识点模块情景设定', START_DATE.date(), '-', (END_DATE-datetime.timedelta(days=1)).date(), '----------', file=f)
for topic in weeklyEnterTopicsTopTenList:
    # print('知识点名称 ', topic['name'])
    print('知识点 ', topic, file=f)
    res = topic_scene(topic)
    print('完成视频,且进入练习人数 ', res['startMaster'], file=f)
    print('完成视频, 且完成练习人数 ', res['completeMaster'], file=f)
    print('完成视频用户中, 完成学习立即进入练习模块用户数 ', res['startMasterImmediately'], file=f)
    print('完成视频用户中, 按照预习,课后模式进入练习用户数 ', res['startMasterLater'], file=f)
    print('完成学习立即进入练习用户中完成练习人数 ', res['immediatelyCompleteCount'], file=f)
    print('完成按照预习,课后模式完成用户中完成练习人数 ', res['laterCompleteCount'], file=f)
    print('完成学习立即进入练习用户完成练习比 ', res['immediatelyCompleteCount'] * 1.0 / res['startMasterImmediately'] if res['startMasterImmediately'] != 0 else 0, file=f)
    print('完成按照预习,课后模式完成用户完成练习比 ', res['laterCompleteCount'] * 1.0 / res['startMasterLater'] if res['startMasterLater'] != 0 else 0, file=f)
    print('----------------------------------------', file=f)

f.close()
e = time.time()
print(e-s)

