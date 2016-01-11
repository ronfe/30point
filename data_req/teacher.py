# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *

s = time.time()

START_DATE = datetime.datetime(2015, 12, 30)
END_DATE = START_DATE + datetime.timedelta(days=7)

ONLINE_30 = datetime.datetime(2015, 12, 18, 16)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)


events_create_room = [
    {"name": "点击创建班级", "key": "createClassroom"},
    {"name": "创建班级成功", "key": "createClassroomSuccess"},
    {"name": "选择前往添加学生", "key": "clickInstantInsertStudent"}
]


events_add_students = [
    {"name": "选择批量创建学生", "key": "initBatchInsert"},
    {"name": "批量创建成功", "key": "batchInsertSuccess"},
    {"name": "批量创建成功后生成学生账号列表", "key": "createStuList"},
    {"name": "下载账号列表", "key": "downloadStuList"},
    {"name": "打印账号列表", "key": "printStuList"},

    {"name": "选择让学生自己注册", "key": "initNaturalInsert"},
    {"name": "查看注册指南", "key": "enterNaturalListPage"},
    {"name": "打印注册指南", "key": "printNaturalList"},
    {"name": "下载注册指南", "key": "downloadNaturalList"},
]


events_room_data = [
    {"name": "进入【班级数据】页面", "key": "enterClassroomInfo"},
    {"name": "点击【查看完成名单】", "key": "checkTopicCompleteList"},
    {"name": "点击【查看视频】", "key": "checkVideo"},
    {"name": "点击【查看习题】", "key": "checkProblem"},
    {"name": "用户查看的知识点内有大于5道错题时，点击【查看更多错题】的比例", "key": "checkMoreMistakes"},
    {"name": "展开题目", "key": "openOneProblem"},
    {"name": "点击【收起】按钮", "key": "closeOneProblem"},
]

events_room_data2 = [
    {"name": "查看【班级数据】页面次数分布", "key": "enterClassroomInfo"},
    {"name": "查看知识点数量分布", "key": "selectTopic"}
]


# 进入第几屏 埋点??????????????????
events_manual = [
    {"name": "进入使用指南", "key": "enterTeacherGuide"},
    # {"name": "进入第一屏", "key": ""},
    # {"name": "进入第二屏", "key": ""},
    # {"name": "进入第三屏", "key": ""},
    # {"name": "进入第四屏", "key": ""},
    # {"name": "进入第五屏", "key": ""},
    # {"name": "进入第六屏", "key": ""},
    {"name": "第一屏【查看课程内容】按钮点击", "key": "clickGuideCourseContent"},
    {"name": "第一屏【让学生加入】按钮点击", "key": "clickGuide1InviteStudents"},
    {"name": "第二屏【查看趣味视频】按钮点击", "key": "clickGuideFeaturedVideo"},
    {"name": "第二屏【让学生加入】按钮点击", "key": "clickGuide2InviteStudents"},
    {"name": "第二屏抽象概念可视化【播放视频】按钮点击", "key": "clickGuide2FirstVideo"},
    {"name": "第二屏趣味性【播放视频】按钮点击", "key": "clickGuide2SecondVideo"},
    {"name": "第二屏认知节奏感【播放视频】按钮点击", "key": "clickGuide2ThirdVideo"},
    {"name": "第三屏【查看专题训练】按钮点击", "key": "clickGuideProblemSet"},
    {"name": "第三屏【让学生加入】按钮点击", "key": "clickGuide3InviteStudents"},
    {"name": "第三屏专题一和专题二中层的点击", "key": "clickGuideProblemSetTab"},
    {"name": "第四屏【查看班级数据】按钮点击", "key": "clickGuideRoomData"},
    {"name": "第四屏【让学生加入】按钮点击", "key": "clickGuide4InviteStudents"},
    {"name": "第五屏-北大附中案例预览", "key": "clickGuide5FirstView"},
    {"name": "第五屏-北大附中案例下载", "key": "clickGuide5FirstDownload"},
    {"name": "第五屏-三十五中案例预览", "key": "clickGuide5SecondView"},
    {"name": "第五屏-三十五中案例下载", "key": "clickGuide5SecondDownload"},
    {"name": "第五屏-人大附中案例预览", "key": "clickGuide5ThirdView"},
    {"name": "第五屏-人大附中案例下载", "key": "clickGuide5ThirdDownload"},
    {"name": "第五屏-十一学校案例预览", "key": "clickGuide5FourthView"},
    {"name": "第五屏-十一学校案例下载", "key": "clickGuide5FourthDownload"},
    {"name": "第六屏【创建班级】按钮点击", "key": "clickGuideCreateClassroom"},

]


events_else = [
    {"name": "教师后台首页-演示班级查看", "key": "checkExampleClassroom"},
    {"name": "视频播放页面-让学生加入", "key": "clickBannerInsert"},
    {"name": "视频播放页面-稍后再说", "key": ""},  #????????
    {"name": "习题页面-让学生加入", "key": ""},
    {"name": "习题页面-稍后再说", "key": ""},
]


def new_teacher(start, end):
    return users.count({
        "role": "teacher",
        "registTime": {"$gte": start, "$lt": end}
    })


def teacher_room_distribution():
    pipeline = [
        {
            "$match": {
                "role": "teacher",
                "registTime": {"$lt": ONLINE_30}
            }
        },
        {
            "$group": {
                "_id": None,
                "count": {"$push": {"$size": "$rooms"}}
            }
        }
    ]
    room_count = list(users.aggregate(pipeline))[0]['count']
    room_bucket = {}
    for c in room_count:
        if c in room_bucket:
            room_bucket[c] += 1
        else:
            room_bucket[c] = 1
    return room_bucket


def batch_count(start, end):
    return users.count({
        "type": "batch",
        "registTime": {"$gte": start, "$lt": end}
    })


def batch_activate_count(start, end):
    return users.count({
        "type": "batch",
        "activateDate": {"$gte": start, "$lt": end}
    })


def room_has_student_count():
    pipeline = [
        {
            "$match": {
                "role": "student",
                "registTime": {"$lt": ONLINE_30}
            }
        },
        {
            "$unwind": {
                "path": "$rooms"
            }
        },
        {
            "$group": {
                "_id": None,
                "rooms": {"$addToSet": "$rooms"}
            }
        }
    ]
    rooms = list(users.aggregate(pipeline))
    return len(rooms[0]['rooms'])


def event_count_distribution(event_flow, event_key):
    res = {}
    for e in event_flow:
        c = e.count(event_key)
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


# 不同页面创建班级成功的埋点 是不同 还是只是url不同?????
def create_room_main():
    pass
    # eventKey : createClassroom createClassroomSuccess


def create_room_banner():
    pass
    # key: clickBannerInsert enterBannerCreateClassroomSuccessModal


def create_room_manual():
    pass
    # key: clickGuideCreateClassroom


#  时间段???????????

users_dict = calc_user_device(START_DATE_UTC, END_DATE_UTC, ['pc'])
event_flow = collect_event(START_DATE_UTC, END_DATE_UTC, users_dict, ['pc'])


print(event_count_distribution(event_flow, 'enterClassroomInfo'))
print(event_count_distribution(event_flow, 'selectTopic'))


print('----------- 教师数据报告', START_DATE.date(), '-', (END_DATE-datetime.timedelta(days=1)).date(), '-----------')
print('---------- 规模数据 ----------')
print('本周新增教师用户数: ', new_teacher(START_DATE_UTC, END_DATE_UTC))
print('3.0教师创建班级分布: ', teacher_room_distribution())
print('3.0有学生的班级数: ', room_has_student_count())
print('本周批量创建学生数: ', batch_count(START_DATE_UTC, END_DATE_UTC))
print('本周批量创建激活学生数: ', batch_activate_count(START_DATE_UTC, END_DATE_UTC))

print('---------- 创建班级 ----------')

for event in events_create_room:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'])
# print('在使用手册页面创建班级成功率', create_room_manual())
# print('后台首页创建班级成功率', create_room_main())
# print('在内循环页面创建班级成功率', create_room_banner())


print('---------- 添加学生 ----------')
for event in events_add_students:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'])

print('---------- 班级数据 ----------')
for event in events_room_data:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'])
for event in events_room_data2:
    print(event['name'], event_count_distribution(event_flow, event['key']))


print('---------- 使用指南 ----------')
for event in events_manual:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'])

print('---------- 其他 ----------')
for event in events_else:
    pv_uv = pv_uv_count(event_flow, event['key'])
    print(event['name'], ' uv: ', pv_uv['uv'], ' pv: ', pv_uv['pv'])