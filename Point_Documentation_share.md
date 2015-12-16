# v3.0 Points Documentation (Video Share)

by ronfe  
Last Modified: 15DEC16 

本文档基于James 20151215钉钉口谕，适用于3.0视频分享页之埋点。  
视频分享页的```platform```为实际平台（pc/iOS/android）

## 分享页

** 进入页面 **

[PC][Mobile] 进入视频分享页。  

---

* ```eventKey: enterSharingPage```
* ```category: site```
* 必传字段：
  - 打开页面的视频ID ```videoId: ObjectId```

** 开始播放视频 **

---

[PC][Mobile]播放视频

* ```eventKey: startVideo```
* ```category: video```
* 必传字段：
 - 播放视频之ID ```videoId: ObjectId```

**暂停视频**

---

[PC][Mobile]暂停视频  

* ```eventKey: pauseVideo```
* ```category: video```
* 必传字段:
  - 视频ID ```videoId: ObjectId```
  - 用户暂停时的视频时间戳（毫秒单位，下同） ```pauseTime: Number```

**完成视频**

---

[PC][Mobile]完成视频  

* ```eventKey: finishVideo```
* ```category: video```
* 必传字段:
  - 视频ID ```videoId: ObjectId```

**分享视频**

---

[PC][Mobile]点击分享按钮

* ```eventKey: shareVideo```
* ```category: site```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 用户分享平台（QQ/QQ空间/微博） ```sharePlatform: String, enum: ['qq', 'qzone', 'weibo']```

**进入主页**

---

[PC]点击“进入主页”

* ```eventKey: clickEnterHomepage```
* ```category: site```

**登录**

---

[PC]点击“登录”

* ```eventKey: clickLoginBtn```
* ```category: site```

**注册**

---

[PC]点击“注册”

* ```eventKey: clickSignupBtn```
* ```category: site```

**点击下载按钮**

---

[Mobile]点击“下载app”

* ```eventKey: clickDownloadApp```
* ```category: site```
