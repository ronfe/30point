from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
db_cache = MongoClient('10.8.8.111:27017')['cache']

event_flow = db_cache['eventFlow']
device_attr_col = db_cache['deviceAttr']
users = db['users']
events = db['events']

class Rentou:
    already_user = {}
    already_registered = {}
    devices = []
    device_exclusive = True
    user_id = ""
    unique_id = ""

    def __init__(self, device, user_id):
        self.unique_id = ObjectId
        if not device.is_exclusive:
            self.device_exclusive = False
            
        self.user_id = user_id
        self.add_device(device)
        if self.user_id == "":
            Rentou.already_registered[self.devices[0].device_id] = self
        else:
            Rentou.already_user[self.user_id] = self

    def add_device(self, device):
        self.devices.append(device)
        self.devices = list(set(self.devices))

class Device:
    device_id = ""
    is_exclusive = True
    platform = "pc"
    users = []
    rentou_list = []
    activate = datetime.datetime(2015,12,19)
    recent = datetime.datetime(2015,12,19)

    def __init__(self, device_attr):
        meta_data = device_attr
        self.device_id = meta_data['_id']
        self.users = meta_data['users']
        self.platform = device_attr['platform']
        self.activate = device_attr['activateDate']
        self.recent = device_attr['recentSession']
        rentou_list = []
        if len(self.users) >= 2:
            self.is_exclusive = False
            for each in self.users:
                rentou_list.append(Rentou(self, each)) 
        elif len(self.users) == 0:
            rentou_list.append(Rentou(self, ""))
        else:
            if self.users[0] in Rentou.already_registered.keys():
                this_rentou = Rentou.already_registered[self.users[0]]
                this_rentou.add_device(self)
            else:
                this_rentou = Rentou(self, self.users[0])

            rentou_list.append(this_rentou)

        self.rentou_list = rentou_list

    def output(self):
        x = {
            "id": self.device_id,
            "isExclusive": self.is_exclusive,
            "users": self.users,
            "rentou": self.rentou_list,
            "platform": self.platform
        }
        return x

START = datetime.datetime(2015,12,23)
END = datetime.datetime(2015,12,24)

# STEP 1 get all the new users in time period
new_user_q = users.find({"type": {"$ne": "batch"}, "registTime": {"$gte": START, "$lt": END}}, {"_id": 1})
new_user_batch_q = users.find({"type":"batch", "activateDate": {"$gte": START, "$lt": END}}, {"_id": 1})
user_group = [doc["_id"] for doc in new_user_q] + [doc["_id"] for doc in new_user_batch_q]

# STEP 2 get all the related devices
device_group = device_attr_col.find({"users": {"$in": user_group}})
device_group = [each for each in device_group]
# remove invalid users
for each in device_group:
    ori_user = set(each['users'])
    new_user = list(ori_user.intersection(set(user_group)))
    each['users'] = new_user
# device_group.remove('null')
# device_group = device_group[2:]


# STEP 3 Add devices
device_list = []
for each in device_group:
    device_list.append(Device(each))

# event_flow_list = []
# for each in Rentou.already_registered.keys():
#     x = Rentou.already_registered[each].collect_events(START, END, ['pc'])
#     event_flow_list.append(x)

# event_flow_list = [each for each in event_flow_list if len(each) > 0]
# print len(event_flow_list)



def collect_events(start, end, platforms):
    x = []
    pipeline = [
        {"$match": {"startTime": {"$gte": start, "$lt": end}, "platform": {"$in": platforms}, "device": {"$in": Rentou.already_registered.keys()}}},
        {"$group": {"_id": "$device", "eventFlows": {"$push": "$eventFlow"}}}
    ]
    x = list(event_flow.aggregate(pipeline))

    if len(x) > 0:
        x = sum(x[0]["eventFlows"], [])
    else:
        x = []

    pipeline = [
        {"$match": {"startTime": {"$gte": start, "$lt": end}, "platform": {"$in": platforms}, "user": {"$in": Rentou.already_user.keys()}}},
        {"$group": {"_id": "$user", "eventFlows": {"$push": "$eventFlow"}}}
    ]
    y = list(event_flow.aggregate(pipeline))

    if len(y) > 0:
        output = []
        for each in y:
            each_ef = sum(each["eventFlows"], [])
            output.append(each_ef)
        y = output
    else:
        y = []

    return x + y

result = collect_events(START, END, ['pc'])
print len(Rentou.already_user.keys())
print len(result)