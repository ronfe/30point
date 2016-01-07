# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
events = db['events']
topics = db['topics']
problemsets = db['problemsets']

START_DATE = datetime.datetime(2015, 12, 21)
END_DATE = datetime.datetime(2015, 12, 28)

# calculate weekly top 10 topics
def weeklyTopicsEnterTop10(startDate, endDate):
    pipeLine = [
        {"$match": {
            "eventKey": "enterTopic",
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            }
        }},
        {"$group": {
            "_id": "$eventValue.topicId",
            "count": {"$sum": 1}
        }},
        {"$sort": {
            "count": DESCENDING
        }}
    ]

    x = list(events.aggregate(pipeLine))[:10]
    return [each["_id"] for each in x]

# top 10 topics list
weeklyEnterTopicsTopTenList = weeklyTopicsEnterTop10(START_DATE, END_DATE)

def uvOfClickExpVideo(startDate, endDate, topic, event, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": event,
            "eventValue.topicId": topic,
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))


pc = "PC"
ios = "iOS"
android = "android"

for topic in weeklyEnterTopicsTopTenList:
    print("----------------------------------")
    topicName = topics.find_one({"_id": ObjectId(topic)})['name']
    print("###%s")%topicName

    # pc
    print("PC 用户点击视频讲解按钮")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "clickExpVideo", pc))
    print("PC 选择错因")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "reasonOfMistake", pc))
    # ios
    print("iOS 用户点击视频讲解按钮")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "clickExpVideo", ios))
    print("iOS 选择错因")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "reasonOfMistake", ios))
    # android
    print("android 用户点击视频讲解按钮")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "clickExpVideo", android))
    print("android 选择错因")
    print(uvOfClickExpVideo(START_DATE, END_DATE, topic, "reasonOfMistake", android))

