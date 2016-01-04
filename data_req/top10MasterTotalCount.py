# -*- coding: utf-8 -*-
# 计算周排名前10练习模块
from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
events = db['events']
topics = db['topics']
problemsets = db['problemsets']

START_DATE = datetime.datetime(2015, 12, 20)
END_DATE = datetime.datetime(2015, 12, 26)

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

def uvOfWeeklyTop10Masters(startDate, endDate, top10Topics):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "startMaster",
            "eventValue.topicId": {"$in": top10Topics}
        }},
        {"$group": {
            "_id": None,
            "user": {"$addToSet": "$user"}
        }}
    ]
    return len(list(events.aggregate(pipeLine))[0]['user'])

print("练习进入总量:")
print(uvOfWeeklyTop10Masters(START_DATE, END_DATE, weeklyEnterTopicsTopTenList))

# 练习模块真实进入量
# 练习第一专题第一题作答总量

def changeObjectId(changeList):
    returnList = []
    for doc in changeList:
        returnList.append(ObjectId(doc))
    return returnList

# catch top 10 topics first problemsets1 problemsets2
def getTop10TopicsFirstAndSecondProblemSet(startDate, endDate, top10Topics):
    topTenTopics = changeObjectId(top10Topics)
    pipeLine = [
        {"$match": {
            "_id": {"$in": topTenTopics}
        }},
        {"$project": {
            "_id": "$_id",
            "problemSets": "$master.problemSets"
        }}
    ]
    problemSetsList = list(topics.aggregate(pipeLine))
    problemFirstSecondDict = {}
    firtProblem = []
    secondProblem = []
    for problem in problemSetsList:
        firtProblem.extend(problem['problemSets'][:1])
        secondProblem.extend(problem['problemSets'][1:2])
    problemFirstSecondDict['firstProblemSets'] = firtProblem
    problemFirstSecondDict['secondProblemSets'] = secondProblem
    return problemFirstSecondDict

problemSetsFirstAndSecond = getTop10TopicsFirstAndSecondProblemSet(START_DATE, END_DATE, weeklyEnterTopicsTopTenList)

# 获取第一个problemset的第一道/二道题目id
def getFirstProblemSetsFirstAndSecondProblem(problemSetsId):
    pipeLine = [
        {"$match": {
            "_id": {"$in": problemSetsId}
        }},
        {"$project": {
            "_id": 1,
            "problems.practice": 1
        }}
    ]
    problemSetsList = list(problemsets.aggregate(pipeLine))
    firstAndSecondProblem = {}
    firstProblem = []
    secondProblem = []
    for doc in problemSetsList:
        firstProblem.append(doc['problems']['practice'][0]['_id'])
        secondProblem.append(doc['problems']['practice'][1]['_id'])
    firstAndSecondProblem['firstProblem'] = firstProblem
    firstAndSecondProblem['secondProblem'] = secondProblem
    return firstAndSecondProblem

firstProblemSetsFirstProblemList = getFirstProblemSetsFirstAndSecondProblem(problemSetsFirstAndSecond['firstProblemSets'])

def removeObjectId(changeList):
    returnList = []
    for doc in changeList:
        returnList.append(str(doc))
    return returnList

def uvOfAnswerFirstProblemSetFirstProblem(startDate, endDate, inputProblemList):
    problemList = removeObjectId(inputProblemList)
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "answerProblem",
            "eventValue.problemId": {"$in": problemList}
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))

problemList = firstProblemSetsFirstProblemList['firstProblem']
print("练习模块真实进入量 --- 练习第一专题第一题作答总量:")
uvOfRealIntoMaster = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList)
print(uvOfRealIntoMaster)

# 练习模块认真完成量 练习第二专题第一题作答总量
secondProblemSetsFirstProblemList = getFirstProblemSetsFirstAndSecondProblem(problemSetsFirstAndSecond['secondProblemSets'])
print("练习模块认真完成量 --- 练习第二专题第一题作答总量:")
problemList = secondProblemSetsFirstProblemList['firstProblem']
uvOfPayAttetionUser = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList)
print(uvOfPayAttetionUser)

# 练习模块真实总完成率 完成量(completeMaster->topics)/真正进入量
def top10TopicsCompleteMaster(startDate, endDate, topTenTopics):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "completeMaster",
            "eventValue.topicId": {"$in": topTenTopics}
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))

uvOfCompleteMaster = top10TopicsCompleteMaster(START_DATE, END_DATE, weeklyEnterTopicsTopTenList)

def perNum(molecule, denominator):
    if molecule == 0 or denominator == 0:
        return str("denominator cannot equal zero.")
    m = float(molecule)
    d = float(denominator)
    num = ("%.2f")%(m/d*100)
    return num

print("练习模块真实总完成率 --- 完成量/真正进入量:")
print(perNum(uvOfCompleteMaster, uvOfRealIntoMaster))

# 认真用户练习模块完成率	练习模块设计参考（是否题目过多过难等）	 完成量/认真完成量
print("认真用户练习模块完成率 --- 完成量/认真完成量:")
print(perNum(uvOfCompleteMaster, uvOfPayAttetionUser))

# 挑战失败率	挑战题设计参考 是否过难	挑战失败量/挑战进入量
def intoChallage(startDate, endDate, topTenTopics):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "startChallenge",
            "eventValue.topicId": {"$in": topTenTopics}
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))

def failInChallage(startDate, endDate, topTenTopics):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "challengeFailure",
            "eventValue.topicId": {"$in": topTenTopics}
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return list(events.aggregate(pipeLine))

def successChallage(startDate, endDate, topTenTopics):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "challengeSuccess",
            "eventValue.topicId": {"$in": topTenTopics}
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return list(events.aggregate(pipeLine))


uvOfIntoChallage = intoChallage(START_DATE, END_DATE, weeklyEnterTopicsTopTenList)
uvOfFailChallage = failInChallage(START_DATE, END_DATE, weeklyEnterTopicsTopTenList)
print("挑战失败率	 --- 挑战失败量/挑战进入量:")
print(perNum(len(uvOfFailChallage), uvOfIntoChallage))

# 挑战完成率	挑战模块吸引用户程度	挑战成功+失败量/挑战进入量

failChallageList = []
for doc in uvOfFailChallage:
    failChallageList.append(doc['_id'])

successChallageList = []
uvOfSuccessChallage = successChallage(START_DATE, END_DATE, weeklyEnterTopicsTopTenList)
for doc in uvOfSuccessChallage:
    successChallageList.append(doc['_id'])

totalFailAndSuccessChallage = list(set.intersection(set(failChallageList), set(successChallageList)))

print("挑战完成率	 --- 挑战成功+失败量/挑战进入量")
print(perNum(len(totalFailAndSuccessChallage), uvOfIntoChallage))
