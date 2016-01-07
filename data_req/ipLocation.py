# _*_ coding:utf-8 _*_
from __future__ import print_function
from pymongo import MongoClient
import datetime
import time
import pickle
import grequests


def get_teachers():
    db = MongoClient('10.8.8.111:27017')['miner-prod25']
    points = db['points']
    users = db['users']
    schools = db['schools']
    provinces = db['provinces']

    start_date = datetime.datetime(2015, 9, 30)
    end_date = datetime.datetime(2015, 10, 30)

    teachers = list(users.find({
        "role": "teacher",
        "usefulData.registDate": {"$gte": start_date, "$lt": end_date},
        "school": {"$exists": True}
    }, {
        "_id": 1,
        "school": 1
    }))

    teacherIds = [teacher['_id'] for teacher in teachers]
    print('teacherIds: ', len(teacherIds))

    for teacher in teachers:
        schoolLoc = provinces.find_one(
                {'cities': {"$elemMatch": {'districts': {'$elemMatch': {'schools': teacher['school']}}}}}
        )
        province = schoolLoc['name']
        city = [city for city in schoolLoc['cities'] if (teacher['school'] in [school for district in city['districts'] for school in district['schools']])][0]['name']
        teacher['school'] = schools.find_one({"_id": teacher['school']})
        teacher['school'].update({'province': province, 'city': city})
        print(teacher['school']['name'], province, city)
    print('teachers: ', len(teachers))

    pipeline = [
        {
            "$match": {
                "user": {"$in": teacherIds},
                "header.ip": {"$exists": True},
                "header.location.region0": {"$exists": True}
            }
        },
        {
            "$group": {
                "_id": "$user",
                "ip": {"$first": "$header.ip"},
                "location": {"$first": "$header.location"}
            }
        }
    ]

    locations = list(points.aggregate(pipeline, allowDiskUse=True))
    print("locations: ", len(locations))

    def merge_lists(l1, l2, key):
        merged = {}
        for item in l1+l2:
            if item[key] in merged:
                merged[item[key]].update(item)
            else:
                merged[item[key]] = item
        return [val for (_, val) in merged.items() if 'ip' in val]

    teachers = merge_lists(teachers, locations, '_id')
    print('teachers: ', len(teachers))
    f0 = open('../data/teachers-0930-1030.txt', 'w')
    pickle.dump(teachers, f0)
    f0.close()


def get_taobao_ips():
    f = open('../data/ips.txt', 'w')
    f2 = open("../data/teachers-0930-1030.txt", 'r')
    teachers = pickle.load(f2)
    request = "http://ip.taobao.com/service/getIpInfo.php?ip="
    ips = [request+teacher['ip'] for teacher in teachers]
    rs = (grequests.get(ip) for ip in ips)
    res = grequests.map(rs)
    print(res[0].json())
    res = [r.json()['data'] for r in res]
    pickle.dump(res, f)
    f.close()
    f2.close()


def get_ip_accuracy():
    f = open('../data/ip准确度-0930-1030.txt', 'w')
    f2 = open("../data/teachers-0930-1030.txt", 'r')
    f3 = open("../data/difference-0930-1030.txt", 'w')
    f4 = open('../data/ips-0930-1030.txt', 'r')
    teachers = pickle.load(f2)
    ips = pickle.load(f4)
    print(len(teachers), len(ips))

    l = len(teachers)
    print('number of teachers: ', l)
    counter = 0
    ip_city_missing = 0
    city_different = 0
    school_ip_different = 0
    school_taobao_different = 0
    l = len(ips)
    for i in range(l):
        data = ips[i]
        teacher = teachers[i]
        region0 = teacher['location']['region0'] if teacher['location']['region0'] else 'None'
        region1 = teacher['location']['region1'] if 'region1' in teacher['location'] and teacher['location']['region1'] else 'None'

        if region0 in ['北京市'.decode('UTF-8'), '天津市'.decode('UTF-8'), '上海市'.decode('UTF-8'), '重庆市'.decode('UTF-8')]:
            region1 = region0

        region = data['region'] if data['region'] else 'None'
        city = data['city'] if data['city'] else 'None'
        if teacher['school']['city'] == region0 == city:  # in ['北京市', '天津市', '上海市', '重庆市']:
            pass
        elif any([name.decode('UTF-8') in teacher['school']['city'] and name.decode('UTF-8') in region1 and name.decode('UTF-8') in city for name in ["恩施", "临夏", "黔西", "黔南", "博尔塔拉", "红河", "湘西", "巴音郭楞"]]):
            pass
        elif teacher['school']['city'] != region1 or region1 != city:
            print(teacher['school']['name'].encode("UTF-8"), teacher['school']['province'].encode("UTF-8"), teacher['school']['city'].encode("UTF-8"),
                  "ip:", teacher['ip'], 'ip库:', region0.encode("UTF-8"), region1.encode("UTF-8"),
                  'taobao: ', region.encode("UTF-8"), city.encode("UTF-8"), file=f3)
            if region1 == "None":
                ip_city_missing += 1
            elif region1 != city:
                city_different += 1
            if region1 != "None" and teacher['school']['city'] != region1:
                school_ip_different += 1
            if city != "None" and teacher['school']['city'] != city:
                school_taobao_different += 1
            counter += 1
    f.close()
    f2.close()
    f3.close()
    f4.close()
    print('city missing', ip_city_missing)
    print('city different: ', city_different)
    print('school ip different: ', school_ip_different)
    print('school taobao different: ', school_taobao_different)
    print('total: ', ip_city_missing + school_ip_different + school_taobao_different + city_different)
    print('counter: ', counter)

s = time.time()
get_taobao_ips()
e = time.time()
print("Total Time: ", e-s, ' s.......')
