# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *
import time


s = time.time()
platforms = ['pc', 'android', 'ios']

START_DATE = datetime.datetime(2015, 12, 27, 0)
END_DATE = datetime.datetime(2016, 1, 3, 0)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)

LAST_WEEK_START_UTC = START_DATE_UTC - datetime.timedelta(days=7)
LAST_WEEK_END_UTC = START_DATE_UTC

days = (END_DATE - START_DATE).days

events_pc = [
    {"name": "进入一个学习模块完成页", "key": "completeLearning"},
    {"name": "进入一个练习模块完成页", "key": "completeMaster"},
    {"name": "完成一个知识点", "key": "challengeSuccess"},
    # {"name": "进入两个及以上学习模块完成页", "key": ""},
    # {"name": "进入两个及以上练习模块完成页", "key": ""},
    # {"name": "进入两个及以上知识点完成页", "key": ""},
    # {"name": "设置6星目标", "key": ""},
    # {"name": "设置9星目标", "key": ""},
    # {"name": "未进入任何视频完成页人中 打开视频数目大于2的用户数", "key": ""},
    # {"name": "未进入任何视频完成页人中 打开视频数目大于2且观看时间小于3分钟的人数", "key": ""}
]

events_mobile = [
    {"name": "完成一个视频", "key": "finishVideo"},
    {"name": "完成一个练习", "key": "problemSetSuccess"},
    # {"name": "完成两个及以上视频", "key": ""},
    # {"name": "完成两个及以上练习", "key": ""},
    # {"name": "未进入任何视频完成页人中 打开视频数目大于2的用户数", "key": ""},
    # {"name": "未进入任何视频完成页人中 打开视频数目大于2且观看时间小于3分钟的人数", "key": ""},
    # {"name": "本周内进入章节页人数", "key": "startChapter"},
    # {"name": "已注册人数", "key": ""},
    # {"name": "新用户中已注册人数比", "key": ""},
    # {"name": "次周用户中已注册人数", "key": ""}
]


def new_register(event_flow):
    next_week_new_user = 0
    for flow in event_flow:
        if 'registSuccess' in flow:
            next_week_new_user += 1
    return next_week_new_user


def uv_1(event_flow, event_key):
    uv = 0
    for flow in event_flow:
        if flow.count(event_key) >= 2:
            uv += 1
    return uv


def uv_2(event_flow, event_key1, event_key2):
    uv = 0
    for flow in event_flow:
        if flow.count(event_key1) < 1 and flow.count(event_key2) > 2:
            uv += 1
    return uv


filename = '../data/新用户次周行为'+str(START_DATE.date()) + '--' + str((END_DATE - datetime.timedelta(days=1)).date()) + ".txt"
f = open(filename, 'w')

last_week_start = START_DATE_UTC - datetime.timedelta(days=7)
last_week_end = START_DATE_UTC


print("---------- 新用户次周行为", START_DATE.date(), '-', (END_DATE - datetime.timedelta(days=1)).date(), " ----------", file=f)


print("---------- pc ----------", file=f)
users_dict = calc_user_device(last_week_start, last_week_end, ['pc'])
event_flow = collect_event(START_DATE_UTC, END_DATE_UTC, users_dict, ['pc'])
print('上周新用户数: ', len(users_dict['hasUsers']), file=f)
for event in events_pc:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], 'uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)
uv = uv_1(event_flow, 'completeLearning')
print("进入两个及以上学习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'completeMaster')
print("进入两个及以上练习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'challengeSuccess')
print("进入两个及以上知识点完成页 ", 'uv: ', uv, file=f)
uv = uv_2(event_flow, 'finishVideo', 'startVideo')
print("未进入任何视频完成页人中 打开视频数目大于2的用户数 ", 'uv: ', uv, file=f)

print("------------ android ------------", file=f)
users_dict = calc_user_device(last_week_start, last_week_end, ['android'])
event_flow = collect_event(START_DATE_UTC, END_DATE_UTC, users_dict, ['android'])
print('上周新用户数: ', len(users_dict['hasUsers'])+len(users_dict['notUsers']), file=f)
for event in events_mobile:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], 'uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)
uv = uv_1(event_flow, 'completeLearning')
print("进入两个及以上学习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'completeMaster')
print("进入两个及以上练习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'challengeSuccess')
print("进入两个及以上知识点完成页 ", 'uv: ', uv, file=f)
uv = uv_2(event_flow, 'finishVideo', 'startVideo')
print("未进入任何视频完成页人中 打开视频数目大于2的用户数 ", 'uv: ', uv, file=f)
# print("已注册人数 ")
print("上周注册人数", len(users_dict['hasUsers']), file=f)
print("这周注册人数", new_register(event_flow), file=f)


print("-------------- iOS ---------------", file=f)
users_dict = calc_user_device(last_week_start, last_week_end, ['ios'])
event_flow = collect_event(START_DATE_UTC, END_DATE_UTC, users_dict, ['ios'])
print('上周新用户数: ', len(users_dict['hasUsers'])+len(users_dict['notUsers']), file=f)
for event in events_mobile:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], 'uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)
uv = uv_1(event_flow, 'completeLearning')
print("进入两个及以上学习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'completeMaster')
print("进入两个及以上练习模块完成页 ", 'uv: ', uv, file=f)
uv = uv_1(event_flow, 'challengeSuccess')
print("进入两个及以上知识点完成页 ", 'uv: ', uv, file=f)
uv = uv_2(event_flow, 'finishVideo', 'startVideo')
print("未进入任何视频完成页人中 打开视频数目大于2的用户数 ", 'uv: ', uv, file=f)
print("上周注册人数", len(users_dict['hasUsers']), file=f)
print("这周注册人数", new_register(event_flow), file=f)

f.close()

e = time.time()
print("Total time: ", int((e-s)), ' s')
