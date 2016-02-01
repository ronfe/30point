# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *

platforms = ['pc', 'android', 'ios']

events = [
    {"name": "进入一个学习模块", "key": "startLearning"},
    {"name": "进入一个练习模块", "key": "startMaster"},
    {"name": "完成一个学习模块", "key": "completeLearning"},
    {"name": "完成一个练习模块", "key": "completeMaster"}
]


def event_occurrence_gt_2(event_flow, event_key):
    uv = 0
    for flow in event_flow:
        if flow.count(event_key) >= 2:
            uv += 1
    return uv


def week_target(userIds, star, end):
    query = {
        "_id": {"$in": userIds},
        "weekTarget": {"$ne": {}},
        "weekTarget.deadline": {"$gt": end},
        "weekTarget.stars": star,
    }
    query2 = {
        "_id": {"$in": userIds},
        "weekTarget": {"$ne": {}},
        "weekTarget.deadline": {"$gt": end},
        "weekTarget.stars": star,
        "weekTarget.finished": True
    }
    return {'set': users.count(query), 'finished': users.count(query2)}


def next_week(start, end):
    ss = time.time()
    last_week_start = start - datetime.timedelta(days=7)
    last_week_end = start
    f = open('../data/新用户次周行为'+str((start+datetime.timedelta(days=1)).date())+'-'+str(end.date())+".txt", 'w')
    print('---------- 新用户次周行为', (start+datetime.timedelta(days=1)).date(), '-', end.date(), '----------', file=f)
    for p in platforms:
        print('----------', p, '-----------', file=f)
        users_dict = calc_user_device(last_week_start, last_week_end, [p])
        event_flow = collect_event(start, end, users_dict, [p])
        num_new_user = len(users_dict['hasUsers']) + (0 if p is 'pc' else len(users_dict['notUsers']))
        userIds = users_dict['hasUsers'].keys()
        print('上周新用户 ', num_new_user, file=f)

        pv_uv = pv_uv_count(event_flow, 'startLearning')
        print('进入一个学习模块 ', ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)

        pv_uv = pv_uv_count(event_flow, 'startMaster')
        print('进入一个练习模块 ', ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)

        print('进入学习模块数大于2 ', ' uv: ', event_occurrence_gt_2(event_flow, 'startLearning'), file=f)
        print('进入练习模块数大于2 ', ' uv: ', event_occurrence_gt_2(event_flow, 'startMaster'), file=f)

        pv_uv = pv_uv_count(event_flow, 'completeLearning')
        print('完成一个学习模块 ', ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)

        pv_uv = pv_uv_count(event_flow, 'completeMaster')
        print('完成一个练习模块 ', ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)

        print('完成两个及以上学习模块 ', ' uv: ', event_occurrence_gt_2(event_flow, 'completeLearning'), file=f)
        print('完成两个及以上练习模块 ', ' uv: ', event_occurrence_gt_2(event_flow, 'completeMaster'), file=f)

        standard = week_target(userIds, 6, end)
        challenge = week_target(userIds, 9, end)
        print('设定标准模式每周目标 ', standard['set'], file=f)
        print('标准目标完成率 ', standard['finished'] * 1.0 / standard['set'] if standard['set'] != 0 else 0, file=f)

        print('设定挑战模式每周目标 ', challenge['set'], file=f)
        print('挑战目标完成率 ', challenge['finished'] * 1.0 / challenge['set'] if challenge['set'] != 0 else 0, file=f)

    f.close()
    ee = time.time()
    print("next week time: ", (ee-ss)/60, 'min')


