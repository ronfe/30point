## Track Events Changelog (PC/web v3.1)

Schema
--

* 区分埋点q和用户q，在埋点Schema中添加webChannel字段，用于记录web query里的q，用户自带的q传到埋点的q字段中

补遗
--

* Add
	* 学生首页，点击下载ios应用后点击“直接下载”
		- eK: `clickDownloadIosAppViaPCSS`
	
	* 教师首页，点击下载ios应用后点击“直接下载”
		- eK: `clickDownloadIosAppViaPCTC`
	
	* 学生首页，点击下载android应用后点击“直接下载”
		- eK: `clickDownloadAndroidAppViaPCSS`
	
	* 教师首页，点击下载android应用后点击“直接下载”
		- eK: `clickDownloadAndroidAppViaPCTC`

	* 进入外循环
		- eK: `enterOuterPage`
	
	* 专题介绍页面，点击“开始专题”
		- eK: `clickStartProblemSet`
		- category: `site`
		- eV: `{topic: String, problemSet: String}`
	

* Modify
	* course类埋点eventValue，topicId/problemId/videoId -> topic/problem/video

学生首页 (/student)
---

* Add

	* 首页示例习题，选择某个选项  
		- eK: ```clickSampleProblemOption``` 
		- eV: ```{"answer": String}```  
		
	* 首页示例习题，点击提交按钮  
		- eK: ```clickSampleProblemSubmit```
		- eV: ```{"answer": String, "correctness": Boolean}```  
	
	* 首页底部，点击“下载Windows版”后，在弹出中点击“下载”  
		- eK: ```clickConfirmDownloadWindowsSS```  
	
	* 首页底部，点击“友情链接”
		- eK: ```clickOpenPartnerLinks```   
	
	* 首页底部，点击“友情链接”后，选择某个链接
		- eK: ```clickPartnerLink```
		- eV: ```{"partner": String}```   
	
	* 首页底部，点击“教师版”
		- eK: ```clickBottomSwitchTeacherHome```  
	
	* 首页底部，点击“加入我们”
		- eK: ```clickJoinus```  
	
	* 首页底部，点击“联系我们”
		- eK: ```clickContactus```  
	
	* 首页底部，点击“关于”
		- eK: ```clickAboutus```  
	
	* 首页底部，点击微博Logo
		- eK: ```clickHomeWeibo```  
	
	* 首页底部，点击QQ Logo
		- eK: ```clickHomeQQ```  
	
	* 首页底部，点击QQ 后选择“加入教师群”
		- eK: ```clickJoinTeacherQQGroup```  
	
	* 首页底部，点击QQ后选择“加入家长群”
		- eK: ```clickJoinParentQQGroup```  

	* 首页底部，点击QQ后选择“加入学生群”
		- eK: ```clickJoinStudentQQGroup```  

	* 首页底部，点击微信Logo
		- eK: ```clickHomeWechat```  

* Modify
	* 首页，点击登录
		- eK: ```clickLoginBtn``` -> ```clickLoginPageBtn```

	* 首页，点击注册
		- eK: ```clickSignupBtn``` -> ```clickSignupPageBtn```

	* 首页底部，点击“免费使用”
		- eK: ```clickFreeForUseSS``` -> ```clickBottomFreeForUseSS```
	

教师首页
---

* Modify 
	* 教师首页进入
		- eK: ```enterHome``` -> ```enterTeacherHome``` 
	
	* 首页，点击登录
		- eK: ```clickLoginBtn``` -> ```clickLoginPageBtn```

	* 首页，点击注册
		- eK: ```clickSignupBtn``` -> ```clickSignupPageBtn```
	
	* 首页学校展示，点击“免费使用”
		- eK: ```clickFreeForUseTC``` -> ```clickSchoolFreeForUseTC```
	
	* 首页底部，点击“免费使用”
		- eK: ```clickFreeForUseTC``` -> ```clickBottomFreeForUseTC```
	 

登录页
---


* Add
	* 点击登录按钮
		- eK: ```clickLoginBtn```
	
	* QQ登录成功
		- eK: `qqLoginSuccess`

	* QQ登录失败
		- eK: `qqLoginFailure`

* Modify
	* 点击“马上注册”
		- eK: ```clickSignupBtn``` -> ```clickSwitchSignupBtn```
	

注册页
---

* Add
	* 点击注册按钮
		- eK: ```clickSignupBtn```
	
	* 点击“确认用户协议”复选框
		- eK: ```clickAgreeLicense```
		- eV: ```{value: Boolean}```
	
	* 点击“用户协议”链接
		- eK: ```clickOpenLicense```

* Modify
	* 教师页来注册页，默认选择“教师”时的埋点
		- eK: ```chooseTeacherRole``` -> ```autoChooseTeacherRole```
		
	* 点击“立即登录”
		- eK: ```clickLoginBtn``` -> ```clickSwitchLoginBtn```
	
		
找回密码页
---

* Add
	* 进入找回密码页
		- eK: ```enterForgetPasswd```
	
	* 点击“确认”
		- eK: ```clickConfirmAccount```
	
	* 确认账号失败
		- eK: ```confirmAccountFailure```
		- eV: ```{error: String后端返回stringify, username: String}```
	
	* 确认账号成功
		- eK: ```confirmAccountSuccess```
		- eV: ```{username: String}```  
	
	* 进入短信验证页
		- eK: ```enterSMSVerification```
	
	* 点击“获取手机验证码”
		- eK: ```clickGetSMSCode```
	
	* 获取手机验证码成功
		- eK: ```getSMSCodeSuccess```
	
	* 获取手机验证码失败
		- eK: ```getSMSCodeFailure```
	
	* 点击“确认并重置密码”
		- eK: ```clickResetPasswd```
	
	* 确认并重置密码成功
		- eK: ```resetPasswdSuccess```
	
	* 确认并重置密码失败
		- eK: ```resetPasswdFailure```
		- eV: ```{error: String}```
	
	* 进入邮箱验证页
		- eK: `enterMailVerification`
	
	* 点击“是，向邮箱发送重置链接”
		- eK: `clickSendResetMailBtn`
	
	* 进入重置邮件已发送页面
		- eK: `enterSendResetMailSuccess`
	
	* 点击“返回登录”
		- eK: `clickReturnLoginBtn`
	
	* 点击“重新发送邮件”
		- eK: `clickResendResetMailBtn`
	
	* 进入重置密码页
		- eK: ```enterResetPasswd```
	
	* 点击“确认”
		- eK: ```clickSetPasswd```
	
	* 重置密码成功
		- eK: ```setPasswdSuccess```
	
	* 重置密码失败(后端失败状态)
		- eK: `setPasswdFailure`
		- eV: `{error: String}`
	
	* 进入重置密码成功页
		- eK: `enterResetPasswdSuccess`
	
用户反馈页
--

* Add

	* 点击“帮助与反馈”
		- eK: `clickUserFeedback`
	
	* 进入用户反馈页
		- eK: `enterUserFeedback`
	
	* 点击“提交”
		- eK: `clickSubmitFeedbackBtn`
	
	* 提交反馈成功
		- eK: `submitFeedbackSuccess`
	
	* 提交反馈失败
		- eK: `submitFeedbackFailure`
		- eV: `{error: String, [content/method, content, method]}`
	
	* 点击某项常见问题 
		- eK: `clickFAQ`
		- eV: `{faq: String， 问题题干}`
	
	* 点击关闭按钮或退出
		- eK: `quitUserFeedback`

用户协议页
--

* Add
	
	* 进入用户协议页
		- eK: `enterLicense`

浏览器不兼容提示弹窗
--

* Add

	* 弹窗显示
		- eK: `enterBrowserIncompatibleAlert`

	* 用户点击“下载Windows版”
		- eK: `clickDownloadWinByBrowserIncompatible`
	
	* 用户关闭弹窗
		- eK: `clickCloseBrowserIncompatibleAlert`


学习主线外循环 - 顶部导航栏
--

* Add
	
	* 点击用户下拉菜单
		- eK: `clickUserDropdown`
	
学习主线外循环 - 新手引导部分
--

* Add
	
	* 新手引导各步骤，点击左上角步骤切换
		- eK: `clickSwitchNewbieGuideStep`
		- eV: `{guide: Number}`
	
	* 新手引导第1-3步，点击右上角“跳过此步骤”
		- eK: `clickSkipThisStep`
		- eV: `{thisStep: Number}`
	
	* 新手引导第一步，点击“继续”
		- eK: `clickNextStepBtn`
		- eV: `{nextStep: 2}`
	
	* 新手引导第三步浮层，点击“继续”
		- eK: `clickOpenNewbieProblem`
	
	* 新手引导第三步，点击选择某个选项
		- eK: `clickNewbieOption`
		- eV: `{option: String,选项文本}`
	
	* 新手引导第三步，点击“查看解析”
		- eK: `clickWatchNewbieHint`
	
	* 新手引导第三步，点击“返回题目”
		- eK: `clickReturnNewbieProblem`
	
	* 新手引导第三步，点击“继续”
		- eK: `clickNextStepBtn`
		- eV: `{nextStep: 4}`
	

* Modify
	
	* 新手引导第一步，首次选择教材后切换其他教材
		- eK: `chooseNewbieBook`
		- eV: `{bookId: String}`
	
	* 新手引导第一步，首次选择年级后切换其他年级
		- eK: `chooseNewbieGrade`
		- eV: `{gradeId: String}`	
	
	* 新手引导第二歩浮层，点击“继续”
		- eK: `startNewbieGuideVideo` -> `clickOpenNewbieVideo`


学习主线外循环 - 章节视图部分
--

* Add

	* 点击年级下拉菜单
		- eK: `clickGradeDropdown`
	
	* 点击教材下拉菜单
		- eK: `clickPublisherDropdown`
	
	* 点击“知识树视图”
		- eK: `clickSwitchTreeView`
	
	* 点击“知识列表视图”
		- eK: `clickSwitchListView`

	* ？自动进入知识列表视图
		- eK: `autoSwitchListView`	
	
	* 知识树视图，点击收起某个章节
		- eK: `clickCloseChapterTree`

* Modify

	* 年级下拉菜单后选择年级
		- eV: `{gradeId: String}`
	
	* 知识树视图，点击打开一个章节
		- eK: `startChapter` -> `clickOpenChapterTree`
	
	* 知识树视图，自动打开一个章节(bug: 重复发埋点)
		- eK: `startChapter` -> `autoOpenChapterTree`
	

学习主线外循环 - 知识点视图部分
--

* Add

	* 点击返回图标
		- eK: `clickQuitTopic`
		- eV: `topicId: String`

* Modify

	* 视频讲解部分，点击“进入”
		- eK: `startLearning` -> `clickEnterLearning`
		- category: `course` -> `site`
	
	* 专题训练部分，点击“进入”
		- eK: `startMaster` -> `clickEnterMaster`
		- category: `course` -> `site`

学习主线外循环 - 每周目标部分
--

* Add

	* 已设置目标默认视图，点击设置图标
		- eK: `clickSetPersonalGoal`
	
	* 两个大圆圈视图，点击返回图标
		- eK: `clickWatchGoalStats`

学习主线外循环 - 积分概况部分
--

* Modify
	
	* 点击商店图标
		- eK: `enterShop` -> `clickEnterShop`
	

学习主线外循环 - 关注部分
--

* Add

	* 点击QQ群后选择“加入教师群”
		- eK: ```clickJoinTeacherQQGroup```  
	
	* 点击QQ群后选择“加入家长群”
		- eK: ```clickJoinParentQQGroup```  

	* 点击QQ群后选择“加入学生群”
		- eK: ```clickJoinStudentQQGroup```  

学习主线外循环 - 商店部分
--

* Add

	* 进入商店
		- eK: `enterShop`
	
	* 未购买头像，点击购买按钮，购买失败
		- eK； `buyProfileAvatarFailure`
		- eV: `{newAvatarId: String, error: String}`
	
	* 已购买头像，点击“立即使用”
		- eK: `clickChangeProfileAvatar`
		- eV: `{newAvatarId: String}`
	
	
* Modify

	* 未购买头像，点击购买按钮
		- eK: `changeProfileAvatar` -> `buyProfileAvatar`
	
	* 购买成功
		- eK: `changeProfileAvatarSuccess` -> `buyProfileAvatarSuccess`
	

个人中心
--

* Add

	* 个人中心右侧栏，点击“个人资料”
		- eK: `clickPersonalProfile`

	* 个人中心右侧栏，点击“社交账号绑定”
		- eK: `clickBindSocialAccounts`
	
	* 点击性别
		- eK: ```clickSwitchGender```
		- eV: ```{newGender: [male, female]}```
	
	* 查找学校弹出，选择“省下拉”
		- eK: ```clickFindSchoolProvinceDropdown`
		
	* 查找学校弹出，选择“市下拉”
		- eK: ```clickFindSchoolCityDropdown`
	
	* 查找学校弹出，选择“区下拉”
		- eK: ```clickFindSchoolDistrictDropdown`
	
	* 查找学校弹出，选择某个学校
		- eK: ```clickSelectSchool```
	
	* 查找学校弹出，点击“没有我的学校”后点击“确定”
		- eK: `clickConfirmCustomSchool`
		- eV: `{schoolName: String}`
	
	* 点击年级下拉菜单
		- eK: `clickGradeDropdown`
	
	* 点击年级
		- eK: `clickSwitchGrade`
		- eV: `{gradeId: String}`
	
	* 点击“保存当前修改”
		- eK: `clickSaveChanges`
	
	* 修改成功浮层，点击“确定”
		- eK: `clickCloseSaveMessage`
	
	* 密码修改页面，输入旧密码，点击“下一步”
		- eK: `clickModifyPasswdNext`
		- eV: `{thisStep: 1}`
	
	* 密码修改页面，输入新密码，点击“下一步”
		- eK: `clickModifyPasswdNext`
		- eV: `{thisStep: 2}`
	
	* 密码修改页面，密码修改成功
		- eK: `modifyPasswdSuccess`
	
	* 密码修改页面，密码修改失败
		- eK: `modifyPasswdFailure`
		- eV: `{error: String}`
	
	* 我的班级页面，点击“搜索”
		- eK: `clickSearchMyClass`
		- eV: `{className: String}`
	
	* 我的班级页面，搜索后点击“班级+点击加入”
		- eK: `clickJoinClass`
		- eV: `{className: String}`

* Modify

	* 社交账号绑定页面，未绑定QQ下，点击“立即绑定”
		- eK: `clickBindSocial` -> `clickBindQQ`
	
内循环 - Site类埋点
--

* Add

	* 学习模块视频页，用户点击右上角关闭图标
		- eK: `clickCloseLearning`
		- eV: `topic: String, video: String`
	
	* 学习模块视频页，用户点击右上角关闭图标后，选择“取消”
		- eK: `clickCancelCloseLearning`
		- eV: `topic: String, video: String`
	
	* 学习模块，用户点击进度条回到某个视频
		- eK: `clickReviewVideo`
		- eV: `{topic: String, video: String}`
	
	* 多视频学习模块视频完成页，用户点击“继续观看”
		- eK: `clickNextVideo`
		- eV: `{topic: String, video: String}`
	
	* 练习模块，用户点击进度条回到某个专题/挑战(如果是挑战，problemSet传topicId)
		- eK: `clickReviewProblemSet`
		- eV: `{topic: String, problemSet: String}`

	* 练习模块问题页，用户点击“返回题目”
		- eK: `clickHideExplanation`
		- eV: `{topic: String, problemSet: String, problem: String}`
	
	* 练习模块问题页，用户点击右上角关闭图标(如果是挑战题目，problemSet传topicId)
		- eK: `clickCloseProblem`
		- eV: `{topic: String, problemSet: String, problem: String}`
	
	* 练习模块问题页，用户点击右上角关闭图标后，选择“取消”(如果是挑战题目，problemSet传topicId)
		- eK: `clickCancelCloseProblem`
		- eV: `{topic: String, problemSet: String, problem: String}`
		
	* 练习模块专题失败页/成功页，用户点击右上角关闭图标
		- eK: `clickCloseProblemSet`
		- eV: `{topic: String, problemSet: String}`

	* 练习模块专题失败页，用户点击右上角关闭图标后，选择“取消”
		- eK: `clickCancelCloseProblemSet`
		- eV: `{topic: String, problemSet: String}`
	
	* 练习模块专题失败页，点击“再来一次”
		- eK: `clickProblemSetAgain`
		- eV: `{topic: String, problemSet: String}`
	
	* 练习模块专题成功页，自动切换小圆点
		- eK: `autoSwitchProblemSetSlick`
		- eV: `{topic: String, problemSet: String}`
	
	* 练习模块专题成功页，点击两个切换小圆点
		- eK: `clickSwitchProblemSetSlick`
		- eV: `{topic: String, problemSet: String}`
	
	* 练习模块专题成功页，点击“下一专题”
		- eK: `clickNextMaster`
		- eV: `{topic: String, problemSet: String}`
	
	* 练习模块挑战失败页/成功页，用户点击右上角关闭图标
		- eK: `clickCloseChallenge`
		- eV: `{topic: String}`
	
	* 练习模块挑战失败页，用户点击右上角关闭图标后，选择“取消”
		- eK: `clickCancelCloseChallenge`
		- eV: `{topic: String}`
	
	* 练习模块挑战失败页，用户点击“返回专题”
		- eK: `clickReturnProblemSet`
		- eV: `{topic: String, nextProblemSet: String}`
	
	* 练习模块挑战成功页，用户点击“完成知识点”  
		注意：此处完成不一定是真完成，完成知识点仍要使用course类埋点中的finishMaster/finishLearning统计
		- eK: `clickFinishTopicBtn`
		- eV: `{topic: String}`
	
	* 练习模块挑战问题页，用户答错后选择“继续”
		- eK: `clickEnterChallengeFailedPage`
		- eV: `{topic: String, problem: String, problemIndex: Number}`

* Modify

	* 学习模块视频页，用户点击右上角关闭图标后，选择“确认退出”
		- eK: `quitVideo` -> `clickConfirmCloseLearning`
		- eV: `{topic: String, video: String}`
	
	* 学习模块完成页，用户点击右上角关闭图标
		- eK: `quitLearning` -> `clickCloseLearning`
		- eV: `{topic: String}`
	
	* 学习模块完成页，用户点击“休息一下”
		- eK: `quitLearning` -> `clickHaveARest`
		- eV: `{topic: String}`
	
	* 学习模块完成页，用户点击“专题训练”
		- eK: `startMaster` -> `clickContinueMaster`
		- eV: `{topic: String}`
	
	* 练习模块问题页，提交答案后点击“查看解析”
		- eK: `showAnswer` -> `clickShowExplanation`
		- eV: `{topic: String, problemSet: String, problem: String}`
	
	* 练习模块问题页，用户点击右上角关闭图标后，选择“确认退出”(如果是挑战题目，problemSet传topicId)
		- eK: `terminateProblemSet` -> `clickConfirmCloseProblem`
		- eV: `{topic: String, problemSet: String, problem: String}`
	
	* 练习模块专题失败页，用户点击右上角关闭图标后，选择“确认退出”
		- eK: `quitProblemSet` -> `clickConfirmCloseProblemSet`
		- eV: `{topic: Stirng, problemSet: String}`
	
	* 练习模块挑战失败页，用户点击右上角关闭图标后，选择“确认退出”
		- eK: `quitChallenge` -> `clickConfirmCloseChallenge`
		- eV: `{topic: String}`
	
	
Course类埋点 - 完全重构
--

* startTopic
	- 未完成本知识点任意视频/挑战/专题/模块等，进入知识点详情页
	- `{topic: String}`

* reviewTopic
	- 除`startTopic`外任何情况下进入知识点详情页
	- `{topic: String}`

* startLearning
	- 未完成本知识点任意视频，进入视频播放页
	- `{topic: String}`

* reviewLearning
	- 除`startLearning`外任何情况下，进入视频播放页
	- `{topic: String, video: String}`

* finishLearning
	- 进入最后一个视频完成页，得到星星与积分
	- `{topic: String, stars: Number, points: Number}`

* startHyperVideo
	- 未完成本视频时，进入视频播放页
	- `{topic: String, video: String}`

* reviewHyperVideo
	- 已完成本视频时，进入视频播放页
	- `{topic: String, video: String}`

* finishHyperVideo
	- 进入视频完成页得到星星（与积分）
	- `{topic: String, video: String, stars: Number, points: Number}`

* startMaster
	- 未完成本知识点任意专题/挑战，进入专题页面
	- `{topic: String}`

* reviewMaster
	- 除`startMaster`外任何情况下，进入专题页面
	- `{topic: String, problemSet: String}`

* finishMaster
	- 完成挑战，得到星星与积分
	- `{topic: String, stars: Number, points: Number}`

* startProblemSet
	- 未完成本专题，打开专题第一道题目
	- `{topic: String, problemSet: String}`

* reviewProblemSet
	- 除`startProblemSet`外任何情况下，进入本专题第一道题目
	- `{topic: String, problemSet: String}`

* finishProblemSet
	- 完成专题，得到星星（与积分）
	- `{topic: String, problemSet: String, stars: Number, points: Number}`

* problemSetFailed
	- 专题失败页面
	- `{topic: String, problemSet: String}`

* startChallenge
	- 未完成本挑战，进入挑战第一题
	- `{topic: String}`

* reviewChallenge
	- 已完成本挑战，进入挑战第一题
	- `{topic: String}`

* finishChallenge
	- 完成挑战，进入挑战成功页面，获得积分与星星
	- `{topic: String, stars: Number, points: Number}`

* challengeFailed
	- 挑战失败，进入挑战失败页面
	- `{topic: String}`


Video类埋点 - 不完全重构
--

* Schema
	* 所有video埋点的eventValue中加上videoUrl字段，值是video的url，以下埋点不再重复
	* 在videoLoadFailed后请求七牛拿视频meta信息


* 第一次playThrough回调，视频开始播放
	- eK: `startVideo`
	- eV: `{video: String}`

* 预加载失败（不包括延时情况），弹出切换提示
	- eK: `videoLoadFailed`
	- eV: `{video: String}`

* 预加载失败，请求七牛API成功返回
	- eK: `getQiniuResSuccess`
	- eV: `{video: String, resTime: Number}`

* 预加载失败，请求七牛API返回失败
	- eK: `getQiniuResFailure`
	- eV: `{video: String, error: String}`

* 预加载延时，弹出切换提示
	- eK: `videoLoadDeffered`
	- eV: `{video: String}`

* 视频播放过程中卡顿发生，弹出切换提示  
	注意：用户拖动后的加载不在本类
	- eK: `videoLagged`
	- eV: `{video: String, timeStamp: Number, cause: String]}`

* 视频播放卡顿后再次playThrough  
	注意：用户拖动后的playThrough亦在本类
	- eK: `resumePlaying`
	- eV: `{video: String, timeStamp: Number}`  

* 视频播放切换提示，用户选择“切换低清"
	- eK: `clickSwitchLowResolution`
	- category: `site`
	- eV: `{video: String, videoUrl: String, timeStamp: Number}`

* 视频播放切换提示，用户选择”刷新页面“
	- eK: `clickRefreshVideoPage`
	- category: `site`
	- eV: `{video: String, videoUrl: String, timeStamp: Number}`

* 视频播放完成，用户startEmpower前，以及没有巩固题的视频在video end时
	- eK: `finishVideo`

* 视频播放器，用户点击音量按钮开/关静音
	- eK: `clickToggleMute`
	- eV: `{video: String, muted: Boolean}`
	
* 视频播放器，用户点击分享图标，弹出下拉
	- eK: `clickShareVideoDropdown`
	- category: `site`
	- eV: `{video: String, timeStamp: String}`

Problem类埋点 - 不完全重构
--

* Schema
	* 所有problem类埋点的eventValue里加problemIndex字段，值为一个非负整数，用来记录用户专题或挑战的问题序号
	* 所有专题类问题埋点的eventValue里加remainedLife字段，值是一个非负整数，用来记录用户答此题目前的剩余生命值
