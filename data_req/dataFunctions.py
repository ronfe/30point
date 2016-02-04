# _*_ coding:utf-8 _*_
from __future__ import print_function
from pymongo import MongoClient, DESCENDING
import datetime
import time
import calendar
import math

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
cache = MongoClient('10.8.8.111:27017')['cache']
deviceAttr = cache['deviceAttr']
userAttr = cache['userAttr']
eventFlow = cache['eventFlow']
users = db['users']
events = db['events']
users25 = cache['users25']
topics = db['topics']

ONLINE_30 = datetime.datetime(2015, 12, 18, 16)


def calc_user_device(start, end, platforms):
    # STEP 1 get all the new users in given time period
    if start < ONLINE_30:
        new_user_q = list(users.find({"type": {"$ne": "batch"}, "from": {"$in": platforms}, "registTime": {"$gte": ONLINE_30, "$lt": end}}, {"_id": 1})) + \
                     list(users25.find({"type": {"$ne": "batch"}, "from": {"$in": platforms}, "registTime": {"$gte": start, "$lt": ONLINE_30}}, {"_id": 1}))
        new_user_batch_q = list(users.find({"type": "batch", "from": {"$in": platforms}, "activateDate": {"$gte": ONLINE_30, "$lt": end}}, {"_id": 1})) + \
                           list(users25.find({"type": "batch", "from": {"$in": platforms}, "activateDate": {"$gte": start, "$lt": ONLINE_30}}, {"_id": 1}))
    else:
        new_user_q = users.find({"type": {"$ne": "batch"}, "from": {"$in": platforms}, "registTime": {"$gte": start, "$lt": end}}, {"_id": 1})
        new_user_batch_q = users.find({"type": "batch", "from": {"$in": platforms}, "activateDate": {"$gte": start, "$lt": end}}, {"_id": 1})

    user_group = [doc["_id"] for doc in new_user_q] + [doc["_id"] for doc in new_user_batch_q]
    # STEP 2 get all the devices that user has used
    user_device = {}
    pipeline = [
        {"$unwind": "$users"},
        {"$match": {"users": {"$in": user_group}, "platform": {"$in": platforms}}},
        {"$group": {"_id": "$users", "devices": {"$addToSet": "$device"}}}
    ]
    temp_device = list(deviceAttr.aggregate(pipeline, allowDiskUse=True))
    for each in temp_device:
        user_device[each['_id']] = each['devices']
    output = {
        "hasUsers": {},
        "notUsers": []
    }
    for k, v in user_device.iteritems():
        output['hasUsers'][k] = v

    # STEP 3 get all the no user devices
    no_user_devices = deviceAttr.find({"platform": {"$in": platforms}, "users.0": {"$exists": False}, "activateDate": {"$gte": start, "$lt": end}}, {"device": 1})
    output['notUsers'] = [each['device'] for each in no_user_devices]

    return output
# d = calc_user_device(datetime.datetime(2016, 1, 13, 16), datetime.datetime(2016, 1, 14, 16), ['android', ])
# print(len(d['hasUsers']))
# print(len(d['notUsers']))
# ff = open('devices14.txt', 'w')
# dd = sum(d['hasUsers'].values(), [])
#
# ddd = d['notUsers']
# for m in dd:
#     print(m, file=ff)
# for m in ddd:
#     print(m, file=ff)
# ff.close()
#


def collect_event(start, end, users_dict, platforms):
    if not platforms:
        platforms = ['pc', 'android', 'ios']
    device_list = users_dict['notUsers']
    user_device_list = users_dict['hasUsers']

    pipeline = [
        {
            "$match": {
                "device": {"$in": device_list},
                "startTime": {"$gte": start, "$lt": end},
                "platform": {"$in": platforms}
            }
        },
        {
            "$group": {
                "_id": "$device",
                "eventFlows": {"$push": "$eventFlow"}
            }
        }
    ]
    xx = list(eventFlow.aggregate(pipeline, allowDiskUse=True))
    x = []
    for each in xx:
        x.append(sum(each["eventFlows"], []))

    devices = list(set(sum(user_device_list.values(), [])))

    pipeline2 = [
        {
            "$match": {
                "startTime": {"$gte": start, "$lt": end},
                "platform": {"$in": platforms},
                "device": {"$in": devices}
            }
        },
        {
            "$sort": {
                "startTime": 1
            }
        },
        {
            "$group": {
                "_id": "$device",
                "userFlows": {"$push": {"user": "$user", "eventFlow": "$eventFlow"}}
            }
        }
    ]
    yyy = list(eventFlow.aggregate(pipeline2, allowDiskUse=True))
    yy = {}
    for device in yyy:
        yy.update({device["_id"]: device["userFlows"]})
    y = []
    for user in user_device_list:
        user_event_flow = []
        for device in user_device_list[user]:
            if device in yy:
                user_flows = yy[device]
                ind_user = [i for i, flow in enumerate(user_flows) if "user" in flow and flow['user'] == user]
                ind_null = [i for i, flow in enumerate(user_flows) if "user" not in flow]
                ind = ind_user[:]
                for i in ind_user:
                    j = i
                    while (j-1) in ind_null:
                        ind.append(j-1)
                        j -= 1
                user_event_flow += sum([flow['eventFlow'] for i, flow in enumerate(user_flows) if i in ind], [])
        y.append(user_event_flow)
    return y + x


def pv_uv_count(event_flow, event_key):
    pv_uv = {}
    pv_counter = 0
    uv_counter = 0
    for oneUserFlow in event_flow:
        has_this_key = False
        for event in oneUserFlow:
            if event == event_key:
                pv_counter += 1
                has_this_key = True
        if has_this_key:
            uv_counter += 1
    pv_uv['pv'] = pv_counter
    pv_uv['uv'] = uv_counter
    return pv_uv

