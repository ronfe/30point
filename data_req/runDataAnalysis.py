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


def run(start):
    end = start + datetime.timedelta(days=7)
    topicIds = weeklyTopicsEnterTop10(start, end)
    topic_list = []
    for t in topicIds:
        to = topics.find_one({"_id": ObjectId(t)}, {'name': 1})
        topic_list.append({"_id": str(to['_id']), "name": to['name']})

    print "---------- 新用户当天行为 ----------"
    td.data_by_day(start, end)

    print "---------- 新用户次周行为 ----------"
    nw.next_week(start, end)

    print "---------- 情景设定 ----------"
    # sc.print_topic_scene(topic_list, start, end)

    print "--------- 时间分析 ----------"
    # ta.print_time_analysis(topic_list, start, end)

s = time.time()


START_DATE = datetime.datetime(2015, 12, 20) - datetime.timedelta(hours=8)
# END_DATE = datetime.datetime(2016, 1, 17, 0) - datetime.timedelta(hours=8)

run(START_DATE)
run(START_DATE+datetime.timedelta(days=7))
run(START_DATE+datetime.timedelta(days=14))
run(START_DATE+datetime.timedelta(days=21))
run(START_DATE+datetime.timedelta(days=28))


e = time.time()
print '总用时: ', (e-s)/ 60, 'min'

