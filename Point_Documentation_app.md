# v3.0 Points Documentation (APP)

by ronfe  
Last Modified: 15DEC03  

本文档基于产品埋点需求文档 v151030 之埋点描述，适用于3.0 Mobile App端埋点。  

## 学习模块    

**点击学习模块**  

---

知识点滑动页，点击进入课前学习时触发。

* ```eventKey: startLearning```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 进入状态 ```state: String, enum: ['success', 'fail']```

**开始播放视频**  

---

视频页，视频加载并开始播放。

* ```eventKey: startVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```

**暂停视频**  

---

视频播放时，用户点击暂停按钮。  
视频所有时间戳均为毫秒数。

* ```eventKey: pauseVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 用户暂停时的时间戳 ```pauseTime: Number```

**恢复播放视频**  

---

用户暂停视频后，再次点击播放按钮。

* ```eventKey: resumeVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 用户点击播放按钮时的时间戳 ```resumeTime: ISODate```

**分享视频**  

---

视频播放时，用户点击右上角视频按钮。

* ```eventKey: shareVideo```
* ```category: site```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - （未载于埋点文档）用户分享平台 ```sharePlatform: String enum: ["qq", "qzone", "weibo", "wechatIM", "wechatShare", 'tencentWeibo']```

**视频交互**  

---

视频播放页面，用户回答视频交互题。

* ```eventKey: answerVideoInteraction```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 交互ID ```interactionId: ObjectId```
  - 用户答案 ```answer: String```

**拖动视频**  

---

视频播放页面，用户拖动视频进度条。

* ```eventKey: dragVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 拖动方向 ```dragDirection: String enum: ['backward', 'forward']```
  - 拖动时视频时间戳 ```fromTimeStamp: TimeStamp```
  - 拖动至视频时间戳 ```toTimeStamp: TimeStamp```

**完成视频**  

---

用户完成观看视频。

* ```eventKey: finishVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```


**退出学习模块**  

---

（适用于多视频学习模块）视频完成页，用户中途退出视频。

* ```eventKey: quitLearning```
* ```category: course```
* 必传字段：
  - 退出视频模块前所完成的视频ID ```videoId: ObjectId```
  - 所退出的学习模块知识点ID ```topicId: ObjectId```

**弹窗后选择视频**  

---

（适用于用户完成学习模块）知识点滑动页，点击“进入学习模块”，弹出选择视频页面，用户选择某一视频。

* ```eventKey: chooseFinishedVideo```
* ```category: site```
* 必传字段：
  - 知识ID ```topicId: ObjectId```
  - 所选择的视频ID ```videoId: ObjectId```

**完成学习模块**  

---

用户完成视频，弹出视频完成页面。

* ```eventKey: completeLearning```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```

**退出视频**  

---

视频播放页，用户中途退出视频。

* ```eventKey: quitVideo```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 退出时的视频时间戳 ```quitTimeStamp: TimeStamp```

**点击缓存**  

---

视频播放页面，点击缓存按钮。

* ```eventKey: clickBuffer```
* ```category: site```
* 必传字段：
  - 视频ID ```videoId: ObjectId```

**点击开始缓存**  

---

知识点滑动页，点击右上角缓存按钮。

* ```eventKey: startBuffer```
* ```category: site```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 缓存视频数量 ```bufferVideos: Number```
  - 缓存视频ID列表 ```videoList: [ObjectId]```

**缓存成功**  

---

知识点滑动页，点击缓存后视频成功缓存。

* ```eventKey: bufferSuccess```
* ```category: site```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 缓存视频列表 ```videoId: ObjectId```

**缓存失败**  

---

知识点滑动页，点击缓存后视频缓失败。

* ```eventKey: bufferFailure```
* ```category: site```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 缓存视频列表 ```videoId: ObjectId```
  - 缓存失败原因 ```errorMessage: String```

## 练习模块

**点击练习模块**  

---

知识点滑动页，点击进入课后练习按钮。

* ```eventKey: startMaster```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 进入状态 state: ```String, enum: ['success', 'fail']```

**开始专题**  

---

专题引导页，点击“开始专题”。

* ```eventKey: startProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 所在专题ID ```problemSetId: ObjectId```

**开始挑战**  

---

挑战引导页，点击“开始挑战”。

* ```eventKey: startChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```

**退出专题**  

---

专题页，点击左上角退出按钮。

* ```eventKey: quitProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 所在专题ID ```problemSetId: ObjectId```
 
**退出挑战**  

---

挑战页，点击左上角退出按钮。

* ```eventKey: quitChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```

**进入题目**  

---

题目页，题目打开。

* ```eventKey: enterProblem```
* ```category: problem```
* 必传字段：
  - 问题ID ```problemId: ObjectId```

**答题**  

---

专题或挑战页，开始选择选项（选择）或开始输入第一个字符（填空）。

* ```eventKey: answerProblem```
* ```category: problem```
* 必传字段：
  - 问题ID ```problemId: ObjectId```
  - 用户选择选项 ```userChoice: String```

**修改选项**  

---

（仅用于选择题）题目页，用户重新选择选项。

* ```eventKey: modifyChoice```
* ```category: problem```
* 必传字段：
  - 问题ID ```problemId: ObjectId```
  - 用户新选择选项 ```userChoice: String```

**提交答案**  

---

题目页，用户点击提交按钮。

* ```eventKey: submitAnswer```
* ```category: problem```
* 必传字段：
  - 问题ID ```problemId: ObjectId```
  - 用户选择选项 ```answer: String```
  - 用户选择正误 ```correctness: Boolean```

**视频讲解**  

---

题目页，用户点击视频讲解按钮。

* ```eventKey: clickExpVideo```
* ```category: problem```
* 必传字段：
  - 专题ID ```problemSetId: ObjectId```
  - 问题ID ```problemId: ObjectId```
  - 题目状态 ```problemState: String enum: ['answering', 'correct', 'incorrect']```

**进入下一题**  

---

题目页，用户点击继续按钮。

* ```eventKey: clickNextProblem```
* ```category: site```
* 必传字段：
  - 当前问题ID ```problemId: ObjectId```

**退出题目**  

---

题目页，点击左上角退出按钮。

* ```eventKey: quitProblem```
* ```category: problem```
* 必传字段：
  - 所在知识点ID ```topicId: ObjectId```
  - 所在专题ID ```problemSetId: ObjectId```
  - 所在层数 ```layer: String```
  - 所在题目ID ```problemId: ObjectId```

**专题失败**  

---

专题页，用户未通过专题。

* ```eventKey: problemSetFailure```
* ```category: course```
* 必传字段：
  - 专题ID ```problemSetId: ObjectId```

**专题通过**  

---

专题页，用户通过专题。

* ```eventKey: problemSetSuccess```
* ```category: course```
* 必传字段：
  - 专题ID ```problemSetId: ObjectId```

**挑战失败**  

---

挑战页，用户未通过挑战。

* ```eventKey: challengeFailure```
* ```category: course```
* 必传字段：
  - 知识点ID ```topicId: ObjectId```

**挑战通过**  

---

挑战页，用户通过挑战。

* ```eventKey: challengeSuccess```
* ```category: course```
* 必传字段：
  - 知识点ID ```topicId: ObjectId```

**完成练习模块**  

---

用户完成专题及挑战，弹出练习完成页面。

* ```eventKey: completeMaster```
* ```category: course```
* 必传字段：
  - 知识点ID ```topicId: ObjectId```

**弹窗后选择专题**  

---

（适用于用户完成练习模块专题）知识点滑动页，点击“进入练习模块”，弹出选择专题页面，用户选择某一专题。

* ```eventKey: chooseFinishedProblemSet```
* ```category: site```
* 必传字段：
  - 知识ID ```topicId: ObjectId```
  - 所选择的专题ID ```problemSetId: ObjectId```

**弹窗后选择挑战**  

---

（适用于用户完成练习模块专题）知识点滑动页，点击“进入练习模块”，弹出选择专题页面，用户选择挑战。

* ```eventKey: chooseFinishedChallenge```
* ```category: site```
* 必传字段：
  - 知识ID ```topicId: ObjectId```

## 外循环

**点击打开某章节**

---

外循环页，用户点击打开某章节按钮。

* ```eventKey: startChapter```
* ```category: site```
* 必传字段：
	- 章节ID ```chapterId: ObjectId```

**点击进入知识点**

---

外循环页，用户打开章节按钮并点击某一知识点（非引入视频）按钮。

* ```eventKey: enterTopic```
* ```category: site```
* 必传字段：
	- 知识点ID `topicId: ObjectId`
	- 进入状态 ```state: String, enum: ['success', 'fail']```

**点击进入观看引入视频**

---

外循环页，用户打开章节并点击章节引入视频按钮。

* ```eventKey: startGuideVideo```
* ```category: site```
* 必传字段：
	- 章节ID `chapterId: Object`
	- 进入状态 ```state: String, enum: ['success', 'fail']```

**进入个人中心**

---

任意位置，用户点击”我的“。

* ```eventKey: enterMyProfile```
* ```category: site```


**进入设置**

---

任意位置，用户点击”设置“。

* ```eventKey: enterSetting```
* ```category: site```


## 新用户、登录相关

**进入引导页**  

---

打开应用进入引导页。

* ```eventKey: enterGuidePage```
* ```category: site```

**立即使用**[tested]  

---

引导页，用户点击“立即使用”。

* ```eventKey: clickExperience```
* ```category: site```

**引导页-点击"注册或登录"**  

---

引导页，选择‘注册或登录’[tested]

* ```eventKey: clickUserLogBtn```
* ```category: site```

**登录-点击忘记密码**  

---

登录页，用户点击‘忘记密码’。

* ```eventKey: clickForgetPassword```
* ```category: site```

**登录-登录**  

---

登录页，用户点选“登录”。

* ```eventKey: clickLoginBtn```
* ```category: site```

**登录-登录成功**  

---

登录页，用户成功登录。

* ```eventKey: loginSuccess```
* ```category: site```

**登录-登录失败**  

---

登录页，用户登录失败。

* ```eventKey: loginFailure```
* ```category: site```
* 必传字段：
  - 失败原因 ```errorMessage: String```

**登录-QQ登录**  [tested]

---

登录页，用户点选“QQ账号登录”。

* ```eventKey: loginQQ```
* ```category: site```

**登录-QQ登录成功**  

---

登录页，用户通过QQ成功登录。

* ```eventKey: qqLoginSuccess```
* ```category: site```

**登录-QQ登录失败**  

---

登录页，用户通过QQ登录失败。

* ```eventKey: qqLoginFailure```
* ```category: site```
* 必传字段：
  - 失败原因 ```errorMessage: String```

**登录-切换至注册**  

---

登录页，用户点选“注册新用户”。

* ```eventKey: switchRegister```
* ```category: site```


**注册-进入注册页面**  

---

注册页，注册页面打开。

* ```eventKey: enterSignupPage```
* ```category: site```

**登录-进入登录页面**  

---

注册页，注册页面打开。

* ```eventKey: enterLoginPage```
* ```category: site```

**注册-切换至登录**  

---

注册页，用户选择”立即登录“按钮。

* ```eventKey: switchLogin```
* ```category: site```

**注册-完成注册**  

---

注册页，用户点选“完成注册”。

* ```eventKey: clickSignupBtn```
* ```category: site```

**注册-注册成功**  

---

注册页，用户注册成功。

* ```eventKey: registSuccess```
* ```category: site```

**注册-注册失败**  

---

注册页，用户注册失败。

* ```eventKey: registFailure```
* ```category: site```
* 必传字段：
  - 失败原因 ```errorMessage: String```

**未登录完成-以后再说**  

---

未登录完成页，用户选择”以后再说“按钮。

* ```eventKey: clickLogLater```
* ```category: site```
* 必传字段：
  - 知识点ID ```topicId: ObjectId```
  - 模块类型 ```type: String, enum: ['learning', 'practice']```

**未登录完成-登录**  

---

未登录完成页，用户选择”登录“按钮。

* ```eventKey: clickLoginNow```
* ```category: site```
* 必传字段：
  - 知识点ID ```topicId: ObjectId```
  - 模块类型 ```type: String, enum: ['learning', 'practice']```

## 设置

**点击切换教材**  

---

设置页，用户选择”教材“。

* ```eventKey: clickSwitchBook```
* ```category: site```

**切换教材成功**  

---

设置页，用户选择”教材“并选择后切换成功。

* ```eventKey: switchBookSuccess```
* ```category: site```
* 必传字段：
  - 用户所选的教材ID ```newBookId: ObjectId```

**切换年级**  

---

设置页，用户选择”年级“，并选择其一。

* ```eventKey: switchGrage```
* ```category: site```
* 必传字段：
  - 用户所选的年级ID ```newGradeId: ObjectId```

**更改网络环境设置**  

---

设置页，用户更改”使用2G/3G/4G网络“开关。

* ```eventKey: switchNetworkConfig```
* ```category: site```
* 必传字段：
  - 用户更改后的开关状态 ```networkConfig: Boolean```

**分享**  

---

设置页，用户选择”分享“。

* ```eventKey: clickShareApp```
* ```category: site```
* 必传字段：
  - （未载于埋点文档）用户分享平台 sharePlatform: String enum: ["qq", "qzone", "weibo", "wechatIM", "wechatShare", 'tencentWeibo']

**评分**  

---

（适用于iOS应用）设置页，用户选择”给洋葱数学评分“。

* ```eventKey: clickRateApp```
* ```category: site```

**消息推送**  

---

设置页，用户更改”消息推送“开关。

* ```eventKey: switchNotification```
* ```category: site```
* 必传字段：
  - 用户更改后的开关状态 ```notificationConfig: Boolean```

**用户反馈**  

---

设置页，用户选择”用户反馈“。

* ```eventKey: clickFeedback```
* ```category: site```

**用户发送反馈**  

---

设置页，用户选择”用户反馈“后点击“发送”。

* ```eventKey: sendFeedback```
* ```category: site```

**缓存管理**  

---

设置页，用户选择”缓存管理“。

* ```eventKey: clickBufferManagement```
* ```category: site```

**缓存管理-点击编辑**  

---

设置页，用户进入缓存管理，点击”编辑“。

* ```eventKey: clickEditBuffer```
* ```category: site```

**缓存管理-点击全选**  

---

设置页，用户进入缓存管理，点击编辑，再点击”全选“。

* ```eventKey: clickBufferSelectAll```
* ```category: site```

**缓存管理-点击删除**  

---

设置页，用户进入缓存管理，点击编辑，再点击”删除“。

* ```eventKey: clickBufferDel```
* ```category: site```

**缓存管理-点击“正在下载”**  

---

缓存管理页，用户点击“正在下载视频”。

* ```eventKey: clickBufferingZone```
* ```category: site```

**下载中缓存管理-点击暂停**  

---

下载中缓存管理页，点击”暂停“。

* ```eventKey: clickBufferingPause```
* ```category: site```

**下载中缓存管理-点击恢复**  

---

下载中缓存管理页，点击”恢复“。

* ```eventKey: clickBufferingResume```
* ```category: site```

**下载中缓存管理-点击编辑**  

---

下载中缓存管理页，点击”编辑“。

* ```eventKey: clickEditBuffering```
* ```category: site```

**下载中缓存管理-点击全选**  

---

下载中缓存管理页，点击编辑，再点击”全选“。

* ```eventKey: clickBufferingSelectAll```
* ```category: site```

**下载中缓存管理-点击删除**  

---

下载中缓存管理页，点击编辑，再点击”删除“。

* ```eventKey: clickBufferingDel```
* ```category: site```


**退出登录**  

---

设置页，用户点击个人头像，选择”退出登录“。

* ```eventKey: clickLogout```
* ```category: site```

**变更目标**  

---

我的页，选择”我的目标“并成功变更。

* ```eventKey: changePersonalGoal```
* ```category: site```
* 必传字段
  - 用户变更后的目标 ```newGoal: String, enum: ['standard', 'advanced']```
 
**进入商店**  

---

我的页，用户选择”洋葱商店“。

* ```eventKey: enterShop```
* ```category: site```

**兑换头像**  

---

我的页，用户进入洋葱商店，兑换任一头像。

* ```eventKey: changeProfileAvatar```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID ```newAvatarId: ObjectId```

**兑换头像成功**  

---

我的页，用户进入洋葱商店，兑换任一头像，并成功兑换。

* ```eventKey: changeProfileAvatarSuccess```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID ```newAvatarId: ObjectId```
