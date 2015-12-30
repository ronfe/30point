# _*_ coding:utf-8 _*_

from pymongo import MongoClient
import datetime
import random

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
cache = MongoClient('10.8.8.111:27017')['cache']
device_attr = cache['deviceAttr']
users = db['users']

START = datetime.datetime(2015,12,23)
END = datetime.datetime(2015,12,24)

def calc_user_device(start, end, platforms):
    # STEP 1 get all the new users in given time period
    new_user_q = users.find({"type": {"$ne": "batch"}, "registTime": {"$gte": start, "$lt": end}}, {"_id": 1})
    new_user_batch_q = users.find({"type":"batch", "activateDate": {"$gte": start, "$lt": end}}, {"_id": 1})
    user_group = [doc["_id"] for doc in new_user_q] + [doc["_id"] for doc in new_user_batch_q]

    # STEP 2 get all the devices that user has used
    user_device = {}
    pipeline = [
        {"$unwind": "$users"},
        {"$match": {"users": {"$in": user_group}, "platform": {"$in": platforms}}},
        {"$group": {"_id": "$users", "devices": {"$addToSet": "$device"}}}
    ]
    temp_device = list(device_attr.aggregate(pipeline))
    for each in temp_device:
        user_device[each['_id']] = each['devices']

    output = {
        "hasUsers": {},
        "notUsers": []
    }
    for k, v in user_device.iteritems():
        output['hasUsers'][k] = v

    # STEP 3 get all the no user devices
    no_user_devices = device_attr.find({"platform": {"$in": platforms}, "users.0": {"$exists": False}, "activateDate": {"$gte": start, "$lt": end}}, {"device": 1})
    output['notUsers'] = [each['device'] for each in no_user_devices]

    return output



x = calc_user_device(START, END, ['android'])