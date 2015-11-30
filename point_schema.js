/**
 * Created by ronfe on 15-11-30.
 */
var point = new Schema({
    "eventKey": String, //Required, event name of the point, refer to the doc
    "category": {type: String, enum: ["site", "course", "video", "problem"]}, //Required, event category of the point, refer to the doc
    "eventValue": {}, //Conditional optional, relevant event values, refer to the poiunt doc
    "eventTime": Number, //Required, timeStamp of points generated, unix epoch time (in ms)
    "serverTime": ISODate, //Server required, Time recorded by server
    "device": String, //Required, unique id for pc, imei for android, idfa for ios
    "deviceAttr": {
        "imei": String, //Android app required, device imei
        "idfv": String, //iOS app required, device idfv
        "idfa": String, //iOS app required, device idfa
        "version": String, //App required, app version name
        "os": {
            "name": String, //Required, operating system name macos/linux/win for pc, android/ios/win for mobile
            "version": String //Conditional optional, os version code
        },
        "model": {  //App conditional optional, mobile model information
            "brand": String ,
            "name": String
        },
        "browser": { //Non-app required, browser type and version info
            "name": String,
            "version": String
        }
    },
    "user": ObjectId, //Required, userId for login user, tempId for non-login user
    "userAttr": {
        "isBatch": Boolean, //Conditional optional, required for login user, True if user is batchly made
        "isRegistered": Boolean, //Required, True for login user
        "registDate": ISODate, //Conditional optional, required if "isRegistered" is true, user's date of registration
        "activateDate": ISODate, //Conditional
        "from": String, // Be the same as the user's from (incl. QQ/Weibo/Wechat...)
        "role": {"type": String, "enum": ["teacher", "student"]},
        "ip": String,
        "ipLocation": { // same as header.location in 2.5
            "region0": String, //provincal
            "region1": String //municipal
        },
        "school": ObjectId //only for users who registered his/her school
        "schoolLocation": {
            "region0": String,
            "region1": String
        }
    },
    "url": String, //only for pc, the full url
    "state": {"type": String, enum: ["normal", "lagged"]}, // lagged for app until mobile send points in real time
    "platform": {"type": String, enum: ["web", "app", "share", "landing", "promotion", "vs"]}, //Required
    "platform2": {"type": String, enum: ["PC", "android", "iOS"]}, //Required
    "q": String
});