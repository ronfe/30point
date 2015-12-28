from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['onionsBackupOnline']
db_cache = MongoClient('10.8.8.111:27017')['cache']

event_flow = db_cache['eventFlow']
device_attr_col = db_cache['deviceAttr']
users = db['users']

class Rentou:
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
            Rentou.already_registered[self.unique_id] = self
        else:
            Rentou.already_registered[self.user_id] = self

    def add_device(self, device):
        self.devices.append(device)
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



y = {
    "_id" : ObjectId("567d089e8223976cc8dfc71f"),
    "users" : [
        ObjectId("563c4614ed88f8da05fe6fce")

    ],
    "recentSession" : datetime.datetime(2015, 12, 2, 12, 41, 48,755),
    "platform" : "android",
    "activateDate" : datetime.datetime(2015, 11, 20, 11, 13, 36, 82),
    "device" : "yanhui rejecor a check"
}

z = {
    "_id" : ObjectId("564f0061ceabbcd42b046bf7"),
    "users": [
        ObjectId("563c4614ed88f8da05fe6fce")

    ],
    "recentSession" : datetime.datetime(2015, 12, 2, 12, 41, 48,755),
    "platform" : "android",
    "activateDate" : datetime.datetime(2015, 11, 20, 11, 13, 36, 82),
    "device" : "yanhui rejecor a check"
}

trial = Device(y)
trial2 = Device(z)

print trial.device_id
print trial2.device_id

print Rentou.already_registered[ObjectId("563c4614ed88f8da05fe6fce")].devices
print Rentou.already_registered.keys()

