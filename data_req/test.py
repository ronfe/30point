# _*_ coding=utf-8 _*_
from pymongo import MongoClient
import datetime
from dataFunctions import *
from bson.objectid import ObjectId
import time
from collections import OrderedDict
# cache = MongoClient(host='10.8.8.111', port=27017)['cache']
# deviceAttr = cache['deviceAttr']
#
# db = MongoClient('10.8.8.111', 27017)['onionsBackupOnline']
# users = db['users']
# events = db['events']

START_DATE = datetime.datetime(2016, 1, 17) - datetime.timedelta(hours=8)
END_DATE = START_DATE + datetime.timedelta(days=7)

print("---------- 首页转化率 ----------\n")


def convert_rate(start, end, platform, keys):
    users_dict = calc_user_device(start, end, [platform])
    event_flow = collect_event(start, end, users_dict, [platform])
    counter = [(key, 0) for key in keys]
    counter = OrderedDict(counter)

    for flow in event_flow:
        for key in counter:
            keys = key.split('|')
            if any([k in flow for k in keys]):
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
    print '-----', p, '-----'
    for i, h in enumerate(home):
        print h['name'], values[i], str(round(values[i]*100.0/values[i-1], 2))+'%' if i != 0 else ''
    print '\n'


# LAST_WEEK_START_DATE = START_DATE - datetime.timedelta(days=7)
# LAST_WEEK_END_DATE = START_DATE
#
#
# def new_user(start, end, platform):
#     user_list = list(users.find({
#         "from": platform,
#         "$or": [
#             {"type": {"$ne": "batch"}, "registTime": {"$gte": start, "$lt": end}},
#             {"type": "batch", "activateDate": {"$gte": start, "$lt": end}}]
#     },
#             {"_id": 1}))
#     user_ids = [u['_id'] for u in user_list]
#     return user_ids
# pcNewUser = len(new_user(LAST_WEEK_START_DATE, LAST_WEEK_END_DATE, 'pc'))
# print LAST_WEEK_START_DATE, LAST_WEEK_END_DATE
# print pcNewUser
#
#
#
# START_DATE = datetime.datetime(2016, 1, 3) - datetime.timedelta(hours=8)
# END_DATE = START_DATE + datetime.timedelta(days=7)
#
# LAST_WEEK_START_DATE = START_DATE - datetime.timedelta(days=7)
# LAST_WEEK_END_DATE = START_DATE
#
#
# def new_user(start, end, platform):
#     user_list = list(users.find({
#         "from": platform,
#         "$or": [
#             {"type": {"$ne": "batch"}, "registTime": {"$gte": start, "$lt": end}},
#             {"type": "batch", "activateDate": {"$gte": start, "$lt": end}}]
#     },
#             {"_id": 1}))
#     user_ids = [u['_id'] for u in user_list]
#     return user_ids
# pcNewUser = len(new_user(START_DATE, END_DATE, 'pc'))
# print START_DATE, END_DATE
# print pcNewUser


# # cyxt = users.distinct('_id', {'type': "cyxt"})
# topicId = "54c708798bac81fccbd4bb53"
# s = time.time()
# start = datetime.datetime(2015, 12, 21)
# end = datetime.datetime(2015, 12, 22)
#
# # eventKeys = list(db.events.find({
# #     "platform2": 'android',
# #     "platform": 'app',
# #     "eventValue.topicId": topicId,
# #     "serverTime": {"$gte": start, "$lt": end},
# #     "eventKey": "startMaster",
# #     "user": {"$exists": True}}))
# # user = [e['user'] for e in eventKeys]
# user = [ObjectId('566c1bd1bf23f0c352e04b31'), ObjectId('5668c528f60c46895efc7a17'), ObjectId('56774aa2c8cb6cff7571bc16'), ObjectId('562852606bc9be4e572cbea1'), ObjectId('56774d5bc8cb6cff7571bd22'), ObjectId('567770c4b9545b4a76537917'), ObjectId('56753df519d6a8275f2566a5'), ObjectId('56753df519d6a8275f2566a5'), ObjectId('56753df519d6a8275f2566a5'), ObjectId('56753df519d6a8275f2566a5'), ObjectId('56753df519d6a8275f2566a5'), ObjectId('5676622cc3620c9b754a1bf3'), ObjectId('567610e2c3620c9b754929e9'), ObjectId('56777ea75bbce84f6ba90d64'), ObjectId('5676bddbb9545b4a76533ac0'), ObjectId('5655a6ea6a40a0a750acd98e'), ObjectId('566d6e221ab55ca00e7dfdb8'), ObjectId('56778331c8cb6cff7571e699'), ObjectId('563ae004ed88f8da05fb5426'), ObjectId('564db19fb77d3b151d72ae2a'), ObjectId('5677881bc3620c9b754b9a0a'), ObjectId('56570475083dfe624f5466db'), ObjectId('567734d9348b65cd75b66fe6'), ObjectId('565a879ff8e493b9187e1651'), ObjectId('567734d9348b65cd75b66fe6'), ObjectId('5674e3a08ef59fc871de9529'), ObjectId('55e8f6d469800542759b41d6'), ObjectId('56778a376051cb1d6bbd75f2'), ObjectId('567780f847155b366b0f16fe'), ObjectId('567780f847155b366b0f16fe'), ObjectId('5677863fd6dad4e67555ac7d'), ObjectId('567780011bf3b7317680dc36'), ObjectId('5677a2ec74a924b4753045e2'), ObjectId('567359c3a938eca9392f847a'), ObjectId('5677ad49484c93ea6a1917ef'), ObjectId('567667c9b9545b4a7652200a'), ObjectId('567667c9b9545b4a7652200a'), ObjectId('55dd80d98872ec8a7b3bf77c'), ObjectId('55dd80d98872ec8a7b3bf78b'), ObjectId('5677b971484c93ea6a191f93'), ObjectId('56482ca152590a431bc28c2c'), ObjectId('56482ca152590a431bc28c2c'), ObjectId('5677c0084fd056e9334f4d76'), ObjectId('5677c0084fd056e9334f4d76'), ObjectId('565c28b5ac50488c5ebf76fc'), ObjectId('5677694e47155b366b0f0892'), ObjectId('5677c6e144529a1e3ed437ee'), ObjectId('5634662961ca11b117d17c0d'), ObjectId('5677c4f8a42253553f2cdea3'), ObjectId('5666b9df7d7436ec02f9f226'), ObjectId('5674e3a08ef59fc871de9529'), ObjectId('5677cb66ecef641f51d49cb5'), ObjectId('566eab171f2192786ba051f2'), ObjectId('56773777b5a5a8a515da22d1'), ObjectId('5674f5fe1dfd6de971924995'), ObjectId('5677ccd8bf57a1e74f1f3381'), ObjectId('5617baf494660c0640245ef7'), ObjectId('5677d0e262079e5c3e07eea1'), ObjectId('5669375eba2f95cf68b5729e'), ObjectId('56584827c887ceb904d396f7'), ObjectId('567568b23ded693c4458824e'), ObjectId('5677d42b7612e68650dbdb03'), ObjectId('56432e0c8f7889fd6e75eb6f'), ObjectId('5677d40d44529a1e3ed44e98'), ObjectId('566e7bcc16914e755d1594e0'), ObjectId('566e7bcc16914e755d1594e0'), ObjectId('5677d3bcc7ad0bdb3d682e2d'), ObjectId('563b2cfaf1dba190054f6e19'), ObjectId('561a0a4aa74ad379699e6c18'), ObjectId('5621c7a097a357780e6a7847'), ObjectId('56767b9c74a924b4752ef659'), ObjectId('5677d8104fd056e9334f6cad'), ObjectId('56768bbcb9545b4a7652824c'), ObjectId('56695b9965ad7165692be464'), ObjectId('56768bbcb9545b4a7652824c'), ObjectId('565c28b5ac50488c5ebf76fc'), ObjectId('5674a0e6dd6c1d37595f54cc'), ObjectId('5677dae0a42253553f2d0683'), ObjectId('5677dd5cf3b2ac323ff4dd11'), ObjectId('565136cbceabbcd42b0fda6d'), ObjectId('564c68fc9a81efc801ad450e'), ObjectId('56768e185bbce84f6ba83c88'), ObjectId('5677de6febcb14c450af3c0d'), ObjectId('5677ddd1ecef641f51d4c01d'), ObjectId('5677ded175f8b8cd40705761'), ObjectId('56768523c3620c9b754a77ff'), ObjectId('56768523c3620c9b754a77ff'), ObjectId('5677d5f29ef5f63d3e2b15e0'), ObjectId('55dd6171315ed84b601d4ddc'), ObjectId('56768bbcb9545b4a7652824c'), ObjectId('566e7bcc16914e755d1594d1'), ObjectId('567249b579ec85911b6276eb'), ObjectId('5667c5106fdc5c623a45da53'), ObjectId('5677df7eb5a5a8a515daa267'), ObjectId('5677df0ca6adf7b453c17801'), ObjectId('56377c33b0f91b3573db8758'), ObjectId('5677d530bf57a1e74f1f41f1'), ObjectId('566ff9bc13de11560893ff36'), ObjectId('567249b579ec85911b6276eb'), ObjectId('566bdf4d8c55cd81798ba37a'), ObjectId('5667c5106fdc5c623a45da53'), ObjectId('5667c5106fdc5c623a45da53'), ObjectId('566aa5190f2897be4d767fc9'), ObjectId('56773283d3a4910c6caf60f9'), ObjectId('56773283d3a4910c6caf60f9'), ObjectId('5677e4d036eae952539c1eb9'), ObjectId('5667c5106fdc5c623a45da53'), ObjectId('56590c10fb98b82d1c248fdc'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('56769d8747155b366b0e74f8'), ObjectId('565304875331e5272ac44f9b'), ObjectId('5677e54fec1330d35311c43c'), ObjectId('5677e5e236eae952539c2295'), ObjectId('56769d8747155b366b0e74f8'), ObjectId('5677e7a54ac24e7354e91546'), ObjectId('56769d1191806b18763fdfc2'), ObjectId('5677e7ca00ab330b40012189'), ObjectId('567653e2eba680d16ae78765'), ObjectId('5677e908b5a5a8a515dabd46'), ObjectId('567668aeb9545b4a7652225f'), ObjectId('5649b4ee30720d683afb03bd'), ObjectId('567687aad6dad4e6755484cb'), ObjectId('56768523c3620c9b754a77ff'), ObjectId('5677e13d4ac24e7354e900a0'), ObjectId('5677e13d4ac24e7354e900a0'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('566577195c4c1c376f07fc70'), ObjectId('567687aad6dad4e6755484cb'), ObjectId('5627842fd0f3bd060a73569e'), ObjectId('5677eae434052a945281b86f'), ObjectId('567687aad6dad4e6755484cb'), ObjectId('566a25e60b208ca86c01efad'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('566a25e60b208ca86c01efad'), ObjectId('565072eac1fb1af5291d95c6'), ObjectId('5605432afc45b51b60f24e33'), ObjectId('566a25e60b208ca86c01efad'), ObjectId('566a25e60b208ca86c01efad'), ObjectId('5677e13d4ac24e7354e900a0'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('566be10b9ac1ee89792208c4'), ObjectId('5645e0120b4dd86d1465009f'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('5677ea384ac24e7354e91e73'), ObjectId('5677e13d4ac24e7354e900a0'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('5610a78fb2ee33af66ec64b3'), ObjectId('5677e13d4ac24e7354e900a0'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('53f4a2bef37732bc6753bf4b'), ObjectId('562c7facd0f3bd060a7ffa68'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('565ef50b090d1c8e695c6ca3'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('5677ee2251785d4223238f8b'), ObjectId('566ffc8fda3c518a0ead78b8'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('566189918e5f76915a6c6156'), ObjectId('56342e6ad4ddfc627d50f9cb'), ObjectId('567687d36bd735b86a1281f7'), ObjectId('567656841bf3b731767f51c1'), ObjectId('56179cddfd0e548a31c9994b'), ObjectId('566189918e5f76915a6c6156'), ObjectId('566189918e5f76915a6c6156'), ObjectId('565ef50b090d1c8e695c6ca3'), ObjectId('566ffc8fda3c518a0ead78b8'), ObjectId('5645c9cc18f3fab058b39e00'), ObjectId('5677f15b34052a945281d69b'), ObjectId('565968ea12f0aa4d5b5ee305'), ObjectId('56618dccaedb94e35a50c58b'), ObjectId('56618dccaedb94e35a50c58b'), ObjectId('56762c3847155b366b0d588a'), ObjectId('566ffc8fda3c518a0ead78b8'), ObjectId('565c3d24ac50488c5ec02be8'), ObjectId('5677f22e34052a945281da46'), ObjectId('5677f399f6142dae3fe882d5'), ObjectId('5677ee2251785d4223238f8b'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('565c28b5ac50488c5ebf76fc'), ObjectId('5655a796be6e5fb536e77927'), ObjectId('564880efc9f594321b7d59a0'), ObjectId('5677f2e775f8b8cd4070b06a'), ObjectId('562afd9575b067c75766e7c3'), ObjectId('56559d226a40a0a750ac6f6e'), ObjectId('560be338b33f6ca064b212cc'), ObjectId('567404095c0e51ea28a62765'), ObjectId('5677f482f3137ced4099eb19'), ObjectId('5677f36c2e7d480c418f73c7'), ObjectId('56655cf67150af5a6fb9e38f'), ObjectId('563f51ab9d102ca9034c720d'), ObjectId('566eab171f2192786ba051f2'), ObjectId('560cf91ff4d9384279f6b7a7'), ObjectId('566eab171f2192786ba051f2'), ObjectId('565868e0b2b8fd644d3fc143'), ObjectId('56778985c3620c9b754b9bd4'), ObjectId('56769fd374a924b4752f6ffb'), ObjectId('56764e60c3620c9b7549e4b7'), ObjectId('566eab171f2192786ba051f2'), ObjectId('5677f6c564079b2a40c46a4c'), ObjectId('566eab171f2192786ba051f2'), ObjectId('560be338b33f6ca064b212cc'), ObjectId('5677eff234052a945281d0e0'), ObjectId('562afd9575b067c75766e7c3'), ObjectId('5676b8b91bf3b73176808b0a'), ObjectId('56555d7b01e1acc63615c63b'), ObjectId('5677ea8234052a945281b6cf'), ObjectId('5676b8b91bf3b73176808b0a'), ObjectId('5662aac88185969e392b88e9'), ObjectId('563f51ab9d102ca9034c720d'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('56753d0f19d6a8275f256426'), ObjectId('5677f4212e7d480c418f7701'), ObjectId('56760303484c93ea6a16d192'), ObjectId('5677ecc54ef5e3cd3f118606'), ObjectId('5651643b5331e5272abd71ce'), ObjectId('5677fe5934052a94528210a0'), ObjectId('56769369c3620c9b754aae94'), ObjectId('56762fc6348b65cd75b49e7b'), ObjectId('5666c70679ff253723435acf'), ObjectId('5666c70679ff253723435acf'), ObjectId('5655a1540d2a40b4504141b9'), ObjectId('5666c70679ff253723435acf'), ObjectId('5666c70679ff253723435acf'), ObjectId('5677f988f6142dae3fe8a2b5'), ObjectId('5666c70679ff253723435acf'), ObjectId('56546912e71e63c55011c3a7'), ObjectId('5677ddb662079e5c3e080ed8'), ObjectId('5677f48d51785d422323a709'), ObjectId('56754c60474ba4634d45792a'), ObjectId('56754c60474ba4634d45792a'), ObjectId('566bbe3438645a1b762400db'), ObjectId('56754c60474ba4634d45792a'), ObjectId('5666c70679ff253723435acf'), ObjectId('564c7e5209e09be52754f1bf'), ObjectId('565a806f66a4443b19b34d11'), ObjectId('567686ea4fd056e9334e0a88'), ObjectId('56769dbbd3a4910c6caeeb3c'), ObjectId('56021844eb8d68a441eac689'), ObjectId('564c7e5209e09be52754f1bf'), ObjectId('567734d9348b65cd75b66fe6'), ObjectId('5677863fd6dad4e67555ac7d'), ObjectId('5678010851785d422323d94d'), ObjectId('56769dbbd3a4910c6caeeb3c'), ObjectId('5677fb45bfeff4ec3f99ccf0'), ObjectId('562b223275b067c757678c53'), ObjectId('5676a1d9d6dad4e67554f4c9'), ObjectId('567643b71bf3b731767f1fa4'), ObjectId('567800324ef5e3cd3f11f12a'), ObjectId('5676a1d9d6dad4e67554f4c9'), ObjectId('5676a1d9d6dad4e67554f4c9'), ObjectId('567801842e7d480c418fbb77'), ObjectId('567800324ef5e3cd3f11f12a'), ObjectId('5676a1d9d6dad4e67554f4c9'), ObjectId('5676a1d9d6dad4e67554f4c9'), ObjectId('564db19fb77d3b151d72ae2a'), ObjectId('5662b81e7a5b9cd539ad7304'), ObjectId('56780174bfeff4ec3f99ee8c'), ObjectId('56768a84b9545b4a76527dd5'), ObjectId('564922109e98a79a3ae96eff'), ObjectId('5677fc68ec1330d353122c1d'), ObjectId('5677f004200626945309a79e'), ObjectId('567801842e7d480c418fbb77'), ObjectId('5672c77e06a9b4726b99e1f9'), ObjectId('565c31b31bd0c4763189faf3'), ObjectId('565a806f66a4443b19b34d11'), ObjectId('565c31b31bd0c4763189faf3'), ObjectId('565c31b31bd0c4763189faf3'), ObjectId('56778399c8cb6cff7571e763'), ObjectId('5677f833d22215b3528593a9'), ObjectId('56486dbc30720d683af89778'), ObjectId('56486dbc30720d683af89778'), ObjectId('567606bf348b65cd75b425e4'), ObjectId('567802a2a6adf7b453c210d0'), ObjectId('5677fa144ac24e7354e9670f'), ObjectId('56778399c8cb6cff7571e763'), ObjectId('564d6740b820cddf0a9c233b'), ObjectId('564aad16dac31106750eefc3'), ObjectId('56693f64a963889c3b32eb2d'), ObjectId('56769862c3620c9b754ac331'), ObjectId('5659c81a2718062f1c20d81b'), ObjectId('56769862c3620c9b754ac331'), ObjectId('567668d15bbce84f6ba7e0be'), ObjectId('5676958051785d4223225d92'), ObjectId('56748369dd6c1d37595f4917'), ObjectId('567632a447155b366b0d6750'), ObjectId('561e3efefa75c03b2f93be2f'), ObjectId('5676958051785d4223225d92'), ObjectId('5676958051785d4223225d92'), ObjectId('5676958051785d4223225d92'), ObjectId('55f42044b51e613c015f644b'), ObjectId('56780a45d22215b35285e1b8'), ObjectId('5642d5b10d1a081b348f0fae'), ObjectId('5642d5b10d1a081b348f0fae'), ObjectId('55f42044b51e613c015f644b'), ObjectId('567811fe51785d42232409ad'), ObjectId('567811fc20062694530a2c22'), ObjectId('56753d94aa6438e14db96c23'), ObjectId('566a542b8358ab626c67046a'), ObjectId('56780fcb51785d42232405e2'), ObjectId('567810b44fd056e933503e24'), ObjectId('5642d5b10d1a081b348f0fae'), ObjectId('564484f735676147147f3777'), ObjectId('564484f735676147147f3777'), ObjectId('5678192bb5a5a8a515db4f5a'), ObjectId('565c5655abec87af5e0ef85b'), ObjectId('564c664e9a81efc801ad2032'), ObjectId('56781ecd51785d42232416e9'), ObjectId('564c664e9a81efc801ad2032'), ObjectId('56781ecd51785d42232416e9'), ObjectId('566196848e5f76915a6cd46f'), ObjectId('566fef810ce26a410d704b75'), ObjectId('5677d4fac7ad0bdb3d6830d0'), ObjectId('5678247864079b2a40c4ec18'), ObjectId('5678247864079b2a40c4ec18'), ObjectId('56781ecd51785d42232416e9'), ObjectId('5678267ab5a5a8a515db5462'), ObjectId('5676ba5aeba680d16ae89b72'), ObjectId('566ceafea067698913bcc003'), ObjectId('566ceafea067698913bcc003'), ObjectId('566ceafea067698913bcc003'), ObjectId('566ceafea067698913bcc003'), ObjectId('56780baf75f8b8cd4071296f'), ObjectId('565316f3c1fb1af529299687'), ObjectId('56189583d6482fe35afb2ae9'), ObjectId('5676ab3774a924b4752f9e6b'), ObjectId('5676ab3774a924b4752f9e6b'), ObjectId('56787d6cf6142dae3fe926ae'), ObjectId('5676a01091806b18763febec'), ObjectId('5674f2fbdd6c1d37595fe8ed'), ObjectId('5678247864079b2a40c4ec18'), ObjectId('5674f2fbdd6c1d37595fe8ed'), ObjectId('5678247864079b2a40c4ec18')]
# # print user
#
# keys = list(events.find({
#     "platform2": 'android',
#     "platform": 'app',
#     # "eventValue.topicId": topicId,
#     "serverTime": {"$gte": start, "$lt": end},
#     "user": ObjectId('5676622cc3620c9b754a1bf3')},
#         {'eventKey': 1, "_id": 0}))
#
# keys = [e['eventKey'] for e in keys]
# print keys

# def h5(start, end, platforms):
#     pipeline = [
#         {
#             "$match": {
#                 "eventKey": "enterMobileSite",
#                 "platform": "landing",
#                 "platform2": {"$in": platforms},
#                 "serverTime": {"$gte": start, "$lt": end}
#             }
#         },
#         {
#             "$group": {
#                 "_id": "$device",
#                 "pv": {"$sum": 1}
#             }
#         },
#         {
#             "$group": {
#                 "_id": None,
#                 "uv": {"$sum": 1},
#                 "pv": {"$sum": "$pv"}
#             }
#         }
#     ]
#     res = list(events.aggregate(pipeline))
#     return res[0]

#
# START_DATE_UTC = datetime.datetime(2015, 12, 19) - datetime.timedelta(hours=8)
# END_DATE_UTC = datetime.datetime(2015, 12, 20) - datetime.timedelta(hours=8)
# h5_android = h5(START_DATE_UTC, END_DATE_UTC, ['android'])
# h5_ios = h5(START_DATE_UTC, END_DATE_UTC, ['iOS'])
# print START_DATE_UTC.date()
# print('android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv'])
# print('iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv'])
#
# START_DATE_UTC = datetime.datetime(2015, 12, 20) - datetime.timedelta(hours=8)
# END_DATE_UTC = datetime.datetime(2015, 12, 27) - datetime.timedelta(hours=8)
# h5_android = h5(START_DATE_UTC, END_DATE_UTC, ['android'])
# h5_ios = h5(START_DATE_UTC, END_DATE_UTC, ['iOS'])
# print START_DATE_UTC.date()
# print('android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv'])
# print('iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv'])
#
# START_DATE_UTC = datetime.datetime(2015, 12, 27) - datetime.timedelta(hours=8)
# END_DATE_UTC = datetime.datetime(2016, 1, 3) - datetime.timedelta(hours=8)
# h5_android = h5(START_DATE_UTC, END_DATE_UTC, ['android'])
# h5_ios = h5(START_DATE_UTC, END_DATE_UTC, ['iOS'])
# print START_DATE_UTC.date()
# print('android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv'])
# print('iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv'])
#
# START_DATE_UTC = datetime.datetime(2016, 1, 3) - datetime.timedelta(hours=8)
# END_DATE_UTC = datetime.datetime(2016, 1, 10) - datetime.timedelta(hours=8)
# h5_android = h5(START_DATE_UTC, END_DATE_UTC, ['android'])
# h5_ios = h5(START_DATE_UTC, END_DATE_UTC, ['iOS'])
# print START_DATE_UTC.date()
# print('android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv'])
# print('iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv'])


# START_DATE_UTC = datetime.datetime(2016, 1, 10) - datetime.timedelta(hours=8)
# END_DATE_UTC = datetime.datetime(2016, 1, 17) - datetime.timedelta(hours=8)
# h5_android = h5(START_DATE_UTC, END_DATE_UTC, ['android'])
# h5_ios = h5(START_DATE_UTC, END_DATE_UTC, ['iOS'])
# print START_DATE_UTC.date()
# print 'android', 'uv:', h5_android['uv'], 'pv:', h5_android['pv']
# print 'iOS', 'uv:', h5_ios['uv'], 'pv:', h5_ios['pv']
#
# e = time.time()
# print 'time: ', e-s, 's'

# ('android', 'uv:', 189, 'pv:', 205)
# ('iOS', 'uv:', 7, 'pv:', 7)

# start = datetime.datetime(2015, 12, 1, 16)
# end = datetime.datetime(2016, 1, 16, 16)
#
#
# pipeline = [
#     {
#         "$match": {
#             "platform": "android",
#             "activateDate": {"$gte": start, "$lt": end}
#         }
#     },
#     {
#         "$project": {
#             "activateDate": {"$add": ["$activateDate", 8*60*60000]}
#         }
#     },
#     {
#         "$group": {
#             "_id": {"$dayOfYear": "$activateDate"},
#             "count": {"$sum": 1}
#         }
#     },
#     {
#         "$sort": {
#         "_id": -1
#     }
#     }
# ]
#
# res = list(deviceAttr.aggregate(pipeline, allowDiskUse=True))
# print res
#
# [
#  {u'count': 19066, u'_id': 16},
#  {u'count': 11637, u'_id': 15},
#  {u'count': 6511, u'_id': 14},
#  {u'count': 8750, u'_id': 13},
#  {u'count': 10011, u'_id': 12},
#  {u'count': 9091, u'_id': 11},
#  {u'count': 20725, u'_id': 10},
#  {u'count': 20471, u'_id': 9},
#  {u'count': 14279, u'_id': 8},
#  {u'count': 7043, u'_id': 7},
#  {u'count': 3199, u'_id': 6},
#  {u'count': 4177, u'_id': 5},
#  {u'count': 10894, u'_id': 4},
#  {u'count': 19705, u'_id': 3},
#  {u'count': 22563, u'_id': 2},
#  {u'count': 26315, u'_id': 1},
# {u'count': 9324, u'_id': 365},
#  {u'count': 6015, u'_id': 364},
#  {u'count': 5211, u'_id': 363},
#  {u'count': 5345, u'_id': 362},
#  {u'count': 11443, u'_id': 361},
#  {u'count': 12429, u'_id': 360},
#  {u'count': 6409, u'_id': 359},
#  {u'count': 5210, u'_id': 358},
#  {u'count': 6577, u'_id': 357},
#  {u'count': 5936, u'_id': 356},
#  {u'count': 5632, u'_id': 355},
#  {u'count': 7093, u'_id': 354},
#  {u'count': 5086, u'_id': 353},
#  {u'count': 2365, u'_id': 352},
#  {u'count': 2100, u'_id': 351},
#  {u'count': 2094, u'_id': 350},
#  {u'count': 2058, u'_id': 349},
#  {u'count': 2159, u'_id': 348},
#  {u'count': 3366, u'_id': 347},
#  {u'count': 3889, u'_id': 346},
#  {u'count': 2625, u'_id': 345},
#  {u'count': 2424, u'_id': 344},
#  {u'count': 2514, u'_id': 343},
#  {u'count': 2700, u'_id': 342},
#  {u'count': 2624, u'_id': 341},
#  {u'count': 4480, u'_id': 340},
#  {u'count': 5982, u'_id': 339},
#  {u'count': 4034, u'_id': 338},
#  {u'count': 5261, u'_id': 337},
#  {u'count': 7353, u'_id': 336}, ]



