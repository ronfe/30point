# Track Events Changelog (iOS/Android App v2.1)
--

以下埋点如无明确category标注，其category均为`site`

增补
--

* 学习模块完成页，点击“休息一下”  [diggzhang-0201-Android2.1:**tested**]
	- `quitLearning` -> `clickHaveARest`
	- `site`
	- `{topicId: String, videoId: String}`

Schema
--

* 区分埋点q和用户q，在埋点Schema中添加webChannel字段，用于记录web query里的q，用户自带的q传到埋点的q字段中

引导页
--
**tips**:Android端引导页的enter事件触发时机都是onresume<即每次页面显示，包括从后台回来>

* 只要进入引导页，就发`enterGuidePage`【i】[diggzhang-0201-Android2.1:**tested**]

* 引导页，进入选择教材版本页面【i】【A】[diggzhang-0201-Android2.1:**tested**]
	- `enterChoosePublisherPage`

* 引导页，选择教材版本页面，点击“返回”图标【i】【A】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromChoosePublisher`

* 引导页，选择教材版本页面，点击某个教材【i】【A】[diggzhang-0201-Android2.1:**tested**]
	- `clickChoosePublisher`
	- `{publisher: String}`

* 引导页，进入选择年级页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterChooseGradePage`

* 引导页，选择年级页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromChooseGrade`

* 引导页，选择年级页面，点击某个年级【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickChooseGrade`
	- `{grade: String}`

提示
--
Tips:Android 暂时没有提示功能
* 弹出wifi中断pop【i】
	- `popDownloadTerminatedMsg`

* wifi中断pop，点击“稍后再说”【i】	- `clickDownloadVideoLater`

* wifi中断pop，点击“继续下载”【i】	- `clickDownloadUsingLocalNetwork`

* 弹出服务器开小差pop (iOS Only)
	- `popServerError`

外循环 - 章节列表页面
--

* 进入章节列表页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterChapterListPage`

* 点击“设置”【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterSetting` -> `clickSettingBtn`

* 点击“我的”【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterMyProfile` -> `clickProfileBtn`

* 点击收起某个章节【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickCloseChapterList`
	- `{chapterId: String}`

* 点击某个知识点【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterTopic` -> `clickEnterTopic`

外循环 - 设置页面
--

* 进入设置页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterSettingPage`

* (unsigned用户)点击“注册新用户”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickSignupFromSetting`

* (unsigned用户)点击“登录”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickLoginFromSetting`

* 进入选择教材版本页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterSwitchBookPage`

* 选择教材版本页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromSwitchBook`

* 选择教材版本页面，点击某个教材【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickSwitchBookBtn`
	- `{book: String}`

* 进入选择年级页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterSwitchGradePage`

* 选择年级页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromSwitchGrade`

* 选择年级页面，点击某个年级【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickSwitchGradeBtn`
	- `{grade: String}`

* 进入缓存管理页面【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterBufferManagementHome`

* 缓存管理页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromBufferManagement`

* 缓存管理页面，点击切换顶部tab到“正在下载”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickDownloadingVideosTab`

* 缓存管理页面，点击切换顶部tab到“已下载”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickDownloadedVideosTab`

<!--* 进入用户反馈页面【i】-->
<!--	- `enterUserFeedbackPage`-->

<!--* 用户反馈页面，点击“返回”【i】-->
<!--	- `clickReturnFromUserFeedback`-->

<!--* 用户反馈页面，点击“完善联系信息”【i】-->
<!--	- `clickFillContactForm`-->

<!--* 用户反馈页面，点击“发送”【i】-->
<!--	- `clickSendUserFeedback`-->

* 点击“常见问题”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickFAQ`

* 进入“常见问题”【i】[diggzhang-0201-Android2.1:**tested**]
	- `enterFAQPage`

* 常见问题页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**] 
	- `clickReturnFromFAQ`

* 常见问题页面，点击“用户反馈”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickUserFeedbackFromFAQ`

* 点击“分享”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickShareAppBtn`

外循环 - “我的”页面
--

* enterMyProfile （进入“我的”页面）【i】[diggzhang-0201-Android2.1:**tested**]
	- `{signedStatus: Boolean}`

* “我的”页面，点击“返回”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickReturnFromProfilePage`
	- `{signedStatus: Boolean}`

* (unsigned用户)点击“登录”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickLoginFromProfile`

* (unsigned用户)点击“注册”【i】[diggzhang-0201-Android2.1:**tested**]
	- `clickSignupFromProfile`

外循环 - 知识点详情页
--

* 进入知识点详情页【i】[diggzhang-0201-Android2.1: **tested**]
 	- `enterTopic`
 	- `{topic: String}`
 	- `course`
 
* 点击“返回”【i】[diggzhang-0201-Android2.1: **tested**]
	- `clickReturnFromTopicPage`
	- `{topic: String}`

* (未缓存视频知识点) 点击下载图标【i】[diggzhang-0201-Android2.1: **tested**]
	- `clickDownloadTopicVideo`
	- `{topic: String}`

* (正在缓存视频知识点) 点击暂停图标【i】[diggzhang-0201-Android2.1: **tested**]
	- `clickPauseDownloadTopicVideo`
	- `{topic: String}`

* 点击“进入”视频讲解【i】[diggzhang-0201-Android2.1: **tested**]
	- `startLearning` -> `clickEnterLearning`
	- `course` -> `site`

* 点击“进入”专题训练“【i】[diggzhang-0201-Android2.1: **tested**]
	- `startMaster` -> `clickEnterMaster`
	- `course` -> `site`
	- `{topic: String}`

* 点击”继续“专题训练后，选择”想进入的专题“ [diggzhang-0201-Android2.1:做了一半练习后退出，点击“继续”再回到专题，该点未触发] **该点的测试时机是什么时候 @弘飞**
	- `clickEnterReviewProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 网络连接不正常时，点击“点击刷新” [diggzhang-0201-Android2.1:tested]
	- `clickRefreshTopic`


内循环 - 学习模块
--

* 1. 首次进入视频讲解，学习第一个视频（一个signed用户一辈子一个知识点只发一次enterLearning）【i】[diggzhang-0201-Android2.1:非第一次进入视频讲解，依然触发enterLearning **tested**] 
	- `enterLearning`
	- `course`
	- `{topic: String}`

* 进入一个交互视频【i】[diggzhang-0201-Android2.1: **tested**]
	- `enterHyperVideo`
	- `course`
	- `{topic: String, video: String}`

* 视频完成，页面跳转之前【i】[传来的是videoId diggzhang-0201-Android2.1: **tested**]
	- `finishHyperVideo`
	- `course`
	- `{topic: String, video: String}`

* 视频完成页，点击”退出“ [diggzhang-0201-Android2.1: **tested**]
	- `quitLearning` -> `clickQuitLearningSeries`
	- `course` -> `site`
	- `{topic: String, video: String}`

* (多视频学习模块) 视频完成页,点击”继续学习“ [diggzhang-0201-Android2.1:传来的是videoId topicId **tested**]
	- `clickContinueLearning`
	- `{topic: String, video: String}`

* 修改 - 按我们check过的走【i】[diggzhang-0201-Android2.1:约定字段video,发出的是videoId,但效果一样，建议修改埋点文档 **待定** tested]
	- `finishLearning`
	- `course`
	- `{topic: String, video: String, stars: Number, points: Number}`

内循环 - 练习模块
--

* 点击”进入“练习模块后，进入练习模块 [diggzhang-0201-Android2.1:触发了clickEnterMaster,但没发现enterMaster **tested**]
	- `enterMaster`
	- `course`
	- `{topic: String}`

* 进入专题介绍页  [diggzhang-0201-Android2.1: **tested**]
	- `enterProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 专题介绍页，点击”开始专题“ [diggzhang-0201-Android2.1: **tested**]
	- `clickStartProblemSet`
	- `site`
	- `{topic: String, problemSet: String}`

* 点击”开始专题“后，进入第一道题 [diggzhang-0201-Android2.1: **@逍遥** tested]
	- `startProblemSet`
	- `course`
	- `{topic: String, problemSet: String}`’

* `problemSetFailure`是在进入专题失败页面时发送吗？**未测到该埋点 @弘飞**

* 专题失败页面，点击”讲解“ [diggzhang-0201-Android2.1: **tested**]
	- `clickExplanationFromFailure`
	- `site`
	- `{topic: String, problemSet: String}`

* 专题失败页面，点击”重来“ [diggzhang-0201-Android2.1: **teasted**]
	- `clickStartProblemSetAgain`
	- `site`
	- `{topic: String, problemSet: String}`

* 进入专题完成页面 [diggzhang-0201-Android2.1:未测试到] **待定 未测到该埋点**
	- `finishProblemSet`
	- `course`
	- `{topic: String, problemSet: String, stars: Number, points: Number}`

* 专题/挑战完成页面，点击”返回“，若是挑战，problemSetId发topic id [diggzhang-0201-Android2.1:未触发] **重复 未测到该埋点 @弘飞**
	- `quitProblemSet` -> `clickQuitMaster`
	- `course` -> `site`
	- `{topicId: String, problemSetId: String}`

* 专题/挑战完成页面，点击”下一专题“，若是挑战，problemSetId发topic id [diggzhang-0201-Android2.1:未触发 **争取埋到该点 @弘飞：是要下一个还是当前的topicId**] 
	- `clickContinueNextProblemSet`
	- `site`
	- `{topicId: String, problemSetId: String}`

* 进入挑战介绍页 [diggzhang-0201-Android2.1: **tested**]
	- `enterChallenge`
	- `site`
	- `{topicId: String}`

* 挑战页面，点击”开始挑战“ [diggzhang-0201-Android2.1: **tested**]
	- `startChallenge` -> `clickStartChallenge`
	- `course` -> `site`
	- `{topicId: String}`

* 点击”开始挑战“后，进入第一道题[diggzhang-0201-Android2.1:**待逍遥发**]
	- `startChallenge`
	- `{topicId: String}`

视频埋点
--

* Schema

	* 所有video埋点的eventValue中加上videoUrl字段，值是video的url，以下埋点不再重复
	* 所有video埋点的eventValue中加上cache字段，值是Boolean，用来标识当前视频是否为用户缓存视频，以下埋点不再重复
	* 在videoLoadFailed后请求七牛拿视频meta信息

* 视频首次开始播放 [diggzhang-0201-Android2.1: **tested**]

	- eK: startVideo
	- eV: {video: String}

* 首次加载视频失败 **tested**

	- eK: videoLoadFailed
	- eV: {video: String, errorCode: String}

* 首次加载失败，请求七牛API成功返回(如果拿不到返回时间，把resTime蠲掉)  **未测到该埋点**

	- eK: getQiniuResSuccess
	- eV: {video: String, resTime: Number}

* 首次加载失败，请求七牛API返回失败  **tested**

	- eK: getQiniuResFailure
	- eV: {video: String, error: String}

* 视频播放过程中出现卡顿(bufferSpeed待定)  **未测到该埋点**
	- eK: videoLagged
	- eV: {video: String, timeStamp: Number, bufferSpeed: Number}

* 视频播放卡顿后再次play  **未测到该埋点**

	- eK: resumePlaying
	- eV: {video: String, timeStamp: Number}

* 视频播放完成（停止播放）[diggzhang-0201-Android2.1:tested]
	- eK: finishVideo
	- eV: {video: String}

* **每次失败发一个点 @弘飞 加点**

题目埋点
--

* Schema
	- 所有problem类埋点的eventValue里加problemIndex字段，值为一个非负整数，用来记录用户专题或挑战的问题序号
	- 所有专题类问题埋点的eventValue里加remainedLife字段，值是一个非负整数，用来记录用户答此题目前的剩余生命值

* 用户提交答案后，点击左下角解析按钮 **@逍遥待测**
	- `clickShowExplanation`
	- `{topic: String, problemSet: String, problem: String}`

* 软键盘出现 [diggzhang-0201-Android2.1:少传一个topic **tested**]
	- `softKeyboardPop`
	- `{topic: String, problemSet: String, problem: String}`

* 软键盘消失 [diggzhang-0201-Android2.1:少传一个topic **tested**]
	- `softKeyboardDisappear`
	- `{topic: String, problemSet: String, problem: String}`

* 填空题，点击输入框 [diggzhang-0201-Android2.1:少传一个topic **tested**]
	- `clickProblemTextbox`
	- `{topic: String, problemSet: String, problem: String}`



