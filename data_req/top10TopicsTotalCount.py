# -*- coding: utf-8 -*-
# 计算周排名前10知识点情况

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
events = db['events']
topics = db['topics']

START_DATE = datetime.datetime(2015, 12, 21)
END_DATE = datetime.datetime(2015, 12, 28)

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

weeklyEnterTopicsTopTenList = weeklyTopicsEnterTop10(START_DATE, END_DATE)

# rate of startLearning/completeLearning in weekly top 10 topics
# pass start/end date as timerange
# pass top ten topics of this week
# pass eventKey
def uvOfStartOrCompleteLearning(startDate, endDate, weeklyTopTenTopics, event):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventValue.topicId": {"$in": weeklyTopTenTopics},
            "eventKey": event
        }},
        {"$group": {
            "_id": "$device"
        }}
    ]

    return len(list(events.aggregate(pipeLine)))

startLearningUv = uvOfStartOrCompleteLearning(START_DATE, END_DATE, weeklyEnterTopicsTopTenList, "startLearning")
completeLearningUv = uvOfStartOrCompleteLearning(START_DATE, END_DATE, weeklyEnterTopicsTopTenList, "completeLearning")

def perNum(molecule, denominator):
    if molecule == 0 or denominator == 0:
        return str("denominator cannot equal zero.")
    m = float(molecule)
    d = float(denominator)
    num = ("%.2f")%(m/d*100)
    return num

print("学习模块完成率:")
print(perNum(completeLearningUv, startLearningUv))


def changeObjectId(changeList):
    returnList = []
    for doc in changeList:
        returnList.append(ObjectId(doc))
    return returnList

def removeObjectId(changeList):
    returnList = []
    for doc in changeList:
        returnList.append(doc)
    return returnList

def weeklyTopTenVideoId(weeklyEnterTopicsTopTenList):
    topTenTopicsList = changeObjectId(weeklyEnterTopicsTopTenList)
    pipeLine = [
        {"$match": {
            "_id": {"$in": topTenTopicsList}
        }},
        {"$group": {
            "_id": "$learning.hyperVideos"
        }}
    ]

    topTenVideosList = []
    topTenVideos = list(topics.aggregate(pipeLine))
    for doc in topTenVideos:
        topTenVideosList.extend(doc['_id'])

    returnList = []
    for doc in topTenVideosList:
        returnList.append(str(doc))
    return returnList

weeklyTopTenVideoIdList = weeklyTopTenVideoId(weeklyEnterTopicsTopTenList)

def startOrfinishVideo(startDate, endDate, weeklyTopTenVideoId, event):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventValue.videoId": {"$in": weeklyTopTenVideoId},
            "eventKey": event
        }},
        {"$group": {
            "_id": "$device"
        }}
    ]

    return len(list(events.aggregate(pipeLine)))


print("视频总观看量:")
print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "startVideo"))
print("视频完成总量:")
print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "finishVideo"))

# print("学习模块完成时间分析")
#
# def findUsersWhoCompleteLearning(startDate, endDate, topicId):
#     pipeLine = [
#         {"$match": {
#             "serverTime": {
#                 "$gte": startDate,
#                 "$lt": endDate
#             },
#             "eventValue.topicId": topicId
#         }},
#         {"$project": {
#             "_id": "$_id",
#             "user": {
#                 "user": "$user",
#                 "completeTime": "$eventTime"
#             }
#         }}
#     ]
#     usersAndCompleteTime = list(events.aggregate(pipeLine))[0]['user']
#     print(usersAndCompleteTime[:10])
#     return usersAndCompleteTime
#
#
# # def pickUsers(usersAndCompleteTime):
# #     pipeLine = [
# #
# #     ]
#
#
# def findUsersWhoStartLearning(startDate, endDate, topicId):
#     return
#
# for topic in weeklyEnterTopicsTopTenList:
#     print topic
#     usersAndCompleteTime = findUsersWhoCompleteLearning(START_DATE, END_DATE, topic)

