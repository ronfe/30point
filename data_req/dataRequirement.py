# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *
import time


s = time.time()
platforms = ['pc', 'android', 'ios']
event_keys = ['']

START_DATE = datetime.datetime(2015, 12, 19, 0)
END_DATE = datetime.datetime(2016, 1, 4, 0)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)

days = (END_DATE - START_DATE).days

events_pc = [
    {"name": "进入启动页面             ", "key": "enterHome"},
    {"name": "启动页点击免费使用        ", "key": "clickFreeForUseSS"},
    {"name": "启动页点击注册           ", "key": "clickSignupBtn"},
    {"name": "进入注册页              ", "key": "enterSignupPage"},
    {"name": "在注册页点击学生         ", "key": "chooseStudentRole"},
    {"name": "在注册页点击教师         ", "key": "chooseTeacherRole"},
    {"name": "在注册页点击注册         ", "key": "signupSuccess"},
    {"name": "完成注册点击我的学习      ", "key": "clickMyLearning"},
    {"name": "进入章节页               ", "key": "startChapter"},
    {"name": "进入知识点               ", "key": "enterTopic"},
    # {"name": "进入学习视频或练习",      "key": ""},
    # {"name": "完成第一个学习视频或专题", "key": ""},
    # {"name": "完成学习模块或练习模块",   "key": ""},
    {"name": "进入学习视频             ", "key": "startLearning"},
    {"name": "进入练习                ", "key": "startMaster"},
    {"name": "完成一个学习视频         ", "key": "finishVideo"},
    {"name": "完成一个专题            ", "key": "problemSetSuccess"},
    {"name": "完成学习模块            ", "key": "completeLearning"},
    {"name": "完成练习模块            ", "key": "completeMaster"}
]

events_mobile = [
    {"name": "进入启动页面             ", "key": "enterGuidePage"},
    {"name": "启动页点击免费使用        ", "key": "clickExperience"},
    {"name": "进入注册页               ", "key": "enterSignupPage"},
    {"name": "在注册页点击注册          ", "key": "registSuccess"},
    # {"name": "完成注册点击进入我的学习", "key": ""},
    {"name": "进入章节页               ", "key": "completeMaster"},
    {"name": "进入知识点               ", "key": "enterTopic"},
    # {"name": "进入学习视频或练习     ", "key": ""},
    # {"name": "完成第一个学习视频或专题", "key": ""},
    # {"name": "完成学习模块或练习模块  ", "key": ""},
    {"name": "进入学习视频             ", "key": "startLearning"},
    {"name": "进入练习                 ", "key": "startMaster"},
    {"name": "完成一个学习视频          ", "key": "finishVideo"},
    {"name": "完成一个专题             ", "key": "problemSetSuccess"},
    {"name": "完成学习模块             ", "key": "completeLearning"},
    {"name": "完成练习模块             ", "key": "completeMaster"}]


filename = '../data/新用户数据'+str(START_DATE.date()) + '--' + str((END_DATE - datetime.timedelta(days=1)).date()) + ".txt"
f = open(filename, 'w')

print("---------- 新用户当天行为 ----------", file=f)
for i in range(days):
    start = START_DATE_UTC + datetime.timedelta(days=i)
    end = start + datetime.timedelta(days=1)
    start_date = start.date() + datetime.timedelta(days=1)

    print("---------- ", start_date, ' ----------', file=f)
    print("---------- ", start_date, ' ----------')
    print("-------------- PC端 --------------", file=f)
    # pc_new_user = new_user_count(start, end, 'pc')
    # print("新用户数: ", pc_new_user, file=f)
    # print("新用户数: ", pc_new_user)

    users_dict = calc_user_device(start, end, ['pc'])
    event_flow = collect_event(start, end, users_dict, ['pc'])
    print('新用户数: ', len(users_dict['hasUsers']), file=f)
    for event in events_pc:
        pv_uv = pv_uv_count(event_flow, event['key'])
        # pv_uv = new_user_pv_uv(start, end, 'pc', event['key'])
        print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f)

    print("------------ android ------------", file=f)
    # android_new_user = new_user_count(start, end, 'android') + mobile_new_unregistered_count(start, end, 'android')
    # print("新用户数: ", android_new_user, file=f)
    # print("新用户数: ", android_new_user)

    users_dict = calc_user_device(start, end, ['android'])
    event_flow = collect_event(start, end, users_dict, ['android'])
    print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f)
    for event in events_mobile:
        pv_uv = pv_uv_count(event_flow, event['key'])
        # pv_uv = new_user_pv_uv(start, end, 'android', event['key'])
        print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f)

    print("-------------- iOS ---------------", file=f)
    # ios_new_user = new_user_count(start, end, 'ios') + mobile_new_unregistered_count(start, end, 'ios')
    # print("新用户数: ", ios_new_user, file=f)
    # print("新用户数: ", ios_new_user)

    users_dict = calc_user_device(start, end, ['ios'])
    event_flow = collect_event(start, end, users_dict, ['ios'])
    print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f)

    for event in events_mobile:
        pv_uv = pv_uv_count(event_flow, event['key'])
        # pv_uv = new_user_pv_uv(start, end, 'ios', event['key'])
        print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f)
    print('\n', file=f)
f.close()

start1 = datetime.datetime(2015, 12, 19)
end1 = datetime.datetime(2016, 1, 4)

start1_utc = start1 - datetime.timedelta(hours=8)
end1_utc = end1 - datetime.timedelta(hours=8)

filename1 = '../data/'+str(start1.date()) + '--' + str((end1 - datetime.timedelta(days=1)).date()) + " total.txt"
f1 = open(filename1, 'w')

print("---------- 新用户 2015-12-19 - 2016-01-03 行为 ----------", file=f1)
print("-------------- PC端 --------------", file=f1)
# pc_new_user = new_user_count(start1_utc, end1_utc, 'pc')
# print("新用户数: ", pc_new_user, file=f1)
# print("新用户数: ", pc_new_user)

users_dict = calc_user_device(start1_utc, end1_utc, ['pc'])
event_flow = collect_event(start1_utc, end1_utc, users_dict, ['pc'])
print('新用户数: ', len(users_dict['hasUsers']), file=f1)


for event in events_pc:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f1)

print("------------ android ------------", file=f1)
# android_new_user = new_user_count(start1_utc, end1_utc, 'android') + mobile_new_unregistered_count(start1_utc, end1_utc, 'android')
# print("新用户数: ", android_new_user, file=f1)
# print("新用户数: ", android_new_user)

users_dict = calc_user_device(start1_utc, end1_utc, ['android'])
event_flow = collect_event(start1_utc, end1_utc, users_dict, ['android'])
print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f1)

for event in events_mobile:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f1)

print("-------------- iOS ---------------", file=f1)
# ios_new_user = new_user_count(start1_utc, end1_utc, 'ios') + mobile_new_unregistered_count(start1_utc, end1_utc, 'ios')
# print("新用户数: ", ios_new_user, file=f1)
# print("新用户数: ", ios_new_user)

users_dict = calc_user_device(start1_utc, end1_utc, ['ios'])
event_flow = collect_event(start1_utc, end1_utc, users_dict, ['ios'])
print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f1)

for event in events_mobile:
    pv_uv = pv_uv_count(event_flow, event['key'])
    # pv_uv = new_user_pv_uv(start1_utc, end1_utc, 'ios', event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f1)
f1.close()


start2 = datetime.datetime(2015, 12, 21)
end2 = datetime.datetime(2015, 12, 28)

start2_utc = start2 - datetime.timedelta(hours=8)
end2_utc = end2 - datetime.timedelta(hours=8)


filename2 = '../data/'+str(start2.date()) + '--' + str((end2 - datetime.timedelta(days=1)).date()) + " total.txt"
f2 = open(filename2, 'w')

print("---------- 新用户 2015-12-21 - 2015-12-27 行为 ----------", file=f2)
print("-------------- PC端 --------------", file=f2)
# pc_new_user = new_user_count(start2_utc, end2_utc, 'pc')
# print("新用户数: ", pc_new_user, file=f2)

users_dict = calc_user_device(start2_utc, end2_utc, ['pc'])
event_flow = collect_event(start2_utc, end2_utc, users_dict, ['pc'])
print('新用户数: ', len(users_dict['hasUsers']), file=f)


for event in events_pc:
    # pv_uv = new_user_pv_uv(start2_utc, end2_utc, 'pc', event['key'])
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f2)

print("------------ android ------------", file=f2)
# android_new_user = new_user_count(start2_utc, end2_utc, 'android') + mobile_new_unregistered_count(start2_utc, end2_utc, 'android')
# print("新用户数: ", android_new_user, file=f2)


users_dict = calc_user_device(start2_utc, end2_utc, ['android'])
event_flow = collect_event(start2_utc, end2_utc, users_dict, ['android'])
print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f2)

for event in events_mobile:
    # pv_uv = new_user_pv_uv(start2_utc, end2_utc, 'android', event['key'])
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f2)

print("-------------- iOS ---------------", file=f2)
# ios_new_user = new_user_count(start2_utc, end2_utc, 'ios') + mobile_new_unregistered_count(start2_utc, end2_utc, 'ios')
# print("新用户数: ", ios_new_user, file=f2)

users_dict = calc_user_device(start2_utc, end2_utc, ['ios'])
event_flow = collect_event(start2_utc, end2_utc, users_dict, ['ios'])
print('新用户数: ', len(users_dict['hasUsers']) + len(users_dict['notUsers']), file=f2)

for event in events_mobile:
    # pv_uv = new_user_pv_uv(start2_utc, end2_utc, 'ios', event['key'])
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], "uv: ", pv_uv['uv'], " pv: ", pv_uv['pv'], file=f2)
f2.close()

e = time.time()
print("Total time: ", int((e-s)/60), ' min')