/**
 * Created by ronfe on 15-12-1.
 */
'use strict';
/**
 * Note before usage
 * ua detect need to import https://github.com/zsxsoft/useragent.js into browser
 **/

var metaPoint = {};

//GA configure
(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
    a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');


+function (window) {
    // ua-host mapping
    // Use the very first letter in window.location.hostname as key
    // TODO: replace with the right GA ua for m.yangcong and vs.yangcong
    var gaMapping = {
        'y': 'UA-66876862-1',
        'w': 'UA-66876862-1',
        'm': 'UA-66876862-1',
        'v': 'UA-66876862-1'
    };

    var pointPltformMapping = {
        'y': 'web',
        'w': 'web',
        'm': 'landing',
        'v': 'vs'
    };
    var hostCategory = window.location.hostname[0];

    /**
     * Send point data with Ajax.
     * @param pointData
     */
    var sendPoint = function (pointData) {
        $.ajax({
            async: false,
            type: 'POST',
            //TODO change to the real point api
            url: '/point/' + window.location.search,
            dataType: 'json',
            data: {"points": [pointData]},
            error: function (XMLHttpRequest, textStatus, err) {
                console.error(err);
            }
        });
    };

    /**
     * Generate a Point object with all needed information.
     * @returns {{}} A point object.
     */
    var initPoint = function () {
        var point = {};

        var pointDevice;
        if (document.cookie.match(/point\.device/) == null) {
            var tempId = new ObjectId().toString();
            document.cookie = 'point.device=' + tempId;
        }
        pointDevice = document.cookie.match(/point\.devide\=\w+(?=(;|$))/)[0].split('=')[1];
        point.device = pointDevice;
        point.deviceAttr = {
            os: {
                name: ua.os.name,
                version: ua.os.version
            },
            browser: {
                name: ua.browser.name,
                version: ua.browser.version
            }
        };
        point.platform = pointPltformMapping[hostCategory];
        //TODO: judge platform2 by device model
        point.platform2 = 'pc';

        //meta ua config
        var gaUa = gaMapping[hostCategory];
        ga('create', gaUa, 'auto');
        return point;
    };
    metaPoint = initPoint();

    /**
     * Bind an event to this HTML element.
     * @param pointData
     * @param userData
     */
    var buryPoint = function (pointData, userData) {
        if (!pointData.eventKey) throw new Error('No EventKey Be Defined');

        var thisPoint = metaPoint;

        //user attr field
        if (userData !== undefined) {
            thisPoint.user = userData._id;
            thisPoint.userAttr = {
                type: userData.type,
                isRegistered: true,
                registDate: userData.registTime,
                activateDate: userData.activateTime,
                from: userData.from,
                role: userData.role
            };

            ga('set', '&uid', userData._id);
            ga('set', 'dimension2', userData.role);//设置用户角色
            ga('set', 'dimension1', userData.channel);//设置用户渠道
            ga('set', 'dimension4', userData.from);//设置用户创建方式
            ga('set', 'dimension3', userData.gender);//设置用户性别
            ga('set', 'dimension6', userData.activateDate);
            ga('set', 'dimension7', userData.type);

            if (userData.school !== undefined) {
                thisPoint.userAttr.school = userData.school;
            }
        }
        else {
            thispoint.userAttr = {
                isRegistered: false
            };
            ga('set', '&uid', thisPoint.device);
        }

        //point info
        thisPoint.url = window.location.href;
        thisPoint.q = pointData.q;

        //event info
        thisPoint.eventKey = pointData.eventKey;
        thisPoint.category = pointData.category;
        thisPoint.eventValue = pointData.eventValue;
        thisPoint.eventTime = Date.now();

        //GA
        ga('set', 'dimension8', pointData.eventKey);


        //send
        if (pointData.eventKey !== 'userActivate') {
            //send with parallel
            sendPoint(thisPoint);
            ga('send', {
                'hitType': 'event',
                'eventCategory': pointData.category,
                'eventAction': pointData.eventKey,
                'eventValue': JSON.stringify(thisPoint)
            });
        }
        else {
            var gaSuccess = false;
            ga('send', {
                'hitType': 'event',
                'eventCategory': eventType,
                'eventAction': gaEvent,
                'eventValue': JSON.stringify(gaPointData),
                'hitCallback': function () {
                    gaSuccess = true;
                    sendPoint(pointData);
                }
            });

            setTimeout(function () {
                if (gaSuccess === false) {
                    sendPoint(pointData);
                }
            }, 3000);
        }
    };
}(window);

//ObjectId part
/**
 * Javascript class that mimics how WCF serializes a object of type MongoDB.Bson.ObjectId
 * and converts between that format and the standard 24 character representation.
 */
var ObjectId = (function () {
    var increment = Math.floor(Math.random() * (16777216));
    var pid = Math.floor(Math.random() * (65536));
    var machine = Math.floor(Math.random() * (16777216));

    var setMachineCookie = function () {
        var cookieList = document.cookie.split('; ');
        for (var i in cookieList) {
            var cookie = cookieList[i].split('=');
            var cookieMachineId = parseInt(cookie[1], 10);
            if (cookie[0] == 'mongoMachineId' && cookieMachineId && cookieMachineId >= 0 && cookieMachineId <= 16777215) {
                machine = cookieMachineId;
                break;
            }
        }
        document.cookie = 'mongoMachineId=' + machine + ';expires=Tue, 19 Jan 2038 05:00:00 GMT;path=/';
    };
    if (typeof (localStorage) != 'undefined') {
        try {
            var mongoMachineId = parseInt(localStorage['mongoMachineId']);
            if (mongoMachineId >= 0 && mongoMachineId <= 16777215) {
                machine = Math.floor(localStorage['mongoMachineId']);
            }
            // Just always stick the value in.
            localStorage['mongoMachineId'] = machine;
        } catch (e) {
            setMachineCookie();
        }
    }
    else {
        setMachineCookie();
    }

    function ObjId() {
        if (!(this instanceof ObjectId)) {
            return new ObjectId(arguments[0], arguments[1], arguments[2], arguments[3]).toString();
        }

        if (typeof (arguments[0]) == 'object') {
            this.timestamp = arguments[0].timestamp;
            this.machine = arguments[0].machine;
            this.pid = arguments[0].pid;
            this.increment = arguments[0].increment;
        }
        else if (typeof (arguments[0]) == 'string' && arguments[0].length == 24) {
            this.timestamp = Number('0x' + arguments[0].substr(0, 8)),
                this.machine = Number('0x' + arguments[0].substr(8, 6)),
                this.pid = Number('0x' + arguments[0].substr(14, 4)),
                this.increment = Number('0x' + arguments[0].substr(18, 6))
        }
        else if (arguments.length == 4 && arguments[0] != null) {
            this.timestamp = arguments[0];
            this.machine = arguments[1];
            this.pid = arguments[2];
            this.increment = arguments[3];
        }
        else {
            this.timestamp = Math.floor(new Date().valueOf() / 1000);
            this.machine = machine;
            this.pid = pid;
            this.increment = increment++;
            if (increment > 0xffffff) {
                increment = 0;
            }
        }
    };
    return ObjId;
})();

ObjectId.prototype.getDate = function () {
    return new Date(this.timestamp * 1000);
};

ObjectId.prototype.toArray = function () {
    var strOid = this.toString();
    var array = [];
    var i;
    for (i = 0; i < 12; i++) {
        array[i] = parseInt(strOid.slice(i * 2, i * 2 + 2), 16);
    }
    return array;
};

/**
 * Turns a WCF representation of a BSON ObjectId into a 24 character string representation.
 */
ObjectId.prototype.toString = function () {
    if (this.timestamp === undefined
        || this.machine === undefined
        || this.pid === undefined
        || this.increment === undefined) {
        return 'Invalid ObjectId';
    }

    var timestamp = this.timestamp.toString(16);
    var machine = this.machine.toString(16);
    var pid = this.pid.toString(16);
    var increment = this.increment.toString(16);
    return '00000000'.substr(0, 8 - timestamp.length) + timestamp +
        '000000'.substr(0, 6 - machine.length) + machine +
        '0000'.substr(0, 4 - pid.length) + pid +
        '000000'.substr(0, 6 - increment.length) + increment;
};