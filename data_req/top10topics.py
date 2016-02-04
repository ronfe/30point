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
print weeklyEnterTopicsTopTenList


# rate of startLearning/completeLearning in weekly top 10 topics
# pass start/end date as timerange
# pass top ten topics of this week
# pass eventKey
# pass platform
def uvOfStartOrCompleteLearning(startDate, endDate, weeklyTopTenTopics, event, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventValue.topicId": {"$in": weeklyTopTenTopics},
            "eventKey": event,
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))


def perNum(molecule, denominator):
    if molecule == 0 or denominator == 0:
        return str("比率不成立")
    m = float(molecule)
    d = float(denominator)
    num = ("%.2f")%(m/d*100)
    return num


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
    topic_id = ObjectId(weeklyEnterTopicsTopTenList[0])
    unit_topic = topics.find_one({"_id": topic_id})

    unit_hv = unit_topic['learning']['hyperVideos']
    hv_id = [str(each) for each in unit_hv]

    return hv_id

    # topTenTopicsList = changeObjectId(weeklyEnterTopicsTopTenList)
    # pipeLine = [
    #     {"$match": {
    #         "_id": {"$in": topTenTopicsList}
    #     }},
    #     {"$group": {
    #         "_id": "$learning.hyperVideos"
    #     }}
    # ]
    #
    # topTenVideosList = []
    # topTenVideos = list(topics.aggregate(pipeLine))
    # for doc in topTenVideos:
    #     topTenVideosList.extend(doc['_id'])
    #
    # returnList = []
    # for doc in topTenVideosList:
    #     returnList.append(str(doc))
    # return returnList


def startOrfinishVideo(startDate, endDate, weeklyTopTenVideoId, event, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventValue.videoId": {"$in": weeklyTopTenVideoId},
            "eventKey": event,
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]

    return len(list(events.aggregate(pipeLine)))

for topic in weeklyEnterTopicsTopTenList:
    oneTopic = [topic]
    print("----------------------------------")
    topicName = topics.find_one({"_id": ObjectId(topic)})['name']
    print("###%s")%topicName
    # PC
    startLearningUvPc = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "startLearning", "PC")
    completeLearningUvPc = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "completeLearning", "PC")
    # iOS
    startLearningUvIos = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "startLearning", "iOS")
    completeLearningUvIos = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "completeLearning", "iOS")
    # android
    startLearningUvAndroid = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "startLearning", "android")
    completeLearningUvAndroid = uvOfStartOrCompleteLearning(START_DATE, END_DATE, oneTopic, "completeLearning", "android")

    # pc
    print("PC 学习模块完成率:")
    print(perNum(completeLearningUvPc, startLearningUvPc))
    # iOS
    print("iOS 学习模块完成率:")
    print(perNum(completeLearningUvIos, startLearningUvIos))
    # android
    print("android 学习模块完成率:")
    print(perNum(completeLearningUvAndroid, startLearningUvAndroid))

    weeklyTopTenVideoIdList = weeklyTopTenVideoId(oneTopic)
    # PC
    print("PC 视频总观看量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "startVideo", "PC"))
    # TODO: after 3.0 only change PC's finishVideo to startEmpower, remember change it 'finishVideo' back.
    print("PC 视频完成总量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "startEmpower", "PC"))

    # iOS
    print("iOS 视频总观看量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "startVideo", "iOS"))
    print("iOS 视频完成总量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "finishVideo", "iOS"))

    # android
    print("android 视频总观看量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "startVideo", "android"))
    print("android 视频完成总量:")
    print(startOrfinishVideo(START_DATE, END_DATE, weeklyTopTenVideoIdList, "finishVideo", "android"))
    print("\n----------------------------------\n")
