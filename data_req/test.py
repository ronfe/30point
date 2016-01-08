from pymongo import MongoClient, DESCENDING
import pickle
from bson.objectid import ObjectId
import time
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


s = time.time()

# points = list(events.find({
#     'user': ObjectId('5655b2ef9ef054665d36508b'),
#     'serverTime': {"$gte": datetime.datetime(2015, 10,1), "$lt": datetime.datetime(2015,12,10)}
# }))

# ids = [ObjectId('5655b2ef9ef054665d36508b'), ]

users1 = list(events.find({"eventKey": "completeLearning", "user": {"$exists": True}, "eventValue.topicId": "54c708798bac81fccbd4bb53"}, {'user': 1}))
users2 = list(events.find({"eventKey": "startMaster", "user": {"$exists": True},  "eventValue.topicId": "54c708798bac81fccbd4bb53"}, {'user': 1}))

print(len(users1), len(users2))
userIds1 = [u['user'] for u in users1]
userIds2 = [u['user'] for u in users2]

userIds = list(set(userIds1).intersection(set(userIds2)))

print('number of users:', len(userIds))

users1 = [u for u in users1 if u['user'] in userIds]
users2 = [u for u in users2 if u['user'] in userIds]

print(len(users1), len(users2))

u1 = {}
u2 = {}

for u in users1:
    if u['user'] in u1:
        u1[u['user']].append(u['_id'])
    else:
        u1[u['user']] = [u['_id']]
for u in users2:
    if u['user'] in u2:
        u2[u['user']].append(u['_id'])
    else:
        u2[u['user']] = [u['_id']]

print(u1)

pipeline = [
    {
        "$match": {
            "user": {"$in": userIds}
        }
    },
    {
        "$sort": {
            "eventTime": 1
        }
    },
    {
        "$group": {
            "_id": "$user",
            "points": {"$push": '$_id'}
        }
    }
]

points = list(events.aggregate(pipeline, allowDiskUse=True))

print('points: ', len(points))
counter = 0
for p in points:
    inds1 = [p['points'].index(i) for i in u1[p['_id']]]
    inds2 = [p['points'].index(i) for i in u2[p['_id']]]
    for i in inds1:
        if (i+1) in inds2:
            counter += 1
            break
print counter
e = time.time()
print(e-s)
# {'topic': u'54c708798bac81fccbd4bb69', 'user': ObjectId('5655b2ef9ef054665d36508b')}, {'topic': u'54c708798bac81fccbd4bb5a', 'user': ObjectId('5655b2ef9ef054665d36508b')})