# _*_ coding:utf-8 _*_
from dataFunctions import *
import newUserThatDay as td
import newUserNextWeek as nw
import scene as sc
import timeAnalysis as ta
from bson.objectid import ObjectId


# calculate weekly top 10 topics
def weeklyTopicsEnterTop10(startDate, endDate):
    pipeline = [
        {
            "$match": {
                "eventKey": "enterTopic",
                "serverTime": {
                    "$gte": startDate,
                    "$lt": endDate
                }
            }
        },
        {
            "$group": {
                "_id": "$eventValue.topicId",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": DESCENDING
            }
        }
    ]

    x = list(events.aggregate(pipeline))[:10]
    return [t['_id'] for t in x]


s = time.time()


START_DATE = datetime.datetime(2016, 1, 10, 0)
END_DATE = datetime.datetime(2016, 1, 17, 0)

START_DATE_UTC = START_DATE - datetime.timedelta(hours=8)
END_DATE_UTC = END_DATE - datetime.timedelta(hours=8)


topicIds = weeklyTopicsEnterTop10(START_DATE_UTC, END_DATE_UTC)
topic_list = []
for t in topicIds:
    to = topics.find_one({"_id": ObjectId(t)}, {'name': 1})
    topic_list.append({"_id": str(to['_id']), "name": to['name']})


print "---------- 新用户当天行为 ----------"
td.data_by_day(START_DATE_UTC, END_DATE_UTC)

print "---------- 新用户次周行为 ----------"
nw.next_week(START_DATE_UTC, END_DATE_UTC)

print "---------- 情景设定 ----------"
sc.print_topic_scene(topic_list, START_DATE_UTC, END_DATE_UTC)

print "--------- 时间分析 ----------"
ta.print_time_analysis(topic_list, START_DATE_UTC, END_DATE_UTC)

e = time.time()
print '总用时: ', (e-s)/ 60, 'min'

