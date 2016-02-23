Event Track Update v3.2 (web/app)
--

Note: 新增埋点如无说明，默认`category`为`site`

### 视频异常埋点（web/app）

注：此部分埋点覆盖式更新。 

web
--

* `videoLoadFailed`
 - `category: video`
 - 视频首次`onError`事件时
 - `{video: String, videoUrl: String, errorCode: String}`

* `videoLoadDeferred`
 - `category: video`
 - 视频首次加载超过6s时
 - `{video: String, videoUrl: String}`

* `getQiniuResSuccess`
 - `category: video`
 - videoLoadFailed或videoLoadDeferred后，请求七牛API成功返回(如果拿不到返回时间，把resTime蠲掉)
 - `{video: String, videoUrl: String, resTime: Number}`

* `getQiniuResFailure`
 - `category: video`
 - videoLoadFailed或videoLoadDeferred后，请求七牛API返回失败
 - `{video: String, videoUrl: String, error: String}`

* `startVideo`
 - `category: video`
 - 第一次playThrough回调，视频开始播放
 - `{video: String, videoUrl: String, loadingTime: Number}` (loadingTime为从视频播放器开始到开始播放视频的历时in毫秒)

* `videoLagged`
 - `category: video`
 - 视频开始播放后，在`onStall`/`onWaiting`/`onSuspend` 事件内计时超过3s, 或者视频开始播放后，触发`onError`事件
 - `{video: String, videoUrl: String, errorEvent: {type: String, enum: ['stall', 'waiting', 'suspend', 'error']}}`

以下埋点详参《PC网速测试逻辑&埋点》  
* `testUserSpeedSuccess`
 - `category: video`
 - GET测试500K文件成功
 - `{video: String, videoUrl: String, startTimeStamp: Number, endTimeStamp: Number}`

* `testUserSpeedFailed`
 - `category: video`
 - GET测试500K文件失败
 - `{video: String, videoUrl: String, startTimeStamp: Number, error: String}`


app
--

* `videoLoadFailed`
 - `category: video`
 - 视频首次报错或加载时长超过10s
 - `{videoId: String, videoUrl: String, duration: Number, netConfig: {type: String, enum: ['none', 'wifi', '3G', '4G', ..]}, cache: Boolean, errorCode: String}` duration加载时长in毫秒

* `getQiniuResSuccess`
 - `category: video`
 - videoLoadFailed后，请求七牛API成功返回(如果拿不到返回时间，把resTime蠲掉)
 - `{videoId: String, videoUrl: String, resTime: Number}`

* `getQiniuResFailure`
 - `category: video`
 - videoLoadFailed后，请求七牛API返回失败
 - `{videoId: String, videoUrl: String, error: String}`

* `startVideo`
 - `category: video`
 - 视频首次播放
 - `{videoId: String, videoUrl: String, duration: Number, netConfig: {type: String, enum: ['none', 'wifi', '3G', '4G', ..]}, cache: Boolean}` duration加载时长in毫秒

* `userQuitLoading`
 - `category: video`
 - 视频首次加载过程中，用户在既未`videoLoadFailed`亦未`startVideo`时退出视频播放器
 - `{videoId: String, videoUrl: String, duration: Number, netConfig: {type: String, enum: ['none', 'wifi', '3G', '4G', ..]}, cache: Boolean}` duration加载时长in毫秒

* `videoLagged`
 - `category: video`
 - 视频开始播放后，自然中断播放（非用户暂停、停止、退出播放器等行为引起的中断播放）时长超过3s
 - `{videoId: String, videoUrl: String, duration: Number, netConfig: {type: String, enum: ['none', 'wifi', '3G', '4G', ..]}, cache: Boolean}` duration中断时长in毫秒，如没有可蠲掉


### Web

* ```enterOuterPage``` 的```eventValue```加上```subject```。若用户进入物理外循环页，则```subject: "physics"```，如果是数学外循环页```subject: "math"```

* 数学外循环页的物理Banner，点击右上角关闭图标
  - `eventKey: clickClosePhysicsBanner`

* 外循环页，点击“学科”
  -  `eventKey: clickSwitchSubject`

* 外循环页，切换学科成功
  - `eventKey: switchSubjectSuccess`
  - 用户所选的学科：`subject: {enum: ['math', 'physics']}`
  
* 物理，进入问卷页面
  - `eventKey: enterQuestionnairePage`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)

* 物理问卷，点击“我不想回答”或左上角关闭图标
  - `eventKey: clickQuitQuestionnairePage`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)

* 物理问卷，点击“提交”
  - `eventKey: clickSubmitQuestionnaire`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)


### App

* ```enterChapterListPage``` 的```eventValue```加上```subject```。若用户进入物理外循环页，则```subject: "physics"```，如果是数学外循环页```subject: "math"```

* 数学外循环页的物理Banner，点击“立即观看”  
  - `eventKey: clickGoPhysics`

* 数学外循环页的物理Banner，点击右上角关闭图标
  - `eventKey: clickClosePhysicsBanner

* 个人中心，点击“学科”
  -  `eventKey: clickSwitchSubject`

* 个人中心，切换学科成功
  - `eventKey: switchSubjectSuccess`
  - 用户所选的学科：`subject: {enum: ['math', 'physics']}`
  
* 物理，进入问卷页面
  - `eventKey: enterQuestionnairePage`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)

* 物理问卷，点击“我不想回答”或左上角关闭图标
  - `eventKey: clickQuitQuestionnairePage`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)

* 物理问卷，点击“提交”
  - `eventKey: clickSubmitQuestionnaire`
  - `questionType: {enum: ['quit', 'finish']}` (分别对应“退出视频”和“完成视频”问卷)

