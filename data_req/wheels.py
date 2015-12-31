from classDef import *


def get_new_users(start, end):
    device_attr_col.find({
        "activateDate": {"$gte": start, "$lt": end}
    })
    device_list = []
    rentou_list = []
    for d in device_attr_col:
        device_list.append(Device(d))

    for d in device_list:
        rentou_list += d.rentou_list
    return rentou_list


def get_event_flow(start, end, platform):
    rentou_list = get_new_users(start, end)
    event_flows = [r.collect_events(start, end, platform) for r in rentou_list]
    return event_flows





