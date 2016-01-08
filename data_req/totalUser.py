# _*_ coding:utf-8 _*_
from pymongo import MongoClient
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
cache = MongoClient('10.8.8.111:27017')['cache']
deviceAttr = cache['deviceAttr']
userAttr = cache['userAttr']
eventFlow = cache['eventFlow']
users = db['users']
events = db['events']

START_DATE = datetime.datetime(2010, 1, 1)
END_DATE = datetime.datetime(2016, 1, 4)


def new_user_count(start, end, platforms):
    query1 = {
        "from": {"$in": platforms},
        "type": {"$ne": "batch"},
        "registTime": {"$gte": start, "$lt": end}
    }
    query2 = {
        "from": {"$in": platforms},
        "type": "batch",
        "activateDate": {"$gte": start, "$lt": end}
    }
    return users.find(query1).count() + users.find(query2).count()


def teacher_count(start, end):
    query = {
        "role": "teacher",
        "registTime": {"$gte": start, "$lt": end}
    }
    return users.find(query).count()


def mobile_new_unregistered_count(start, end):
    query = {
        "users": [],
        "activateDate": {"$gte": start, "$lt": end},
        "platform": {"$in": ['android', 'ios']}
    }
    return deviceAttr.find(query).count()


def new_user_by_attr(start, end):
    return userAttr.find(
            {
                "activateDate": {"$gte": start, "$lt": end},
                # "recentPCSession": {"$ne": None}
            }
    ).count()

registered_user = new_user_count(START_DATE, END_DATE, ['pc', 'android', 'ios'])
teacher = teacher_count(START_DATE, END_DATE)
mobile_user = new_user_count(START_DATE, END_DATE, ['android', 'ios'])
mobile_unregistered = mobile_new_unregistered_count(START_DATE, END_DATE)

pc_user = new_user_count(START_DATE, END_DATE, ['pc'])
# android_user = new_user_count(START_DATE, END_DATE, ['android'])
# ios_user = new_user_count(START_DATE, END_DATE, ['ios'])

print "总用户数: ", registered_user + mobile_unregistered
print "总教师用户数: ", teacher
print "移动端用户数: ", mobile_user + mobile_unregistered

print "pc端总用户数: " , pc_user
# print 'pc: ', new_user_by_attr(START_DATE, END_DATE)
# print "android总用户数: "
# print "ios端总用户数: "
