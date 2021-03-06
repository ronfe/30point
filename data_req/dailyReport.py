# _*_ coding:utf-8 _*_
from __future__ import print_function
from dataFunctions import *
import time
from collections import OrderedDict

s = time.time()


ONLINE_30 = datetime.datetime(2015, 12, 18, 16)

START_DATE = datetime.datetime(2015, 12, 19)
END_DATE = START_DATE + datetime.timedelta(days=1)


START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)

LAST_WEEK_START_DATE_UTC = START_DATE_UTC - datetime.timedelta(days=7)
LAST_WEEK_END_DATE_UTC = START_DATE_UTC

filename = '../data/数据日报' + str(START_DATE.date()) + '-' + str((END_DATE - datetime.timedelta(days=1)).date()) + '.txt'
f = open(filename, 'w')

pc = 'PC'
ios = 'iOS'
android = 'android'

print('---------- 数据日报 ', START_DATE.date(), '-', (END_DATE - datetime.timedelta(days=1)).date(), ' ----------\n', file=f)

print('---------- 视频播放PV ----------\n', file=f)


def video_play_pv(start, end, platform, event):
    query = {
        "eventKey": event,
        "platform2": platform,
        "serverTime": {"$gte": start, "$lt": end}
    }
    return events.count(query)

eventKey = 'startVideo'
iosVideoPlay = video_play_pv(START_DATE_UTC, END_DATE_UTC, ios, eventKey) + video_play_pv(START_DATE_UTC, END_DATE_UTC, ios, 'startLearning')
androidVideoPlay = video_play_pv(START_DATE_UTC, END_DATE_UTC, android, eventKey)
pcVideoPlay = video_play_pv(START_DATE_UTC, END_DATE_UTC, pc, eventKey)

print(pc, '本日视频播放数: ', str(pcVideoPlay), '\n', file=f)
print(android, '本日视频播放数: ', str(androidVideoPlay), '\n', file=f)
print(ios, '本日视频播放数: ', str(iosVideoPlay), '\n', file=f)
print('本日视频播放总数: ', str(iosVideoPlay + androidVideoPlay + pcVideoPlay), '\n', file=f)


print('---------- 总用户数 ----------\n', file=f)


def user_count_30(platform):
    query1 = {
        "from": platform,
        "type": {"$ne": "batch"},
        "registTime": {"$exists": True, "$gte": ONLINE_30, "$lt": END_DATE_UTC}
    }
    query2 = {
        "from": platform,
        "type": "batch",
        "activateDate": {"$exists": True, "$gte": ONLINE_30, "$lt": END_DATE_UTC}
    }
    return users.count(query1) + users.count(query2)


def user_count_25(platform):
    query1 = {
        "from": platform,
        "type": {"$ne": "batch"},
        "registTime": {"$exists": True, "$lt": ONLINE_30}
    }
    query2 = {
        "from": platform,
        "type": "batch",
        "activateDate": {"$exists": True, "$lt": ONLINE_30}
    }
    return users25.count(query1) + users25.count(query2)


def mobile_unregistered(platforms):
    query = {
        "platform": {"$in": platforms},
        "users.0": {"$exists": False}
    }
    return deviceAttr.count(query)

pcUser25 = 267984  #user_count_25('pc')
androidUser25 = 180068  #user_count_25('android')
iosUser25 = 43430  #user_count_25('ios')

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
    query1 = {
        "from": platform,
        "type": {"$ne": "batch"},
        "registTime": {"$gte": start, "$lt": end}
    }
    query2 = {
        "from": platform,
        "type": "batch",
        "activateDate": {"$gte": start, "$lt": end}
    }
    user_list = list(users.find(query1, {"_id": 1})) + list(users.find(query2, {"_id": 1}))
    user_ids = [u['_id'] for u in user_list]
    return user_ids


def mobile_new_unregistered(start, end, platforms):
    query = {
        "users.0": {"$exists": False},
        "activateDate": {"$gte": start, "$lt": end},
        "platform": {"$in": platforms}
    }
    user_list = list(deviceAttr.find(query, {"device": 1}))
    user_ids = [u['device'] for u in user_list]
    return user_ids


# ['qq', "cyxt", "lnxxt", "bjxxt" ]
def new_user_by_type(start, end, types):
    query = {
        "type": {"$in": types},
        "registTime": {"$gte": start, "$lt": end}
    }
    return users.count(query)


# def new_user_third_party(start, end, channel):
#     query = {
#         "channel": {"$in": channel},
#         "registTime": {"$gte": start, "$lt": end}
#     }
#     return users.find(query).count()
#

def new_user_batch(start, end):
    query = {
        "type": 'batch',
        "activateDate": {"$gte": start, "$lt": end}
    }
    return users.count(query)

thirdParty = ["cyxt", "lnxxt", "bjxxt"]

pcNewUser = len(new_user(START_DATE_UTC, END_DATE_UTC, 'pc'))
androidNewUser = len(new_user(START_DATE_UTC, END_DATE_UTC, 'android'))
iosNewUser = len(new_user(START_DATE_UTC, END_DATE_UTC, 'ios'))
androidNewUnregistered = len(mobile_new_unregistered(START_DATE_UTC, END_DATE_UTC, ['android']))
iosNewUnregistered = len(mobile_new_unregistered(START_DATE_UTC, END_DATE_UTC, ['ios']))
mobileNewUnregistered = androidNewUnregistered + iosNewUnregistered
qqNewUser = new_user_by_type(START_DATE_UTC, END_DATE_UTC, ['qq'])
thirdPartyNewUser = new_user_by_type(START_DATE_UTC, END_DATE_UTC, thirdParty)
batchNewUser = new_user_batch(START_DATE_UTC, END_DATE_UTC)


print('本日新增用户数: ', pcNewUser + androidNewUser + iosNewUser + mobileNewUnregistered, '\n', file=f)
print('PC端本日新增用户数: ' + str(pcNewUser) + '\n', file=f)
print('移动端本日新增用户数: ' + str(androidNewUser + iosNewUser + mobileNewUnregistered),
      '  注册: ', (androidNewUser + iosNewUser), '  未注册: ', mobileNewUnregistered, '\n', file=f)
print('android本日新增用户数: ', androidNewUser + androidNewUnregistered,
      '  注册: ', androidNewUser, '  未注册: ', androidNewUnregistered, '\n', file=f)
print('iOS本日新增用户数: ', iosNewUser + iosNewUnregistered,
      '  注册: ', iosNewUser, '  未注册: ', iosNewUnregistered, '\n', file=f)

print('本日首次QQ登录用户: ' + str(qqNewUser) + '\n', file=f)
print('本日首次第三方登录用户: ', str(thirdPartyNewUser), ' (朝阳学堂, 校讯通等)', '\n', file=f)
print('本日批量创建激活用户: ' + str(batchNewUser) + '\n', file=f)

print('---------- 活跃用户数 ----------\n', file=f)


def pc_active_user(start, end):
    return userAttr.count({"recentPCSession": {"$gte": start, "$lt": end}})


def mobile_active_user(start, end):
    reg = userAttr.count({"recentMobileSession": {"$gte": start, "$lt": end}})
    unreg = deviceAttr.count({
        "recentSession": {"$gte": start, "$lt": end},
        "users.0": {"$exists": False}
    })
    return reg + unreg


def both_active_user(start, end):
    return userAttr.count({
        "recentPCSession": {"$gte": start, "$lt": end},
        "recentMobileSession": {"$gte": start, "$lt": end}
    })

pcActUser = pc_active_user(START_DATE_UTC, END_DATE_UTC)
mobileActUser = mobile_active_user(START_DATE_UTC, END_DATE_UTC)
bothActUser = both_active_user(START_DATE_UTC, END_DATE_UTC)

print("本日PC端活跃用户: " + str(pcActUser) + '\n', file=f)
print("本日移动端活跃用户: " + str(mobileActUser) + '\n', file=f)
print("本日双端活跃用户: " + str(bothActUser) + '\n', file=f)


print("---------- 首页转化率 ----------\n", file=f)


def convert_rate(start, end, platform):
    users_dict = calc_user_device(start, end, [platform])
    event_flow = collect_event(start, end, users_dict, [platform])

    if platform is 'pc':
        counter = [('enterHome', 0), ('clickSignupBtn', 0), ('enterSignupPage', 0), ('signupSuccess', 0), ('startVideo', 0), ('finishVideo', 0)]
    elif platform is 'android':
        counter = [('enterGuidePage', 0), ('clickUserLogBtn', 0), ('enterSignupPage', 0), ('clickSignupBtn', 0), ('registSuccess', 0), ('startVideo', 0), ('finishVideo', 0)]
    else:
        counter = [('clickUserLogBtn', 0), ('enterSignupPage', 0), ('clickSignupBtn', 0), ('registSuccess', 0), ('startVideo', 0), ('finishVideo', 0)]
    counter = OrderedDict(counter)

    for flow in event_flow:
        for key in counter:
            if key in flow:
                counter[key] += 1
            else:
                break
    return counter

convert_rate_pc = convert_rate(START_DATE_UTC, END_DATE_UTC, 'pc')
convert_rate_android = convert_rate(START_DATE_UTC, END_DATE_UTC, 'android')
convert_rate_ios = convert_rate(START_DATE_UTC, END_DATE_UTC, 'ios')

print('----- PC -----', file=f)
print('首页访问: ', convert_rate_pc['enterHome'], file=f)
print('点击注册: ', convert_rate_pc['clickSignupBtn'], file=f)
print('进入注册页面: ', convert_rate_pc['enterSignupPage'], file=f)
print('注册成功: ', convert_rate_pc['signupSuccess'], file=f)
print('开始观看一个视频: ', convert_rate_pc['startVideo'], file=f)
print('观看完一个视频: ', convert_rate_pc['finishVideo'], file=f)
print('\n', file=f)
print('----- android -----', file=f)
print('首页访问: ', convert_rate_android['enterGuidePage'], file=f)
print('点击注册: ', convert_rate_android['clickUserLogBtn'], file=f)
print('进入注册页面: ', convert_rate_android['enterSignupPage'], file=f)
print('提交注册: ', convert_rate_android['clickSignupBtn'], file=f)
print('注册成功: ', convert_rate_android['registSuccess'], file=f)
print('开始观看一个视频: ', convert_rate_android['startVideo'], file=f)
print('观看完一个视频: ', convert_rate_android['finishVideo'], file=f)
print('\n', file=f)
print('----- iOS -----', file=f)
print('点击注册: ', convert_rate_ios['clickUserLogBtn'], file=f)
print('进入注册页面: ', convert_rate_ios['enterSignupPage'], file=f)
print('提交注册: ', convert_rate_ios['clickSignupBtn'], file=f)
print('注册成功: ', convert_rate_ios['registSuccess'], file=f)
print('开始观看一个视频: ', convert_rate_ios['startVideo'], file=f)
print('观看完一个视频: ', convert_rate_ios['finishVideo'], file=f)

print('\n', file=f)
print('----------- 日留存 -----------\n', file=f)
last_week_users_pc = new_user(LAST_WEEK_START_DATE_UTC, LAST_WEEK_END_DATE_UTC, 'pc')
last_week_users_android = new_user(LAST_WEEK_START_DATE_UTC, LAST_WEEK_END_DATE_UTC, 'android')
last_week_users_ios = new_user(LAST_WEEK_START_DATE_UTC, LAST_WEEK_END_DATE_UTC, 'ios')
last_week_users_mobile_unregistered = mobile_new_unregistered(LAST_WEEK_START_DATE_UTC, LAST_WEEK_END_DATE_UTC, ['android', 'ios'])


def count_active(start, end, ids, platform):
    recent_session = "recentPCSession" if platform is "pc" else "recentMobileSession"
    query = {
        "user": {"$in": ids},
        recent_session: {"$gte": start, "$lt": end}
    }
    return userAttr.count(query)


def count_active_unregistered(start, end, devices):
    query = {
        "device": {"$in": devices},
        "recentSession": {"$gte": start, "$lt": end}
    }
    return deviceAttr.count(query)

this_week_retention_pc = count_active(START_DATE_UTC, END_DATE_UTC, last_week_users_pc, 'pc')
this_week_retention_mobile = count_active(START_DATE_UTC, END_DATE_UTC, last_week_users_android, 'android') \
                             + count_active(START_DATE_UTC, END_DATE_UTC, last_week_users_ios, 'ios') \
                             + count_active_unregistered(START_DATE_UTC, END_DATE_UTC, last_week_users_mobile_unregistered)

print('pc端上周新增用户: ', len(last_week_users_pc), '\n', file=f)
print('pc端上周新增用户本日留存: ', this_week_retention_pc, '\n', file=f)
print('移动端上周新增用户: ', len(last_week_users_android) + len(last_week_users_ios) + len(last_week_users_mobile_unregistered), '\n', file=f)
print('移动端上周新增用户本日留存: ', this_week_retention_mobile, '\n', file=f)

f.close()
e = time.time()
print("Total time: ", (e-s)/60, ' min')
