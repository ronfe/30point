from pymongo import MongoClient
import datetime

db = MongoClient('10.8.8.111:27017')['cache']
event_flow = db['eventFlow']

START_DATE = datetime.datetime(2015, 12, 22, 0)
END_DATE = datetime.datetime(2015, 12, 23, 0)


def collect_event(start, end, users, platforms):
    device_list = users['notUsers']
    user_device_list = users['hasUsers']

    pipeline = [
        {
            "$match": {
                "device": {"$in": device_list},
                "startTime": {"$gte": start, "$lt": end},
                "platform": {"$in": platforms}
            }
        },
        {
            "$group": {
                "_id": "$device",
                "eventFlows": {"$push": "$eventFlow"}
            }
        }
    ]
    xx = list(event_flow.aggregate(pipeline, allowDiskUse=True))
    x = []
    for each in xx:
        x.append(sum(each["eventFlows"], []))


    # devices = ["F230CBFF-3D5C-4CB7-8E1E-1F05BD6BD4D2", "B75D97E8-2A27-4290-B87D-51098614A646"]
    devices = list(set(sum(user_device_list.values(), [])))

    pipeline2 = [
        {
            "$match": {
                "startTime": {"$gte": start, "$lt": end},
                "platform": {"$in": platforms},
                "device": {"$in": devices}
            }
        },
        {
            "$sort": {
                "startTime": 1
            }
        },
        {
            "$group": {
                "_id": "$device",
                "userFlows": {"$push": {"user": "$user", "eventFlow": "$eventFlow"}}
            }
        }
    ]
    yyy = list(event_flow.aggregate(pipeline2, allowDiskUse=True))
    yy = {}
    for device in yyy:
        yy.update({device["_id"]: device["userFlows"]})
    print yy
    y = []
    for user in user_device_list:
        user_event_flow = []
        for device in user_device_list[user]:
            if device in yy:
                user_flows = yy[device]
                ind_user = [i for i, flow in enumerate(user_flows) if "user" in flow and flow['user'] == user]
                ind_null = [i for i, flow in enumerate(user_flows) if "user" not in flow]
                ind = ind_user[:]
                for i in ind_user:
                    j = i
                    while (j-1) in ind_null:
                        ind.append(j-1)
                        j -= 1
                user_event_flow += sum([flow['eventFlow'] for i, flow in enumerate(user_flows) if i in ind], [])
        y.append(user_event_flow)
    return x + y


collect_event(START_DATE, END_DATE, {}, ['ios'])











