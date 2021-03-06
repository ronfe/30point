# Track Events Changelog (iOS/Android App v2.1)
--

以下埋点如无明确category标注，其category均为`site`

增补
--

* 学习模块完成页，点击“休息一下”
	- `quitLearning` -> `clickHaveARest`
	- `site`
	- `{topicId: String, videoId: String}`

* 新增 学习模块完成页, 点击"专题训练" [Tao]
    - `clickContinueMaster`
    - `site`
    -`{topicId: String}`

Schema
--

* 区分埋点q和用户q，在埋点Schema中添加webChannel字段，用于记录web query里的q，用户自带的q传到埋点的q字段中

    >移动端??

引导页
--
**tips**:Android端引导页的enter事件触发时机都是onresume<即每次页面显示，包括从后台回来>

* 只要进入引导页，就发`enterGuidePage`【i】

* 引导页，进入选择教材版本页面【i】【A】
	- `enterChoosePublisherPage`

* 引导页，选择教材版本页面，点击“返回”图标【i】【A】
	- `clickReturnFromChoosePublisher`

* 引导页，选择教材版本页面，点击某个教材【i】【A】
	- `clickChoosePublisher`
	- `{publisher: String}`

* 引导页，进入选择年级页面【i】
	- `enterChooseGradePage`

* 引导页，选择年级页面，点击“返回”【i】
	- `clickReturnFromChooseGrade`

* 引导页，选择年级页面，点击某个年级【i】
	- `clickChooseGrade`
	- `{grade: String}`

提示
--
Android 暂时没有提示功能

* 弹出wifi中断pop【i】
	- `popDownloadTerminatedMsg`

* wifi中断pop，点击“稍后再说”【i】
    - `clickDownloadVideoLater`

* wifi中断pop，点击“继续下载”【i】
    - `clickDownloadUsingLocalNetwork`

* 弹出服务器开小差pop (iOS Only)
	- `popServerError`

外循环 - 章节列表页面
--

* 进入章节列表页面【i】
	- `enterChapterListPage`

* 点击“设置”【i】
	- `enterSetting` -> `clickSettingBtn`

* 点击“我的”【i】
	- `enterMyProfile` -> `clickProfileBtn`

* 点击收起某个章节【i】
	- `clickCloseChapterList`
	- `{chapterId: String}`

* 点击某个知识点【i】
	- `enterTopic` -> `clickEnterTopic`

外循环 - 设置页面
--

* 进入设置页面【i】
	- `enterSettingPage`

* (unsigned用户)点击“注册新用户”【i】
	- `clickSignupFromSetting`

* (unsigned用户)点击“登录”【i】
	- `clickLoginFromSetting`

* 进入选择教材版本页面【i】
	- `enterSwitchBookPage`

* 选择教材版本页面，点击“返回”【i】
	- `clickReturnFromSwitchBook`

* 选择教材版本页面，点击某个教材【i】
	- `clickSwitchBookBtn`
	- `{book: String}`

* 进入选择年级页面【i】
	- `enterSwitchGradePage`

* 选择年级页面，点击“返回”【i】
	- `clickReturnFromSwitchGrade`

* 选择年级页面，点击某个年级【i】
	- `clickSwitchGradeBtn`
	- `{grade: String}`

* 进入缓存管理页面【i】
	- `enterBufferManagementHome`

* 缓存管理页面，点击“返回”【i】
	- `clickReturnFromBufferManagement`

* 缓存管理页面，点击切换顶部tab到“正在下载”【i】
	- `clickDownloadingVideosTab`

* 缓存管理页面，点击切换顶部tab到“已下载”【i】
	- `clickDownloadedVideosTab`

<!--* 进入用户反馈页面【i】-->
<!--	- `enterUserFeedbackPage`-->

<!--* 用户反馈页面，点击“返回”【i】-->
<!--	- `clickReturnFromUserFeedback`-->

<!--* 用户反馈页面，点击“完善联系信息”【i】-->
<!--	- `clickFillContactForm`-->

<!--* 用户反馈页面，点击“发送”【i】-->
<!--	- `clickSendUserFeedback`-->

* 点击“常见问题”【i】
	- `clickFAQ`

* 进入“常见问题”【i】
	- `enterFAQPage`

* 常见问题页面，点击“返回”【i】 
	- `clickReturnFromFAQ`

* 常见问题页面，点击“用户反馈”【i】
	- `clickUserFeedbackFromFAQ`

* 点击“分享”【i】
	- `clickShareAppBtn`

外循环 - “我的”页面
--

* enterMyProfile （进入“我的”页面）【i】
	- `{signedStatus: Boolean}`

* “我的”页面，点击“返回”【i】
	- `clickReturnFromProfilePage`
	- `{signedStatus: Boolean}`

* (unsigned用户)点击“登录”【i】
	- `clickLoginFromProfile`

* (unsigned用户)点击“注册”【i】
	- `clickSignupFromProfile`

外循环 - 知识点详情页
--

* 进入知识点详情页【i】
 	- `enterTopic`
 	- `{topic: String}`
 	- `course`
 
* 点击“返回”【i】
	- `clickReturnFromTopicPage`
	- `{topic: String}`

* (未缓存视频知识点) 点击下载图标【i】
	- `clickDownloadTopicVideo`
	- `{topic: String}`

* (正在缓存视频知识点) 点击暂停图标【i】
	- `clickPauseDownloadTopicVideo`
	- `{topic: String}`

* 点击“进入”视频讲解【i】
	- `startLearning` -> `clickEnterLearning`
	- `course` -> `site`
	- 去掉eventValue.state [tao]

* 点击“进入”专题训练“【i】
	- `startMaster` -> `clickEnterMaster`
	- `course` -> `site`
	- `{topic: String}`

* ~~点击”继续“专题训练后，选择”想进入的专题“~~ [tao]
	- `clickEnterReviewProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 网络连接不正常时，点击“点击刷新”
	- `clickRefreshTopic`


内循环 - 学习模块
--

* 1. 首次进入视频讲解，学习第一个视频【i】 未注册用户每次进入都会发; 注册用户若未完成任何视频时每次进入都会发, 完成一个视频后再次进入不会发
	- `enterLearning`
	- `course`
	- `{topic: String}`

* 进入一个交互视频【i】
	- `enterHyperVideo`
	- `course`
	- `{topic: String, video: String}`

* 视频完成，页面跳转之前【i】
	- `finishHyperVideo`
	- `course`
	- `{topic: String, video: String}`

* 视频完成页，点击”退出“ 
	- `quitLearning` -> `clickQuitLearningSeries`
	- `course` -> `site`
	- `{topic: String, video: String}`

* (多视频学习模块) 视频完成页,点击”继续学习“
	- `clickContinueLearning`
	- `{topic: String, video: String}`

* 修改 - 注册用户完成学习模块【i】进入学习模块完成页发; 每次完成都发; 第一次完成时有星星积分;重复完成时星星积分为0 [tao]
	- `finishLearning`
	- `course`
	- `{topic: String, video: String, stars: Number, points: Number}`

* 新增 - 未注册用户完成学习模块 未注册用户 完成所有视频; 每次完成都发
	- `finishLearningUnreg`
	- `course`
	- `{topic: String, video: String}`

* 新增 视频播放时，用户点击右上角视频按钮 [tao] 注：安卓app埋点```sharePlatform```值为```"unknown"```
    - ```eventKey: shareVideoAfterComplete```
    - ```category: site```
    - 视频ID ```videoId: ObjectId```
    - （未载于埋点文档）用户分享平台 ```sharePlatform: String enum: ["qq", "qzone", "weibo", "wechatIM", "wechatShare", 'tencent']```


内循环 - 练习模块
--

* 点击”进入“练习模块后，进入练习模块 和enterLearning逻辑类似
	- `enterMaster`
	- `course`
	- `{topic: String}`

* 进入专题介绍页  
	- `enterProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 专题介绍页，点击”开始专题“ 
	- `clickStartProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 点击”开始专题“后，进入第一道题
	- `startProblemSet`
	- `course`
	- `{topic: String, problemSet: String}`’


* 专题失败页面，点击”讲解“ 
	- `clickExplanationFromFailure`
	- `site`
	- `{topic: String, problemSet: String}`

* 专题失败页面，点击”重来“
	- `clickStartProblemSetAgain`
	- `site`
	- `{topic: String, problemSet: String}`

* 进入专题完成页面 每次完成专题都发
	- `finishProblemSet`
	- `course`
	- `{topic: String, problemSet: String, stars: Number, points: Number}` -> `{topic: String, problemSet: String}`

* 专题/挑战完成页面，点击”返回“，若是挑战，problemSetId发topicId
	- `quitProblemSet` -> `clickQuitMaster`
	- `course` -> `site`
	- `{topicId: String, problemSetId: String}`

* 专题/挑战完成页面，点击”下一专题“，若是挑战，problemSetId发topicId
	- `clickContinueNextProblemSet`
	- `site`
	- `{topicId: String, problemSetId: String}` (problemSetId为当前专题)

* 进入挑战介绍页 
	- `enterChallenge`
	- `site`
	- `{topicId: String}`

* 挑战页面，点击”开始挑战“ 
	- `startChallenge` -> `clickStartChallenge`
	- `course` -> `site`
	- `{topicId: String}`

* 点击”开始挑战“后，进入第一道题
	- `startChallenge`
	- `{topicId: String}`


* ~~新增 注册用户完成所有专题(不包括挑战) 每次完成发 重复完成星星积分为0~~ [tao]
    - `finishAllProblemSet`
    - `course`
    - `{topic: String, stars: Number, points: Number}`

* 新增 未注册用户完成所有专题(不包括挑战) 每次完成发 [tao]
    - `finishAllProblemSetUnreg`
    - `course`
    - `{topic: String}`

视频埋点
--

* Schema

	* 所有video埋点的eventValue中加上videoUrl字段，值是video的url，以下埋点不再重复
	* 所有video埋点的eventValue中加上cache字段，值是Boolean，用来标识当前视频是否为用户缓存视频，以下埋点不再重复
	* 在videoLoadFailed后请求七牛拿视频meta信息  [tao: 七牛bug, 没办法拿到json信息]

* 视频~~首次~~开始播放

	- eK: startVideo
	- eV: {video: String}

* ~~首次~~加载视频失败

	- eK: videoLoadFailed
	- eV: {video: String, errorCode: String}

* ~~首次~~加载失败，请求七牛API成功返回(如果拿不到返回时间，把resTime蠲掉) **暂未测试*

	- eK: getQiniuResSuccess
	- eV: {video: String, resTime: Number}

* ~~首次~~加载失败，请求七牛API返回失败

	- eK: getQiniuResFailure
	- eV: {video: String, error: String}

* ~~视频播放过程中出现卡顿(bufferSpeed待定)~~  **暂时无法实现**
	- eK: videoLagged
	- eV: {video: String, timeStamp: Number, bufferSpeed: Number}

* ~~视频播放卡顿后再次play~~  **暂时无法实现**

	- eK: resumePlaying
	- eV: {video: String, timeStamp: Number}

* 视频播放完成（停止播放）
	- eK: finishVideo
	- eV: {video: String}


题目埋点
--

* Schema
	- 所有problem类埋点的eventValue里加problemIndex字段，值为一个非负整数，用来记录用户专题或挑战的问题序号
	- 所有专题类问题埋点的eventValue里加remainedLife字段，值是一个非负整数，用来记录用户答此题目前的剩余生命值

* 用户提交答案后，点击左下角解析按钮
	- `clickShowExplanation`
	- `{topic: String, problemSet: String, problem: String}`

* 软键盘出现
	- `softKeyboardPop`
	- `{topic: String, problemSet: String, problem: String}`

* 软键盘消失
	- `softKeyboardDisappear`
	- `{topic: String, problemSet: String, problem: String}`

* 填空题，点击输入框
	- `clickProblemTextbox`
	- `{topic: String, problemSet: String, problem: String}`



