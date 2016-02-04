# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *
import pickle
# from bson.objectid import ObjectId

# db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']


def arr_2_dict(arr, key1, key2):
    d = dict()
    for a in arr:
        d[a[key1]] = a[key2]
    return d


def topic_scene(start, end, topicId, platform):
    res = {"startMaster": 0, "completeMaster": 0, "startMasterNow": 0, "startMasterLater": 0, "completeCountNow": 0, "completeCountLater": 0}
    users1 = list(events.find({
        "eventKey": "completeLearning",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1}))
    users2 = list(events.find({
        "eventKey": "startMaster",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1}))
    users3 = list(events.find({
        "eventKey": "completeMaster",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
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

    if res['startMaster'] == 0:
        return res
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

    pipeline = [
        {
            "$match": {
                "user": {"$in": userIds},
                "platform2": platform,
                "eventTime": {"$gte": start, "$lt": end}
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
                "points": {"$push": '$_id'},
                "keys": {"$push": "$eventKey"}
            }
        }
    ]

    users_points = list(events.aggregate(pipeline, allowDiskUse=True))

    for p in users_points:
        inds1 = [p['points'].index(i) for i in u1[p['_id']]]
        inds2 = [p['points'].index(i) for i in u2[p['_id']]]
        inds3 = [p['points'].index(i) for i in u3[p['_id']]] if p['_id'] in u3 else []
        i = get_ind(inds1, inds2)
        if i > -1:
            # print(i)
            j = inds2.index(i+1) if (i+1) in inds2 else -1
            if j > -1:
                res['startMasterNow'] += 1
                i1 = inds2[j]
                i2 = inds2[j+1] if j+1 < len(inds2) else 1000000
                if any([i1 < k < i2 for k in inds3]):
                    res['completeCountNow'] += 1
            else:
                res['startMasterLater'] += 1
                # print(inds2)
                inds22 = [ii for ii in inds2 if ii > i]
                i1 = inds22[0] if 0 < len(inds22) else 1000000
                i2 = inds22[1] if 1 < len(inds22) else 1000000
                if any([i1 < k < i2 for k in inds3]):
                    res['completeCountLater'] += 1
    # res['startMasterLater'] = res['startMaster'] - res['startMasterNow']
    # res['laterCompleteCount'] = res['completeMaster'] - res['immediatelyCompleteCount']
    return res


def get_ind(inds1, inds2):
    i = inds1[0]
    inds22 = [ii for ii in inds2 if ii > i]
    if len(inds22) > 0:
        j = inds22[0]
        inds11 = [ii for ii in inds1 if ii < j]
        k = inds11[-1]
    else:
        k = -1
    return k

# top 10 topics list

# weeklyEnterTopicsTopTenList = [
#     u'54c708798bac81fccbd4bae5',
#     u'56629d6057da889d40916287',
#     u'54c708798bac81fccbd4bb53',
#     u'564ed38c2e05ec030b0ad3c3',
#     u'54c708798bac81fccbd4bb3c',
#     u'563050396c21a8f0350a1ea3',
#     u'5620af46b032f8db1619ee28',
#     u'54c708798bac81fccbd4bae8',
#     u'56399cccbdbf426a5d58ed5e',
#     u'564ee8151edb0de474025bd0']
# print(weeklyEnterTopicsTopTenList)


def print_topic_scene(topics, start, end):
    start_timestamp = calendar.timegm(start.utctimetuple()) * 1000
    end_timestamp = calendar.timegm(end.utctimetuple()) * 1000
    s = time.time()
    # platforms = ['PC', 'android', 'iOS']
    platforms = ['PC']
    f = open('../data/周前十知识点模块情景设定'+str((start + datetime.timedelta(days=1)).date())+'-'+str(end.date())+'.txt', 'w')
    print('---------- 周前十知识点模块情景设定', (start + datetime.timedelta(days=1)).date(), '-', end.date(), '----------', file=f)
    for topic in topics:
        print('知识点 ', topic['_id'], topic['name'].encode('UTF-8'), file=f)
        for p in platforms:
            print('----------', p, '----------', file=f)
            res = topic_scene(start_timestamp, end_timestamp, topic['_id'], p)
            if res['startMaster'] == 0:
                print('没有专题模块', file=f)
            else:
                print('完成视频,且进入练习人数 ', res['startMaster'], res['startMasterNow']+res['startMasterLater'],file=f)
                print('完成视频, 且完成练习人数 ', res['completeMaster'], res['completeCountNow']+res['completeCountLater'],file=f)
                print('完成视频用户中, 完成学习立即进入练习模块用户数 ', res['startMasterNow'], file=f)
                print('完成视频用户中, 按照预习,课后模式进入练习用户数 ', res['startMasterLater'], file=f)
                print('完成学习立即进入练习用户中完成练习人数 ', res['completeCountNow'], file=f)
                print('完成按照预习,课后模式完成用户中完成练习人数 ', res['completeCountLater'], file=f)
                print('完成学习立即进入练习用户完成练习比 ', res['completeCountNow'] * 1.0 / res['startMasterNow'] if res['startMasterNow'] != 0 else 0, file=f)
                print('完成按照预习,课后模式完成用户完成练习比 ', res['completeCountLater'] * 1.0 / res['startMasterLater'] if res['startMasterLater'] != 0 else 0, file=f)
                print('----------------------------------------', file=f)
            print(topic['_id'], topic['name'], p, 'done')

    # for p in platforms:
    #     print('----------', p, '----------', file=f)
    #     for topic in topics:
    #         # print('知识点名称 ', topic['name'])
    #         print('知识点 ', topic['_id'], topic['name'].encode('UTF-8'), file=f)
    #         res = topic_scene(start_timestamp, end_timestamp, topic['_id'], p)
    #         print('完成视频,且进入练习人数 ', res['startMaster'], file=f)
    #         print('完成视频, 且完成练习人数 ', res['completeMaster'], file=f)
    #         print('完成视频用户中, 完成学习立即进入练习模块用户数 ', res['startMasterNow'], file=f)
    #         print('完成视频用户中, 按照预习,课后模式进入练习用户数 ', res['startMasterLater'], file=f)
    #         print('完成学习立即进入练习用户中完成练习人数 ', res['immediatelyCompleteCount'], file=f)
    #         print('完成按照预习,课后模式完成用户中完成练习人数 ', res['laterCompleteCount'], file=f)
    #         print('完成学习立即进入练习用户完成练习比 ', res['immediatelyCompleteCount'] * 1.0 / res['startMasterNow'] if res['startMasterNow'] != 0 else 0, file=f)
    #         print('完成按照预习,课后模式完成用户完成练习比 ', res['laterCompleteCount'] * 1.0 / res['startMasterLater'] if res['startMasterLater'] != 0 else 0, file=f)
    #         print('----------------------------------------', file=f)
    #         print('知识点', topic['name'], p, 'done')

    f.close()
    e = time.time()
    print('新用户周前十知识点情景设定 运行用时: ',(e-s)/60, 'min')


# print_topic_scene([{"_id": "564ed38c2e05ec030b0ad3c3", 'name': 'topic'}], datetime.datetime(2016, 1, 9, 16), datetime.datetime(2016, 1, 16, 16))
