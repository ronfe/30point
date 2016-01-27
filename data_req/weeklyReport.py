# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *
import time
from collections import OrderedDict

s = time.time()


ONLINE_30 = datetime.datetime(2015, 12, 18, 16)
START_DATE = datetime.datetime(2016, 1, 17) - datetime.timedelta(hours=8)
END_DATE = START_DATE + datetime.timedelta(days=7)

LAST_WEEK_START_DATE = START_DATE - datetime.timedelta(days=7)
LAST_WEEK_END_DATE = START_DATE

filename = '../data/数据周报' + str((START_DATE + datetime.timedelta(days=1)).date()) + '-' + str(END_DATE.date()) + '.txt'
f = open(filename, 'w')

print('---------- 数据周报 ', (START_DATE + datetime.timedelta(days=1)).date(), '-', END_DATE.date(), ' ----------\n', file=f)

print('---------- 视频播放PV ----------\n', file=f)


def video_play_pv(start, end, platform, event):
    return events.count({
        "eventKey": event,
        "platform2": platform,
        "serverTime": {"$gte": start, "$lt": end}
    })

eventKey = 'startVideo'
iosVideoPlay = video_play_pv(START_DATE, END_DATE, 'iOS', eventKey) + video_play_pv(START_DATE, END_DATE, 'iOS', 'startLearning')
androidVideoPlay = video_play_pv(START_DATE, END_DATE, 'android', eventKey)
pcVideoPlay = video_play_pv(START_DATE, END_DATE, 'PC', eventKey)

print('PC本周视频播放数: ', str(pcVideoPlay), '\n', file=f)
print('android本周视频播放数: ', str(androidVideoPlay), '\n', file=f)
print('iOS本周视频播放数: ', str(iosVideoPlay), '\n', file=f)
print('本周视频播放总数: ', str(iosVideoPlay + androidVideoPlay + pcVideoPlay), '\n', file=f)


print('---------- 总用户数 ----------\n', file=f)


def user_count_30(platform):
    return users.count({
        "from": platform,
        "$or": [
            {"type": {"$ne": "batch"}, "registTime": {"$gte": ONLINE_30, "$lt": END_DATE}},
            {"type": "batch", "activateDate": {"$gte": ONLINE_30, "$lt": END_DATE}}
        ]
    })


def user_count_25(platform):
    return users25.count({
        "from": platform,
        "$or": [
            {"type": {"$ne": "batch"}, "registTime": {"$lt": ONLINE_30}},
            {"type": "batch", "activateDate": {"$lt": ONLINE_30}}
        ]
    })


def mobile_unregistered(platforms):
    return deviceAttr.count({
        "platform": {"$in": platforms},
        "users.0": {"$exists": False}
    })

pcUser25 = 267984  # user_count_25('pc')
androidUser25 = 180068  # user_count_25('android')
iosUser25 = 43430  # user_count_25('ios')

pcActUser = pcUser25 + user_count_30('pc')
androidActUser = androidUser25 + user_count_30('android')
iosActUser = iosUser25 + user_count_30('ios')
androidUnregistered = mobile_unregistered(['android'])
iosUnregistered = mobile_unregistered(['ios'])

print('总用户数: ', pcActUser + androidActUser + iosActUser + androidUnregistered + iosUnregistered, '\n', file=f)
print('PC端累计活跃用户数: ' + str(pcActUser) + '\n', file=f)
print('移动端总用户数: ' + str(androidActUser + iosActUser + androidUnregistered + iosUnregistered),
      '  注册: ', androidActUser + iosActUser, '  未注册: ', androidUnregistered + iosUnregistered, '\n', file=f)
print ('android总用户数: ', str(androidActUser + androidUnregistered),
       '   注册: ', androidActUser, '  未注册: ', androidUnregistered, '\n', file=f)
print ('iOS总用户数: ', str(iosActUser + iosUnregistered),
       '   注册: ', iosActUser, '  未注册: ', iosUnregistered, '\n', file=f)


print('---------- 新增用户数 ----------\n', file=f)


def new_user(start, end, platform):
    user_list = list(users.find({
        "from": platform,
        "$or": [
            {"type": {"$ne": "batch"}, "registTime": {"$gte": start, "$lt": end}},
            {"type": "batch", "activateDate": {"$gte": start, "$lt": end}}]
    },
            {"_id": 1}))
    user_ids = [u['_id'] for u in user_list]
    return user_ids


def mobile_new_unregistered(start, end, platforms):
    user_list = list(deviceAttr.find({
        "users.0": {"$exists": False},
        "activateDate": {"$gte": start, "$lt": end},
        "platform": {"$in": platforms}
    }, {"device": 1}))
    user_ids = [u['device'] for u in user_list]
    return user_ids


def new_user_by_type(start, end, types):
    return users.count({
        "type": {"$in": types},
        "registTime": {"$gte": start, "$lt": end}
    })


# 'cyxt'/*朝阳学堂*/,'bjxxt'/*北京校讯通*/, 'cqxxt'/*重庆校讯通*/, 'lnxxt'/*辽宁校讯通*/,
# 'ynxxt'/*云南校讯通*/, 'tjxxt'/*天津校讯通*/, 'twsm'/*天闻数媒*/, 'eduyun'/*国家教育资源公共服务平台*/
def new_user_by_third_party(start, end):
    return users.count({
        "type": {"$nin": ["signup", "batch", "qq"]},
        "registTime": {"$gte": start, "$lt": end}
    })


def new_user_batch(start, end):
    return users.count({
        "type": 'batch',
        "activateDate": {"$gte": start, "$lt": end}
    })

pcNewUser = len(new_user(START_DATE, END_DATE, 'pc'))
androidNewUser = len(new_user(START_DATE, END_DATE, 'android'))
iosNewUser = len(new_user(START_DATE, END_DATE, 'ios'))
androidNewUnregistered = len(mobile_new_unregistered(START_DATE, END_DATE, ['android']))
iosNewUnregistered = len(mobile_new_unregistered(START_DATE, END_DATE, ['ios']))
mobileNewUnregistered = androidNewUnregistered + iosNewUnregistered
qqNewUser = new_user_by_type(START_DATE, END_DATE, ['qq'])
thirdPartyNewUser = new_user_by_third_party(START_DATE, END_DATE)
batchNewUser = new_user_batch(START_DATE, END_DATE)


print('本周新增用户数: ', pcNewUser + androidNewUser + iosNewUser + mobileNewUnregistered, '\n', file=f)
print('PC端本周新增用户数: ' + str(pcNewUser) + '\n', file=f)
print('移动端本周新增用户数: ' + str(androidNewUser + iosNewUser + mobileNewUnregistered),
      '  注册: ', (androidNewUser + iosNewUser), '  未注册: ', mobileNewUnregistered, '\n', file=f)
print('android本周新增用户数: ', androidNewUser + androidNewUnregistered,
      '  注册: ', androidNewUser, '  未注册: ', androidNewUnregistered, '\n', file=f)
print('iOS本周新增用户数: ', iosNewUser + iosNewUnregistered,
      '  注册: ', iosNewUser, '  未注册: ', iosNewUnregistered, '\n', file=f)

print('本周首次QQ登录用户: ' + str(qqNewUser) + '\n', file=f)
print('本周首次第三方登录用户: ', str(thirdPartyNewUser), '\n', file=f)
print('本周批量创建激活用户: ' + str(batchNewUser) + '\n', file=f)


print('---------- 活跃用户数 ----------\n', file=f)


def active_user(start, end, platform):
    recent_session = 'recentPCSession' if platform is 'pc' else 'recentMobileSession'
    return list(userAttr.find({recent_session: {"$gte": start, "$lt": end}}))


def active_user_unregistered(start, end):
    return list(deviceAttr.find({
        "platform": {"$in": ["android", "ios"]},
        "recentSession": {"$gte": start, "$lt": end},
        "users.0": {"$exists": False},
    }))


def both_active_user(start, end):
    return userAttr.count({
        "recentPCSession": {"$gte": start, "$lt": end},
        "recentMobileSession": {"$gte": start, "$lt": end}
    })

pcActUser = active_user(START_DATE, END_DATE, 'pc')
mobileActUser = active_user(START_DATE, END_DATE, 'mobile')
mobileActUserUnregistered = active_user_unregistered(START_DATE, END_DATE)
bothActUser = both_active_user(START_DATE, END_DATE)

print("本周PC端活跃用户: ", len(pcActUser),  '\n', file=f)
print("本周移动端活跃用户: ", len(mobileActUser) + len(mobileActUserUnregistered), '\n', file=f)
print("本周双端活跃用户: " + str(bothActUser) + '\n', file=f)


print('---------- 去新增活跃用户数 ----------\n', file=f)

# 目的：更深入地分析活跃用户的质量，监控我们的用户质量是否有不正常的起伏
# 定义：定义时间内，刨除掉仅在新增当天活跃过的活跃用户数
# 公式：老活跃用户+定义时间内活跃>=2天的新增用户


def real_active_user(user_list, platform):
    recent_session = 'recentPCSession' if platform is 'pc' else ('recentMobileSession' if platform is 'mobile' else 'recentSession')
    counter = 0
    for user in user_list:
        if (user[recent_session] + datetime.timedelta(hours=8)).date() != (user['activateDate'] + datetime.timedelta(hours=8)).date():
            counter += 1
    return counter

print('本周PC端去新增活跃用户数: ', real_active_user(pcActUser, 'pc'), '\n', file=f)
print('本周移动端去新增活跃用户数: ', real_active_user(mobileActUser, 'mobile') + real_active_user(mobileActUserUnregistered, 'else'),
      '注册:', real_active_user(mobileActUser, 'mobile'), '未注册:', real_active_user(mobileActUserUnregistered, 'else'), '\n', file=f)

print("---------- 首页转化率 ----------\n", file=f)


def convert_rate(start, end, platform, keys):
    users_dict = calc_user_device(start, end, [platform])
    event_flow = collect_event(start, end, users_dict, [platform])
    counter = OrderedDict([(key, 0) for key in keys])
    for flow in event_flow:
        for key in counter:
            ks = key.split('|')
            if any([k in flow for k in ks]):
                counter[key] += 1
            else:
                break
    return counter


home_pc = [
    {"name": "首页访问", "key": "enterHome"},
    {"name": "点击注册", "key": "clickSignupBtn|clickFreeForUseSS"},
    {"name": "进入注册页面", "key": "enterSignupPage"},
    {"name": "注册成功", "key": "signupSuccess"},
    {"name": "开始观看一个视频", "key": "startVideo"},
    {"name": "观看完一个视频", "key": "finishVideo"},
]

home_android = [
    {"name": "首页访问", "key": "enterGuidePage"},
    {"name": "点击注册", "key": "clickUserLogBtn"},
    {"name": "进入注册页面", "key": "enterSignupPage"},
    {"name": "提交注册", "key": "clickSignupBtn"},
    {"name": "注册成功", "key": "registSuccess"},
    {"name": "开始观看一个视频", "key": "startVideo"},
    {"name": "观看完一个视频", "key": "finishVideo"},
]

home_ios = [
    {"name": "点击注册", "key": "clickUserLogBtn"},
    {"name": "进入注册页面", "key": "enterSignupPage"},
    {"name": "提交注册", "key": "clickSignupBtn"},
    {"name": "注册成功", "key": "registSuccess"},
    {"name": "开始观看一个视频", "key": "startVideo"},
    {"name": "观看完一个视频", "key": "finishVideo"},
]

platforms = ['pc', 'android', 'ios']
for p in platforms:
    home = globals()['home_'+p]
    keys = [h['key'] for h in home]
    rate = convert_rate(START_DATE, END_DATE, p, keys)
    values = rate.values()
    print('-----', p, '-----', file=f)
    for i, h in enumerate(home):
        print(h['name'], rate[h['key']], str(round(values[i]*100.0/values[i-1], 2))+'%' if i != 0 else '',
              str(round(values[i]*100.0/values[0], 2))+'%' if i != 0 else '', file=f)
    print('\n', file=f)


print('----------- 周留存 -----------\n', file=f)


last_week_users_pc = new_user(LAST_WEEK_START_DATE, LAST_WEEK_END_DATE, 'pc')
last_week_users_android = new_user(LAST_WEEK_START_DATE, LAST_WEEK_END_DATE, 'android')
last_week_users_ios = new_user(LAST_WEEK_START_DATE, LAST_WEEK_END_DATE, 'ios')
last_week_users_mobile_unregistered = mobile_new_unregistered(LAST_WEEK_START_DATE, LAST_WEEK_END_DATE, ['android', 'ios'])


def count_active(start, end, ids, platform):
    recent_session = "recentPCSession" if platform is "pc" else "recentMobileSession"
    return userAttr.count({
        "user": {"$in": ids},
        recent_session: {"$gte": start, "$lt": end}
    })


def count_active_unregistered(start, end, devices):
    return deviceAttr.count({
        "device": {"$in": devices},
        "recentSession": {"$gte": start, "$lt": end},
    })

this_week_retention_pc = count_active(START_DATE, END_DATE, last_week_users_pc, 'pc')
this_week_retention_mobile = count_active(START_DATE, END_DATE, last_week_users_android, 'android') \
                             + count_active(START_DATE, END_DATE, last_week_users_ios, 'ios') \
                             + count_active_unregistered(START_DATE, END_DATE, last_week_users_mobile_unregistered)

print('pc端上周新增用户: ', len(last_week_users_pc), '\n', file=f)
print('pc端上周新增用户本周留存: ', this_week_retention_pc, '\n', file=f)
print('移动端上周新增用户: ', len(last_week_users_android) + len(last_week_users_ios) + len(last_week_users_mobile_unregistered), '\n', file=f)
print('移动端上周新增用户本周留存: ', this_week_retention_mobile, '\n', file=f)


print('----------- H5首页 -----------\n', file=f)


def h5(start, end, platforms):
    pipeline = [
        {
            "$match": {
                "eventKey": "enterMobileSite",
                "platform": "landing",
                "platform2": {"$in": platforms},
                "serverTime": {"$gte": start, "$lt": end}
            }
        },
        {
            "$group": {
                "_id": "$device",
                "pv": {"$sum": 1}
            }
        },
        {
            "$group": {
                "_id": None,
                "uv": {"$sum": 1},
                "pv": {"$sum": "$pv"}
            }
        }
    ]
    return list(events.aggregate(pipeline))[0]
h5_android = h5(START_DATE, END_DATE, ['android'])
h5_ios = h5(START_DATE, END_DATE, ['iOS'])

print('android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv'], '\n', file=f)
print('iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv'], file=f)


f.close()
e = time.time()
print("Total time: ", (e-s)/60, ' min')
