# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *

START_DATE = datetime.datetime(2015, 12, 19, 0)
END_DATE = datetime.datetime(2016, 1, 4, 0)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)

events = [
    {"name": "注册成功          ", "key": "signupSuccess"},
    {"name": "首页点击开始       ", "key": "chooseStartNewbieGuide"},
    {"name": "首页点击跳过新手引导", "key": "chooseSkipNewbieGuide"},
    {"name": "选择教材          ", "key": "chooseNewbieBook"},
    {"name": "选择年级          ", "key": "chooseNewbieGrade"},
    {"name": "观看引导视频       ", "key": "startNewbieGuideVideo"},
    {"name": "做题页提交答案      ", "key": "submitNewbieGuideAnswer"},
    {"name": "设定周目标         ", "key": "chooseNewbieTarget"},
    {"name": "完成新手引导       ", "key": "finishNewbieGuide"}
]

filename = '../data/新用户引导行为'+str(START_DATE.date()) + '--' + str((END_DATE - datetime.timedelta(days=1)).date()) + ".txt"
f = open(filename, 'w')


users_dict = calc_user_device(START_DATE_UTC, END_DATE_UTC, ['pc'])
event_flow = collect_event(START_DATE_UTC, END_DATE_UTC, users_dict, ['pc'])
print('---------- 新用户引导行为', START_DATE.date(), '-', END_DATE.date()-datetime.timedelta(days=1), '----------', file=f)
print('新用户数:              ', len(users_dict['hasUsers']), file=f)

for event in events:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], 'uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'], file=f)

f.close()














# events = [
#     {"name": "新用户，学生从注册页进入新用户引导", "key": "signupSuccess"},
#     {"name": "新用户引导首页点击\"开始\"", "key": "chooseStartNewbieGuide"},
#     {"name": "新用户引导首页点击\"跳过新手引导\"", "key": "chooseSkipNewbieGuide"},
#     {"name": "第一页选择年级", "key": "chooseNewbieGrade"},
#     {"name": "第一页选择教材", "key": "chooseNewbieBook"},
#     {"name": "第一页点击\"继续\"", "key": "startNewbieGuideVideo"},
#     {"name": "第一页点击\"跳过此步骤\"", "key": ""},
#     {"name": "第二页点击\"继续\"", "key": ""},
#     {"name": "第二页视频内交互，点击选项", "key": ""},
#     {"name": "第二页点击\"跳过此步骤\"", "key": ""},
#     {"name": "第三页点击页头\"继续\"", "key": ""},
#     {"name": "第三页点击\"查看解析\"", "key": ""},
#     {"name": "第三页点击\"提交\"", "key": "submitNewbieGuideAnswer"},
#     {"name": "第三页点击\"返回题目\"", "key": ""},
#     {"name": "第三页做完题点击\"继续\"", "key": ""},
#     {"name": "第三页点击\"跳过此步骤\"", "key": ""},
#     {"name": "第四页选择周目标", "key": "chooseNewbieTarget"},
#     {"name": "第四页点击\"进入我的学习\"", "key": "finishNewbieGuide"}
# ]
#

events = [
    {"name": "新用户，学生从注册页进入新用户引导", "key": "signupSuccess"},
    {"name": "新用户引导首页点击\"开始\"", "key": "chooseStartNewbieGuide"},
    {"name": "新用户引导首页点击\"跳过新手引导\"", "key": "chooseSkipNewbieGuide"},
    {"name": "第一页选择年级", "key": "chooseNewbieGrade"},
    {"name": "第一页选择教材", "key": "chooseNewbieBook"},
    {"name": "第二页观看引导视频", "key": "startNewbieGuideVideo"},
    # {"name": "第一页点击\"跳过此步骤\"", "key": ""},
    # {"name": "第二页点击\"继续\"", "key": ""},
    # {"name": "第二页视频内交互，点击选项", "key": ""},
    # {"name": "第二页点击\"跳过此步骤\"", "key": ""},
    # {"name": "第三页点击页头\"继续\"", "key": ""},
    # {"name": "第三页点击\"查看解析\"", "key": ""},
    {"name": "第三页提交答案", "key": "submitNewbieGuideAnswer"},
    # {"name": "第三页点击\"返回题目\"", "key": ""},
    # {"name": "第三页做完题点击\"继续\"", "key": ""},
    # {"name": "第三页点击\"跳过此步骤\"", "key": ""},
    {"name": "第四页选择周目标", "key": "chooseNewbieTarget"},
    {"name": "完成新手引导", "key": "finishNewbieGuide"}
]











