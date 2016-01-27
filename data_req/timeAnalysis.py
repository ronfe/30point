# _*_ coding:utf-8 _*_
from __future__ import print_function
# import pickle
# from bson.objectid import ObjectId
from dataFunctions import *


def topic_time(start, end, topicId, platform):
    # res = {'completeLearning': 0, 'completeMaster': 0, 'time_learning': [], 'time_master': 0}
    res = dict()
    users1 = list(events.find({
        "eventKey": "startLearning",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1, 'eventTime': 1, '_id': 0}).sort('eventTime', 1)
                  )
    users2 = list(events.find({
        "eventKey": "completeLearning",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1, 'eventTime': 1, '_id': 0}).sort('eventTime', 1))

    users3 = list(events.find({
        "eventKey": "startMaster",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1, 'eventTime': 1, '_id': 0}).sort('eventTime', 1))

    users4 = list(events.find({
        "eventKey": "completeMaster",
        "user": {"$exists": True},
        "platform2": platform,
        "eventValue.topicId": topicId,
        "eventTime": {"$gte": start, "$lt": end}
    }, {'user': 1, 'eventTime': 1, '_id': 0}).sort('eventTime', 1))

    print(len(users1), len(users2), len(users3), len(users4))
    userIds1 = [u['user'] for u in users1]
    userIds2 = [u['user'] for u in users2]
    userIds3 = [u['user'] for u in users3]
    userIds4 = [u['user'] for u in users4]
    #
    # # get user ids that both have completeLearning and startMaster points
    user_ids_learning = list(set(userIds1).intersection(set(userIds2)))
    user_ids_master = list(set(userIds3).intersection(set(userIds4)))

    res['completeLearning'] = len(user_ids_learning)
    res['completeMaster'] = len(user_ids_master)
    print('complete learning:', res['completeLearning'])
    print('complete master: ', res['completeMaster'])

    users1 = [u for u in users1 if u['user'] in user_ids_learning]
    users2 = [u for u in users2 if u['user'] in user_ids_learning]
    users3 = [u for u in users3 if u['user'] in user_ids_master]
    users4 = [u for u in users4 if u['user'] in user_ids_master]

    print(len(users1), len(users2), len(users3), len(users4))

    u1 = {}
    u2 = {}
    u3 = {}
    u4 = {}

    for u in users1:
        if u['user'] in u1:
            u1[u['user']].append(u['eventTime'])
        else:
            u1[u['user']] = [u['eventTime']]
    for u in users2:
        if u['user'] in u2:
            u2[u['user']].append(u['eventTime'])
        else:
            u2[u['user']] = [u['eventTime']]
    for u in users3:
        if u['user'] in u3:
            u3[u['user']].append(u['eventTime'])
        else:
            u3[u['user']] = [u['eventTime']]
    for u in users4:
        if u['user'] in u4:
            u4[u['user']].append(u['eventTime'])
        else:
            u4[u['user']] = [u['eventTime']]
    print(len(u1), len(u2), len(u3), len(u4))

    res['time_learning'] = []
    res['time_master'] = []

    for u in u2:
        i = 0
        j = 0
        while j < len(u2[u]) and u1[u][0] > u2[u][j]:
            j += 1
        if j == len(u2[u]):
            start = datetime.datetime.fromtimestamp(u1[u][0]/1000)
            complete = datetime.datetime.fromtimestamp(u2[u][j-1]/1000)
            print('user:', u, 'start learning:', start, 'complete learning', complete)
            continue
        while i < len(u1[u]) and u1[u][i] < u2[u][j]:
            i += 1
        interval = round((u2[u][j] - u1[u][i-1]) * 1.0 / 60000, 2)
        res['time_learning'].append(interval)

    for u in u4:
        i = 0
        j = 0
        while j < len(u4[u]) and u3[u][0] > u4[u][j]:
            j += 1
        if j == len(u4[u]):
            start = datetime.datetime.fromtimestamp(u3[u][0]/1000)
            complete = datetime.datetime.fromtimestamp(u4[u][j-1]/1000)
            print('user:', u, 'start master:', start, 'complete master', complete)
            continue
        while i < len(u3[u]) and u3[u][i] < u4[u][j]:
            i += 1
        interval = round((u4[u][j] - u3[u][i-1]) * 1.0 / 60000, 2)
        res['time_master'].append(interval)

    res['completeLearning'] = len(res['time_learning'])
    res['completeMaster'] = len(res['time_master'])

    res['learning_time_bucket'] = {}
    res['master_time_bucket'] = {}

    for i in range(0, 31, 2):
        res['learning_time_bucket'][i] = 0
        res['master_time_bucket'][i] = 0
    for t in res['time_learning']:
        b = int(math.floor(math.floor(t) / 2) * 2)
        if b < 30:
            res['learning_time_bucket'][b] += 1
        else:
            res['learning_time_bucket'][30] += 1
    for t in res['time_master']:
        b = int(math.floor(math.floor(t) / 2) * 2)
        if b < 30:
            res['master_time_bucket'][b] += 1
        else:
            res['master_time_bucket'][30] += 1

    print(len(res['time_learning']), len(res['time_master']))

    return res

# top 10 topics list
# weeklyEnterTopicsTopTenList = weeklyTopicsEnterTop10(START_DATE_UTC, END_DATE_UTC)

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

# weeklyEnterTopicsTopTenList = [u'54c708798bac81fccbd4bae5', u'54c708798bac81fccbd4bb3c', u'54c708798bac81fccbd4bae8', u'56629d6057da889d40916287', u'54c708798bac81fccbd4bb53', u'564ed38c2e05ec030b0ad3c3', u'54c708798bac81fccbd4bb40', u'563050396c21a8f0350a1ea3', u'564ee8151edb0de474025bd0', u'56399cccbdbf426a5d58ed5e']
# print(weeklyEnterTopicsTopTenList)
# f = open('../data/周前十知识点时间分析'+str(START_DATE.date())+'-'+str((END_DATE-datetime.timedelta(days=1)).date())+'.txt', 'w')


def print_time_analysis(topics, start, end):
    s = time.time()
    start_timestamp = calendar.timegm(start.utctimetuple()) * 1000
    end_timestamp = calendar.timegm(end.utctimetuple()) * 1000
    platforms = ['PC', 'android', 'iOS']
    f = open('../data/周前十知识点时间分析'+str((start + datetime.timedelta(days=1)).date())+'-'+str(end.date())+'.txt', 'w')
    print('---------- 周前十知识点时间分析', (start+datetime.timedelta(days=1)).date(), '-', end.date(), '----------', file=f)
    for p in platforms:
        print('----------', p, '----------', file=f)
        for topic in topics:
            # print('知识点名称 ', topic['name'])
            print('知识点 ', topic['_id'], topic['name'].encode('UTF-8'), file=f)
            res = topic_time(start_timestamp, end_timestamp, topic['_id'], p)
            print('学习模块完成人数 ', res['completeLearning'], file=f)
            print('练习模块完成人数', res['completeMaster'], file=f)
            print('学习模块时间分析 ', file=f)
            for k in res['learning_time_bucket']:
                if k != 30:
                    print(k, '-', k+2, '分钟: ', res['learning_time_bucket'][k], file=f)
                else:
                    print('30分钟以上: ', res['learning_time_bucket'][30], file=f)
            print('练习模块时间分析 ', file=f)
            for k in res['master_time_bucket']:
                if k != 30:
                    print(k, '-', k+2, '分钟: ', res['master_time_bucket'][k], file=f)
                else:
                    print('30分钟以上: ', res['master_time_bucket'][30], file=f)
            # print(res['time_learning'])
            # print(res['time_master'])
            # print(res['learning_time_bucket'])
            # print(res['master_time_bucket'])
            print('----------------------------------------', file=f)
            print('知识点', topic['name'], p, 'done')

    f.close()
    e = time.time()
    print('新用户周前十知识点时间分析 运行用时: ', (e-s)/60, 'min')

