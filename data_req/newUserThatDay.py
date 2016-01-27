# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *

platforms = ['pc', 'android', 'ios']
events_platform = dict()
events_platform['pc'] = [
    {"name": "进入启动页面             ", "key": "enterHome"},
    {"name": "启动页点击免费使用        ", "key": "clickFreeForUseSS"},
    {"name": "启动页点击注册           ", "key": "clickSignupBtn"},
    {"name": "进入注册页              ", "key": "enterSignupPage", "pre": 0},
    {"name": "在注册页点击学生         ", "key": "chooseStudentRole"},
    {"name": "在注册页点击教师         ", "key": "chooseTeacherRole"},
    {"name": "注册成功                ", "key": "signupSuccess", "pre": 3},
    {"name": "完成注册点击我的学习      ", "key": "clickMyLearning"},
    {"name": "进入章节页               ", "key": "startChapter", "pre": 6},
    {"name": "进入知识点               ", "key": "enterTopic", "pre": 8},
    {"name": "进入学习视频             ", "key": "startLearning", "pre": 9},
    {"name": "进入练习                ", "key": "startMaster", "pre": 9},
    {"name": "完成一个学习视频         ", "key": "finishVideo", "pre": 10},
    {"name": "完成一个专题            ", "key": "problemSetSuccess", "pre": 11},
    {"name": "完成学习模块            ", "key": "completeLearning", "pre": 10},
    {"name": "完成练习模块            ", "key": "completeMaster", "pre": 11}
]

events_platform['android'] = [
    {"name": "进入启动页面             ", "key": "enterGuidePage"},
    {"name": "启动页点击免费使用        ", "key": "clickExperience"},
    {"name": "进入注册页               ", "key": "enterSignupPage"},
    {"name": "完成注册                 ", "key": "registSuccess"},
    {"name": "进入章节页               ", "key": "completeMaster"},
    {"name": "进入知识点               ", "key": "enterTopic", "pre": 0},
    {"name": "进入学习视频             ", "key": "startLearning", "pre": 5},
    {"name": "进入练习                 ", "key": "startMaster", "pre": 5},
    {"name": "完成一个学习视频          ", "key": "finishVideo", "pre": 6},
    {"name": "完成一个专题             ", "key": "problemSetSuccess", "pre": 7},
    {"name": "完成学习模块             ", "key": "completeLearning", "pre": 6},
    {"name": "完成练习模块             ", "key": "completeMaster", "pre": 7}]

events_platform['ios'] = [
    {"name": "启动页点击免费使用        ", "key": "clickExperience"},
    {"name": "进入注册页               ", "key": "enterSignupPage"},
    {"name": "完成注册                 ", "key": "registSuccess"},
    {"name": "进入章节页               ", "key": "completeMaster"},
    {"name": "进入知识点               ", "key": "enterTopic"},
    {"name": "进入学习视频             ", "key": "startLearning", "pre": 4},
    {"name": "进入练习                 ", "key": "startMaster", "pre": 4},
    {"name": "完成一个学习视频          ", "key": "finishVideo", "pre": 5},
    {"name": "完成一个专题             ", "key": "problemSetSuccess", "pre": 6},
    {"name": "完成学习模块             ", "key": "completeLearning", "pre": 5},
    {"name": "完成练习模块             ", "key": "completeMaster", "pre": 6}]


def data_by_day(start, end):
    ss = time.time()
    days = (end - start).days
    filename = '../data/新用户行为漏斗'+str((start+datetime.timedelta(days=1)).date()) + '-' + str(end.date()) + ".txt"
    f = open(filename, 'w')
    print("------------- 新用户", (start+datetime.timedelta(days=1)).date(), "-", end.date(), "行为 -------------", file=f)
    for p in platforms:
        print('-----------------', p, "-----------------", file=f)
        users_dict = calc_user_device(start, end, [p])
        event_flow = collect_event(start, end, users_dict, [p])
        num_new_user = len(users_dict['hasUsers']) + (0 if p == 'pc' else len(users_dict['notUsers']))
        print('新用户数                     ', num_new_user, file=f)
        pv_uv_list = []
        for event in events_platform[p]:
            pv_uv = pv_uv_count(event_flow, event['key'])
            pv_uv_list.append(pv_uv)
            pv_rate = str(round(pv_uv['pv']*100.0/pv_uv_list[event['pre']]['pv'], 2))+'%' if 'pre' in event else ''
            uv_rate = str(round(pv_uv['uv']*100.0/pv_uv_list[event['pre']]['uv'], 2))+'%' if 'pre' in event else ''
            print(event['name'], "uv: ", pv_uv['uv'], uv_rate, " pv: ", pv_uv['pv'], pv_rate, file=f)
    print('\n', file=f)

    print("------------- 新用户当天行为 -------------", file=f)
    for i in range(days):
        s = start + datetime.timedelta(days=i)
        e = s + datetime.timedelta(days=1)
        start_date = s.date() + datetime.timedelta(days=1)

        print("------------- ", start_date, ' -------------', file=f)
        print("---------- ", start_date, ' ----------')

        for p in platforms:
            print('-----------------', p, "-----------------", file=f)
            users_dict = calc_user_device(s, e, [p])
            event_flow = collect_event(s, e, users_dict, [p])
            num_new_user = len(users_dict['hasUsers']) + (0 if p == 'pc' else len(users_dict['notUsers']))
            print('新用户数                     ', num_new_user, file=f)
            pv_uv_list = []
            for event in events_platform[p]:
                pv_uv = pv_uv_count(event_flow, event['key'])
                pv_uv_list.append(pv_uv)
                pv_rate = str(round(pv_uv['pv']*100.0/pv_uv_list[event['pre']]['pv'], 2))+'%' if 'pre' in event else ''
                uv_rate = str(round(pv_uv['uv']*100.0/pv_uv_list[event['pre']]['uv'], 2))+'%' if 'pre' in event else ''
                print(event['name'], "uv: ", pv_uv['uv'], uv_rate, " pv: ", pv_uv['pv'], pv_rate, file=f)
    f.close()
    ee = time.time()
    print('新用户当天行为 运行用时: ', (ee-ss)/ 60, 'min' )

