# import random

# # export random event key
# eventFlow = []
#
# def randomEvent():
#     actionArray = ['enterHome', 'enterTopic', 'playVideo', 'stopVideo', 'installUbuntu']
#     interEventFlowArray = []
#     for event in range(0,10):
#         interEventFlowArray.append(random.choice(actionArray))
#     return interEventFlowArray
#
#
# for x in range(0,10):
#     eventFlow.append(randomEvent())
#
# # print eventFlow
#
#
# # pv:5  uv3
# eventFlow = [
#     ['playVideo', 'enterHome', 'enterHome', 'enterHome', 'installUbuntu', 'enterHome', 'installUbuntu', 'playVideo', 'enterTopic', 'enterTopic'],
#     ['enterHome', 'stopVideo', 'enterHome', 'enterTopic', 'enterHome', 'installUbuntu', 'enterHome', 'enterTopic', 'playVideo', 'enterTopic'],
#     ['installUbuntu', 'enterHome', 'installUbuntu', 'stopVideo', 'enterHome', 'enterTopic', 'stopVideo', 'playVideo', 'playVideo', 'installUbuntu'],
#     ['installUbuntu', 'installUbuntu', 'enterHome', 'installUbuntu', 'enterTopic', 'stopVideo', 'enterTopic', 'stopVideo', 'enterTopic', 'enterTopic'],
# ]
#
# eventKey = 'playVideo'

def pvUvCount(eventFlow, eventKey):
    pvUv = {}
    pvCounter = 0
    uvCounter = 0
    for oneUserFlow in eventFlow:
        hasThisKey = False
        for event in oneUserFlow:
            if event == eventKey:
                pvCounter += 1
                hasThisKey = True
        if hasThisKey:
            uvCounter += 1
    pvUv['pv'] = pvCounter
    pvUv['uv'] = uvCounter
    return pvUv

print(pvUvCount(eventFlow, eventKey))

