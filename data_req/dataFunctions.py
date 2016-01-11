# _*_ coding:utf-8 _*_
from pymongo import MongoClient
import datetime
import time


db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
cache = MongoClient('10.8.8.111:27017')['cache']
deviceAttr = cache['deviceAttr']
userAttr = cache['userAttr']
eventFlow = cache['eventFlow']
users = db['users']
events = db['events']


def calc_user_device(start, end, platforms):
    # STEP 1 get all the new users in given time period
    new_user_q = users.find({"type": {"$ne": "batch"}, "registTime": {"$gte": start, "$lt": end}}, {"_id": 1})
    new_user_batch_q = users.find({"type": "batch", "activateDate": {"$gte": start, "$lt": end}}, {"_id": 1})
    user_group = [doc["_id"] for doc in new_user_q] + [doc["_id"] for doc in new_user_batch_q]
    # STEP 2 get all the devices that user has used
    user_device = {}
    pipeline = [
        {"$unwind": "$users"},
        {"$match": {"users": {"$in": user_group}, "platform": {"$in": platforms}}},
        {"$group": {"_id": "$users", "devices": {"$addToSet": "$device"}}}
    ]
    temp_device = list(deviceAttr.aggregate(pipeline))
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


def collect_event(start, end, users_dict, platforms):
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
    return x + y


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


def new_user_count(start, end, platform):
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
    return users.find(query1).count() + users.find(query2).count()


def mobile_new_unregistered_count(start, end, platform):
    query = {
        "users.0": {"$exists": False},
        "activateDate": {"$gte": start, "$lt": end},
        "platform": platform
    }
    return deviceAttr.find(query).count()
