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

# configure list of topics that you need spec
listOfTopic = ["平方根","估算与比较大小","符号语言","整体代入","等式的性质","同底数幂的乘法","十字相乘法","分式的概念","负数指数幂","二次根式的混合运算"]

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

def returnTopicId(topicName):
    pipeLine = [
        {"$match": {
            "name": {"$in": topicName}
        }},
        {"$project": {
            "_id": 1
        }}
    ]
    return list(topics.aggregate(pipeLine))

def specTopics(topicNameList):
    idList = []
    topicsIdList = returnTopicId(topicNameList)

    for doc in topicsIdList:
        idList.append(str(doc['_id']))
    return idList

weeklyEnterTopicsTopTenList = specTopics(listOfTopic)

def uvOfWeeklyTop10Masters(startDate, endDate, top10Topics, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "startMaster",
            "eventValue.topicId": {"$in": top10Topics},
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user",
        }}
    ]
    return len(list(events.aggregate(pipeLine)))


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
    print problemFirstSecondDict
    return problemFirstSecondDict

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
        if doc['problems']['practice'] == []:
            print("本章节没有专题")
            firstAndSecondProblem['firstProblem'] = None
            firstAndSecondProblem['secondProblem'] = None
        else:
            firstProblem.append(doc['problems']['practice'][0]['_id'])
            secondProblem.append(doc['problems']['practice'][1]['_id'])
            firstAndSecondProblem['firstProblem'] = firstProblem
            firstAndSecondProblem['secondProblem'] = secondProblem
    return firstAndSecondProblem

def removeObjectId(changeList):
    returnList = []
    for doc in changeList:
        returnList.append(str(doc))
    return returnList

def uvOfAnswerFirstProblemSetFirstProblem(startDate, endDate, inputProblemList, platform):
    if inputProblemList == None:
        return 0
    else:
        problemList = removeObjectId(inputProblemList)
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "answerProblem",
            "eventValue.problemId": {"$in": problemList},
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))

# 练习模块真实总完成率 完成量(completeMaster->topics)/真正进入量
def top10TopicsCompleteMaster(startDate, endDate, topTenTopics, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "completeMaster",
            "eventValue.topicId": {"$in": topTenTopics},
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
    print("%.2f / %.2f ")%(m,d)
    num = ("%.2f")%(m/d*100)
    return num

# 挑战失败率	挑战题设计参考 是否过难	挑战失败量/挑战进入量
def intoChallage(startDate, endDate, topTenTopics, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "startChallenge",
            "eventValue.topicId": {"$in": topTenTopics},
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return len(list(events.aggregate(pipeLine)))

def failInChallage(startDate, endDate, topTenTopics, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "challengeFailure",
            "eventValue.topicId": {"$in": topTenTopics},
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return list(events.aggregate(pipeLine))

def successChallage(startDate, endDate, topTenTopics, platform):
    pipeLine = [
        {"$match": {
            "serverTime": {
                "$gte": startDate,
                "$lt": endDate
            },
            "eventKey": "challengeSuccess",
            "eventValue.topicId": {"$in": topTenTopics},
            "platform2": platform
        }},
        {"$group": {
            "_id": "$user"
        }}
    ]
    return list(events.aggregate(pipeLine))

pc = "PC"
ios = "iOS"
android = "android"

for topic in weeklyEnterTopicsTopTenList:
    oneTopic = [topic]
    print("----------------------------------")
    topicName = topics.find_one({"_id": ObjectId(topic)})['name']
    print topicName

    # PC
    print("PC 练习进入总量:")
    print(uvOfWeeklyTop10Masters(START_DATE, END_DATE, oneTopic, pc))
    # iOS
    print("iOS 练习进入总量:")
    print(uvOfWeeklyTop10Masters(START_DATE, END_DATE, oneTopic, ios))
    # android
    print("android 练习进入总量:")
    print(uvOfWeeklyTop10Masters(START_DATE, END_DATE, oneTopic, android))

    problemSetsFirstAndSecond = getTop10TopicsFirstAndSecondProblemSet(START_DATE, END_DATE, oneTopic)
    if problemSetsFirstAndSecond.has_key('firstProblemSets'):
        firstProblemSetsFirstProblemList = getFirstProblemSetsFirstAndSecondProblem(problemSetsFirstAndSecond['firstProblemSets'])
        if firstProblemSetsFirstProblemList.has_key('firstProblem') and firstProblemSetsFirstProblemList['firstProblem'] != None:
            problemList1 = firstProblemSetsFirstProblemList['firstProblem']
        else:
            print("专题内没有题目")
            problemList1 = None

    if problemSetsFirstAndSecond.has_key('secondProblemSets'):
        secondProblemSetsFirstProblemList = getFirstProblemSetsFirstAndSecondProblem(problemSetsFirstAndSecond['secondProblemSets'])
        if secondProblemSetsFirstProblemList.has_key('firstProblem') and secondProblemSetsFirstProblemList['firstProblem'] != None:
            problemList2 = secondProblemSetsFirstProblemList['firstProblem']
        else:
            print("专题内任何题目")
            problemList2 = None

    # PC
    print("PC 练习模块真实进入量 --- 练习第一专题第一题作答总量:")
    uvOfRealIntoMaster = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList1, pc)
    print(uvOfRealIntoMaster)

    print("PC 练习模块认真完成量 --- 练习第二专题第一题作答总量:")
    uvOfPayAttetionUser = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList2, pc)
    print(uvOfPayAttetionUser)

    uvOfCompleteMaster = top10TopicsCompleteMaster(START_DATE, END_DATE, oneTopic, pc)
    print("PC 练习模块真实总完成率 --- 完成量/真正进入量:")
    print(perNum(uvOfCompleteMaster, uvOfRealIntoMaster))

    print("PC 认真用户练习模块完成率 --- 完成量/认真完成量:")
    print(perNum(uvOfCompleteMaster, uvOfPayAttetionUser))

    print("PC 挑战失败率	 --- 挑战失败量/挑战进入量:")
    uvOfIntoChallage = intoChallage(START_DATE, END_DATE, oneTopic, pc)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, pc)
    print(perNum(len(uvOfFailChallage), uvOfIntoChallage))

    print("PC 挑战成功率	 --- 挑战成功量/挑战进入量:")
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, pc)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, pc)
    print(perNum(len(uvOfSuccessChallage), uvOfIntoChallage))

    print("PC 挑战完成率	 --- 挑战成功+失败量/挑战进入量")
    failChallageList = []
    for doc in uvOfFailChallage:
        failChallageList.append(doc['_id'])

    successChallageList = []
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, pc)
    for doc in uvOfSuccessChallage:
        successChallageList.append(doc['_id'])
    totalFailAndSuccessChallage = list(set.union(set(failChallageList), set(successChallageList)))

    print(perNum(len(totalFailAndSuccessChallage), uvOfIntoChallage))


    # iOS
    print("iOS 练习模块真实进入量 --- 练习第一专题第一题作答总量:")
    uvOfRealIntoMaster = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList1, ios)
    print(uvOfRealIntoMaster)

    print("iOS 练习模块认真完成量 --- 练习第二专题第一题作答总量:")
    uvOfPayAttetionUser = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList2, ios)
    print(uvOfPayAttetionUser)

    uvOfCompleteMaster = top10TopicsCompleteMaster(START_DATE, END_DATE, oneTopic, ios)
    print("iOS 练习模块真实总完成率 --- 完成量/真正进入量:")
    print(perNum(uvOfCompleteMaster, uvOfRealIntoMaster))

    print("iOS 认真用户练习模块完成率 --- 完成量/认真完成量:")
    print(perNum(uvOfCompleteMaster, uvOfPayAttetionUser))

    print("iOS 挑战失败率	 --- 挑战失败量/挑战进入量:")
    uvOfIntoChallage = intoChallage(START_DATE, END_DATE, oneTopic, ios)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, ios)
    print(perNum(len(uvOfFailChallage), uvOfIntoChallage))

    print("iOS 挑战成功率	 --- 挑战成功量/挑战进入量:")
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, ios)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, ios)
    print(perNum(len(uvOfSuccessChallage), uvOfIntoChallage))

    print("iOS 挑战完成率	 --- 挑战成功+失败量/挑战进入量")
    failChallageList = []
    for doc in uvOfFailChallage:
        failChallageList.append(doc['_id'])

    successChallageList = []
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, ios)
    for doc in uvOfSuccessChallage:
        successChallageList.append(doc['_id'])
    totalFailAndSuccessChallage = list(set.union(set(failChallageList), set(successChallageList)))

    print(perNum(len(totalFailAndSuccessChallage), uvOfIntoChallage))


    # android
    print("android 练习模块真实进入量 --- 练习第一专题第一题作答总量:")
    uvOfRealIntoMaster = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList1, android)
    print(uvOfRealIntoMaster)

    print("android 练习模块认真完成量 --- 练习第二专题第一题作答总量:")
    uvOfPayAttetionUser = uvOfAnswerFirstProblemSetFirstProblem(START_DATE, END_DATE, problemList2, android)
    print(uvOfPayAttetionUser)

    uvOfCompleteMaster = top10TopicsCompleteMaster(START_DATE, END_DATE, oneTopic, android)
    print("android 练习模块真实总完成率 --- 完成量/真正进入量:")
    print(perNum(uvOfCompleteMaster, uvOfRealIntoMaster))

    print("android 认真用户练习模块完成率 --- 完成量/认真完成量:")
    print(perNum(uvOfCompleteMaster, uvOfPayAttetionUser))

    print("android 挑战失败率	 --- 挑战失败量/挑战进入量:")
    uvOfIntoChallage = intoChallage(START_DATE, END_DATE, oneTopic, android)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, android)
    print(perNum(len(uvOfFailChallage), uvOfIntoChallage))

    print("android 挑战成功率	 --- 挑战成功量/挑战进入量:")
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, android)
    uvOfFailChallage = failInChallage(START_DATE, END_DATE, oneTopic, android)
    print(perNum(len(uvOfSuccessChallage), uvOfIntoChallage))

    print("android 挑战完成率	 --- 挑战成功+失败量/挑战进入量")
    failChallageList = []
    for doc in uvOfFailChallage:
        failChallageList.append(doc['_id'])

    successChallageList = []
    uvOfSuccessChallage = successChallage(START_DATE, END_DATE, oneTopic, android)
    for doc in uvOfSuccessChallage:
        successChallageList.append(doc['_id'])
    totalFailAndSuccessChallage = list(set.union(set(failChallageList), set(successChallageList)))

    print(perNum(len(totalFailAndSuccessChallage), uvOfIntoChallage))

    print("\n----------------------------------\n")
