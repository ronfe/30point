from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
db_cache = MongoClient('10.8.8.111:27017')['cache']

event_flow = db_cache['eventFlow']
device_attr_col = db_cache['deviceAttr']

class Rentou:
    devices = []
    device_exclusive = True
    user_id = ""
    unique_id = ""

    def __init__(self, device, user_id):
        self.unique_id = ObjectId
        if not device.is_exclusive:
            self.device_exclusive = False
            
        self.user_id = user_id

    def add_device(self, device_id):
        self.devices.append(device_id)
        self.devices = list(set(self.devices))

    def collect_events(self, start, end):
        if self.device_exclusive:
            pipeline = [
                {
                    "$match": {"start": {"$gte": start, "$lt": end}, "device": {"$in": self.devices}}
                },
                {
                    "$group": {"_id": None, "event_flows": {"$push": "$eventFlow"}}
                }
            ]
        else:
            pipeline = [
                {
                    "$match": {"start": {"$gte": start, "$lt": end}, "device": {"$in": self.devices}, "user": self.user_id}
                },
                {
                    "$group": {"_id": None, "event_flows": {"$push": "$eventFlow"}}
                }
            ]
        x = list(event_flow.aggregate(pipeline))

        if len(x) > 0:
            return x[0]["event_flows"]
        else:
            return []

class Device:
    device_id = ""
    is_exclusive = True
    platform = "pc"
    users = []
    rentou_list = []

    def __init__(self, device_attr):
        meta_data = device_attr
        self.device_id = meta_data['_id']
        self.users = meta_data['users']
        rentou_list = []
        if len(self.users) >= 2:
            self.is_exclusive = False
            for each in self.users:
                rentou_list.append(Rentou(self, each)) 
        elif len(self.users) == 0:
            rentou_list.append(Rentou(self, ""))
        else:
            rentou_list.append(Rentou(self, self.users[0]))

        self.rentou_list = rentou_list



y = {
    "_id" : ObjectId("567d089e8223976cc8dfc71f"),
    "users" : [
        ObjectId("563c4614ed88f8da05fe6fce"),
        ObjectId("564f0061ceabbcd42b046bf7")
    ],
    "recentSession" : datetime.datetime(2015, 12, 2, 12, 41, 48,755),
    "platform" : "android",
    "activateDate" : datetime.datetime(2015, 11, 20, 11, 13, 36, 82),
    "device" : "yanhui rejecor a check"
}

trial = Device(y)
print trial.device_id
for each in trial.rentou_list:
    print each.user_id
