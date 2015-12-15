# v3.0 Points Documentation (PC)

by ronfe  
Last Modified: 15DEC14 

本文档基于产品埋点需求文档 v151030 之埋点描述，适用于3.0 PC端埋点。  

## 首页、登录、注册、新手引导

**进入首页**

---

进入首页

* ```eventKey: enterHome```
* ```category: site```

**切换教师版**

---

首页，点击“教师版”按钮

* ```eventKey: switchTeacherHome```
* ```category: site```

**切换学生版**

---

首页，点击“学生版”按钮

* ```eventKey: switchStudentHome```
* ```category: site```

**首页-点击登录**

---

首页，点击“登录”按钮

* ```eventKey: clickLoginBtn```
* ```category: site```

**首页-点击注册**

---

首页，点击“注册”按钮

* ```eventKey: clickSignupBtn```
* ```category: site```

**学生首页-免费使用**

---

学生版首页第一屏，点击“免费使用”

* ```eventKey: clickFreeForUseSS```
* ```category: site```

**学生首页-应用下载**

---

学生版首页第一屏，点击“应用下载”

* ```eventKey: clickDownloadApp```
* ```category: site```

**学生首页-观看视频**

---

学生版首页第二屏，点击“点击观看”

* ```eventKey: clickWatchingVideoSample```
* ```category: site```

**学生首页-iOS下载**

---

学生版首页末屏，点击“下载iOS版”

* ```eventKey: clickDownloadIosSS```
* ```category: site```

**学生首页-安卓下载**

---

学生版首页末屏，点击“下载Android版”

* ```eventKey: clickDownloadAndoridSS```
* ```category: site```

**学生首页-Windows下载**

---

学生版首页末屏，点击“下载Windows版”

* ```eventKey: clickDownloadWindowsSS```
* ```category: site```

**教师首页-看看微课**

---

教师版首页第一屏，点击“看看微课”

* ```eventKey: clickHaveALook```
* ```category: site```

**教师首页-免费使用**

---

教师版首页第一屏，点击“免费使用”

* ```eventKey: clickFreeForUseTC```
* ```category: site```

**教师首页-引入视频**

---

教师版首页第二屏全章引入视频，点击“点击观看”

* ```eventKey: clickWatchGuideVideo```
* ```category: site```

**教师首页-基础视频**

---

教师版首页第二屏基础视频，点击“点击观看”

* ```eventKey: clickWatchElementaryVideo```
* ```category: site```

**教师首页-提高食品**

---

教师版首页第二屏提高视频，点击“点击观看”

* ```eventKey: clickWatchAdvancedVideo```
* ```category: site```

**教师首页-详情点击**

---

教师版首页第四屏，点击“详情点击”

* ```eventKey: clickLearnMoreLink```
* ```category: site```

**教师首页-请戳**

---

教师版首页第四屏，点击“请戳”

* ```eventKey: clickClickMe```
* ```category: site```

**教师首页-iOS下载**

---

教师版首页末屏，点击“下载iOS版”

* ```eventKey: clickDownloadIosTC```
* ```category: site```

**教师首页-安卓下载**

---

教师版首页末屏，点击“下载Android版”

* ```eventKey: clickDownloadAndroidTC```
* ```category: site```

**教师首页-Windows下载**

---

教师版首页末屏，点击“下载Windows版”

* ```eventKey: clickDownloadWindowsTC```
* ```category: site```

**登录页-进入登录页**

---

进入登录页

* ```eventKey: enterLoginPage```
* ```category: site```

**登录页-忘记密码**

---

登录页，点击“忘记密码？”

* ```eventKey: clickForgetPasswd```
* ```category: site```

**登录页-QQ登录**

---

登录页，点击“QQ账号登录”

* ```eventKey: clickQQLogin```
* ```category: site```

**登录页-登录成功**

---

登录页，用户登录成功 (此埋点发送GA)

* ```eventKey: loginSuccess```
* ```category: site```

**登录页-未登录活跃**

---

用户无需登录即进入循环。(此埋点发送GA)

* ```eventKey: userVigoured```
* ```category: site```

**登录页-批量创建用户激活**

---

登录页，批量创建用户首次登录。（此埋点发送GA）

* ```eventKey: userActivate```
* ```category: site```

**登录页-登录失败**

---

登录页，用户登录失败

* ```eventKey: loginFailure```
* ```category: site```
* 必传字段：
  - 登录失败原因  ```errorMessage: String```

**注册页-进入注册页面**

---

进入注册页

* ```eventKey: enterSignupPage```
* ```category: site```

**注册页-选择学生**

---

注册页，选择“我是学生”

* ```eventKey: chooseStudentRole```
* ```category: site```

**注册页-选择老师**

---

注册页，选择“我是老师”

* ```eventKey: chooseTeacherRole```
* ```category: site```

**注册页-注册成功**

---

注册页，用户注册成功 （此埋点发送GA）

* ```eventKey: signupSuccess```
* ```category: site```

**注册页-注册失败**

---

注册页，用户注册失败

* ```eventKey: signupFailure```
* ```category: site```

**新手引导页-跳过**

---

新手引导页，跳过新手引导

* ```eventKey: chooseSkipNewbieGuide```
* ```category: site```

**新手引导页-开始**

---

新手引导页，开始新手引导

* ```eventKey: chooseStartNewbieGuide```
* ```category: site```

**新手引导页-观看视频**

---

新手引导页，开始观看视频

* ```eventKey: startNewbieGuideVideo```
* ```category: site```

**新手引导页-提交答案**

---

新手引导页，提交问题答案

* ```eventKey: submitNewbieGuideAnswer```
* ```category: site```

**新手引导页-选择教材**

---

新手引导页，成功选择教材

* ```eventKey: chooseNewbieBook```
* ```category: site```
* 必传字段：
  - 所选择的教材版本ID  ```bookId: ObjectId```

**新手引导页-选择年级**

---

新手引导页，成功选择年级

* ```eventKey: chooseNewbieGrade```
* ```category: site```
* 必传字段：
  - 所选择的的年级ID  ```gradeId: ObjectId```

**新手引导页-选择目标**

---

新手引导页，成功选择目标

* ```eventKey: chooseNewbieTarget```
* ```category: site```
* 必传字段：
  - 所选择的的目标  ```target: String, enum: ['standard', 'advanced']```

**新手引导页-完成**

---

新手引导页，完成新手引导

* ```eventKey: finishNewbieGuide```
* ```category: site```

## 外循环

**外循环页-我的学习**

---

外循环页导航栏，点击“我的学习”

* ```eventKey: clickMyLearning```
* ```category: site```

**外循环页-错题本**

---

外循环页导航栏，点击“错题本”

* ```eventKey: clickMistackLog```
* ```category: site```

**外循环页-打开章节**[tested]

---

外循环页，打开某章节

* ```eventKey: startChapter```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**外循环页-进入知识点**[tested]

---

外循环页，打开章节并点击某一知识点（非引入视频）

* ```eventKey: enterTopic```
* ```category: site```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**外循环页-引入视频**[tested]

---

外循环页，打开章节并点击引入视频

* ```eventKey: startGuideVideo```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**外循环页-商店**[tested]

---

外循环页，点击商店图标

* ```eventKey: enterShop```
* ```category: site```

**外循环页-兑换头像**[tested]

---

商店页，点击任一头像“兑换”

* ```eventKey: changeProfileAvatar```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID  ```newAvatarId: ObjectId```

**外循环页-兑换头像成功**[tested]

---

商店页，成功兑换头像

* ```eventKey: changeProfileAvatarSuccess```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID  ```newAvatarId: ObjectId```

**外循环页-关注我们**[tested]

---

外循环页，点击“关注我们”区域任一按钮

* ```eventKey: clickFollowUs```
* ```category: site```
* 必传字段：
  - 用户所关注的社交媒体  ```followPlatform: String, enum: ['qqGroup', 'wechat', 'weibo']```

**外循环页-目标**[tested]

---

外循环页，设定（或更改）每周目标

* ```eventKey: changePersonalGoal```
* ```category: site```
* 必传字段：
  - 用户变更后的目标  ```newGoal: String, enum: ['standard', 'advanced']```

**设置-外循环切换教材**[tested]

---

设置页，用户选择教材

* ```eventKey: clickSwitchBook```
* ```category: site```

**外循环-切换教材成功**[tested]

---

外循环页，用户选择教材并切换成功

* ```eventKey: switchBookSuccess```
* ```category: site```
* 必传字段：
  - 用户所选的教材ID ```newBookId: ObjectId```

**设置-外循环切换年级**[tested]

---

设置页，用户选择”年级“，并选择其一

* ```eventKey: clickSwitchGrade```
* ```category: site```

**设置-切换年级成功**[tested]

---

外循环或设置页，用户选择年级并切换成功

* ```eventKey: switchGradeSuccess```
* ```category: site```
* 必传字段：
  - 用户选择年级ID  ```newGradeId: ObjectId```

**设置-进入个人中心**[tested]

---

用户进入个人中心

* ```eventKey: enterMyProfile```
* ```category: site```

**设置-退出登录**[tested]

---

用户点击退出登录

* ```eventKey: clickLogout```
* ```category: site```

**设置-进入密码修改**[tested]

---

用户点击密码修改

* ```eventKey: clickModifyPassword```
* ```category: site```

**设置-成功修改密码**[tested]

---

进入密码修改后，完成修改过程，成功修改密码

* ```eventKey: modifyPasswordSuccess```
* ```category: site```

**设置-进入我的班级**[tested]

---

进入设置页内的我的班级

* ```eventKey: enterMyClassroom```
* ```category: site```

**设置-成功加入班级**

---

成功加入某一班级

* ```eventKey: joinClassSuccess```
* ```category: site```

**设置-加入班级失败**

---

加入班级失败

* ```eventKey: joinClassFailed```
* ```category: site```
* 必传字段：
  - 失败原因  ```joinClassFailedReason: String```

**设置-进入社交账户绑定**[tested]

---

点击“立即绑定”

* ```eventKey: clickBindSocial```
* ```category: site```
* 必传字段：
  - 绑定第三方名  ```bindPlatform: String, enum: ['qq']```

**设置-成功绑定**

---

第三方成功绑定账户

* ```eventKey: clickBindSuccess```
* ```category: site```

**设置-邮箱添加或变更**[tested]

---

个人资料页添加或变更邮箱

* ```eventKey: changeMailAddress```
* ```category: site```

**设置-手机号添加或变更**[tested]

---

个人资料页添加或变更手机号

* ```eventKey: changePhoneNum```
* ```category: site```

**设置-姓名添加或变更**[tested]

---

个人资料页添加或变更姓名

* ```eventKey: changeUserName```
* ```category: site```

**设置-性别添加或变更**[tested]

---

个人资料页添加或变更性别

* ```eventKey: changeGender```
* ```category: site```
* 必传字段：
  - 更改后的性别  ```newGender: String enum:['male','female']```

**设置-点击查找学校**[tested]

---

个人资料页点击"查找学校"

* ```eventKey: clickFindSchool```
* ```category: site```

**设置-选中一个学校**[tested]

---

点击查找学校后，弹出选项中选中了某一学校

* ```eventKey: findSchoolSuccess```
* ```category: site```
* 必传字段：
  - 选中学校ID  ```newSchoolId: ObjectId```

**设置-点击“没有我的学校”**[tested]

---

点击了没有我的学校

* ```eventKey: mySchoolNotExist```
* ```category: site```

**设置-输入学校名称**[tested]

---

没有学校用户自己新建的学校
埋点测试Mark: 点击保存后触发

* ```eventKey: enterSchoolName```
* ```category: site```
* 必传字段：
  - 新的学校ID  ```newSchoolId: ObjectId```

**设置-保存更改**[tested]

---

修改个人资料后保存

* ```eventKey: saveChangedProfile```
* ```category: site```

## 知识点页

**知识点页-点击学习模块**[pending]

---

知识点页视频讲解，点击“进入”

* ```eventKey: startLearning```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-点击练习模块**[pending]

---

进入某个练习模块

* ```eventKey: startMaster```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

## 学习模块

**视频页-开始**[tested]

---

视频页，视频加载并开始播放

* ```eventKey: startVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```

**视频页-暂停**[tested]

---

视频页，点击暂停按钮

* ```eventKey: pauseVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 用户暂停时的视频时间戳（毫秒单位，下同）  ```pauseTime: Number```

**视频页-恢复**[tested]

---

视频页，暂停视频后，再次点击播放

* ```eventKey: resumeVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 用户点击播放时的视频时间戳  ```resumeTime: Number```

**视频页-回退**[tested]

---

视频页，点击"倒回10秒前"

* ```eventKey: rollbackVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 用户回退前所在的视频时间戳  ```fromTimeStamp: Number```

**视频页-全屏**[tested]

---

视频页，点击“全屏”按钮

* ```eventKey: toggleFullSize```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 全屏方向（全屏为true，取消全屏为false） ```direction: Boolean```
  - 点击全屏按钮时视频时间戳 ```fromTimeStamp: Number```

**视频页-分享**

---

视频页，点击视屏右上角分享按钮并选择某个分享平台

* ```eventKey: shareVideo```
* ```category: site```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 用户分享平台(QQ/QQ空间/微博/微信/微信朋友圈/腾讯微博)  ```sharePlatform: String, enum: ['qq', 'qzone', "weibo", "wechatIM", "wechatShare", 'tencentWeibo']```

**视频页-交互**[tested]

---

视频页，用户完成交互题

* ```eventKey: answerVideoInteraction```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 交互题ID  ```interactionId: ObjectId```
  - 交互点弹出时刻  ```startTime: ISODate```
  - 用户答案  ```answer: String```

**视频页-拖动**[pending]

---

视频页，用户拖动进度条。由左向右为forward，由右向左为backward．

* ```eventKey: dragVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 拖动方向  ```dragDirection: String, enum: ['backward', 'forward']```
  - 拖动时视频时间戳  ```fromTimeStamp: Number```
  - 拖动至视频时间戳  ```toTimeStamp: Number```

**视频页-开始巩固**[tested]

---

视频页，巩固页面开始

* ```eventKey: startEmpower```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```

**视频页-巩固题开始**[tested]

---

视频页，巩固题目开始。

* ```eventKey: startEmpowerProblem```
* ```category: video```
* 必传字段：
  - 视频ID ```videoId: ObjectId```
  - 巩固题ID ```problemId: ObjectId```

**视频页-回答巩固题**[tested]

---

视频页，回答巩固题目

* ```eventKey: submitEmpower```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 巩固题ID  ```problemId: ObjectId```
  - 用户选择  ```choice: String```
  - 正误  ```correctness: Boolean```

**视频页-完成**[pending]

---

视频页，完成视频。

* ```eventKey: finishVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```

**视频页-退出**[pending]

---

视频页，中途退出视频

* ```eventKey: quitVideo```
* ```category: video```
* 必传字段：
  - 视频ID  ```videoId: ObjectId```
  - 退出时的视频时间戳  ```quitTimeStamp: Number```

**学习模块-中断学习**[tested]

---

视频完成页，退出学习模块

* ```eventKey: quitLearning```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 最后完成视频ID  ```videoId: ObjectId```

## 练习模块

**练习模块-开始专题**

---

在练习模块页，点击“开始专题”

* ```eventKey: startProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-开始挑战**

---

在练习模块页，点击“开始挑战“

* ```eventKey: startChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-退出专题**

---

关闭退出某个专题

* ```eventKey: quitProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-退出挑战**

---

关闭退出某个挑战

* ```eventKey: quitChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-中止专题**

---

专题题目页，用户退出某个专题

* ```eventKey: terminateProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-退出挑战**

---

挑战题目页，退出挑战

* ```eventKey: terminateChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-进入题目**

---

进入某一题目

* ```eventKey: enterProblem```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```

**练习模块-答题**

---

开始答题(开始选择选项（选择）或开始输入第一个字符（填空）)

* ```eventKey: answerProblem```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```

**练习模块-修改**

---

答题过程中修改选择题选项(仅限于选择题)

* ```eventKey: modifyChoice```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```

**练习模块-提交答案**

---

题目页，用户点击提交按钮

* ```eventKey: submitAnswer```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```
  - 用户选择正误  ```correctness: Boolean```

**练习模块-查看解析**

---

用户点击查看解析

* ```eventKey: showAnswer```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```
  - 题目状态  ```problemState: String enum: ['answering', 'correct', 'incorrect']```

**练习模块-视频讲解**

---

题目页，用户点击视频讲解按钮

* ```eventKey: clickExpVideo```
* ```category: problem```
* 必传字段：
  - 专题ID  ```problemSetId: ObjectId```
  - 问题ID  ```problemId: ObjectId```
  - 题目状态  ```problemState: String enum: ['answering', 'correct', 'incorrect']```

**练习模块-选择错因**

---

题目页，选择错因

* ```eventKey: reasonOfMistake```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 所选的错误原因 ```mistakeReason: String```

**练习模块-继续到下一题**

---

题目页，用户点击继续按钮

* ```eventKey: clickNextProblem```
* ```category: site```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```

**练习模块-专题失败**

---

专题页，用户未通过专题

* ```eventKey: problemSetFailure```
* ```category: course```
* 必传字段：
  - 专题ID  ```problemSetId: ObjectId```

**练习模块-专题通过**

---

专题页，用户通过专题

* ```eventKey: problemSetSuccess```
* ```category: course```
* 必传字段：
  - 专题ID  ```problemSetId: ObjectId```

**练习模块-挑战失败**

---

专题页，用户未通过挑战

* ```eventKey: challengeFailure```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**练习模块-挑战通过**

---

专题页，用户通过挑战

* ```eventKey: challengeSuccess```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**练习模块-完成练习模块**

---

用户完成专题及挑战，弹出练习完成页面

* ```eventKey: completeMaster```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

## 教师端

**教师端后台首页-点击创建班级**

---

用户单击创建班级button

* ```eventKey: createClassroom```
* ```category: site```

**教师端后台首页-进入创建班级弹窗**

---

弹出创建班级的弹窗

* ```eventKey: enterCreateClassroomModal```
* ```category: site```

**教师端后台首页-弹窗内确认创建班级**

---

在弹窗内点击“确认创建”

* ```eventKey: confirmCreateClassroom```
* ```category: site```

**教师端后台首页-弹窗内取消创建班级**

---

在弹窗内取消创建班级

* ```eventKey: cancelCreateClassroom```
* ```category: site```

**教师端后台首页-创建班级成功**

---

成功创建了一个班级

* ```eventKey: createClassroomSuccess```
* ```category: site```

**教师端后台首页-进入创建班级成功的弹窗**

---

创建班级成功后进入"创建班级成功！"的弹窗

* ```eventKey: enterCreateClassroomSuccessModal```
* ```category: site```

**教师端后台首页-前往添加学生**

---

创建班级成功后，单击“前往添加学生”

* ```eventKey: clickInstantInsertStudent```
* ```category: site```

**教师端后台首页-取消添加学生**

---

创建班级成功后，单击“取消”

* ```eventKey: clickCancelInstantInsertStudent```
* ```category: site```

**教师端后台首页-查看班级**

---

查看当前班级状态

* ```eventKey: checkClassroomStat```
* ```category: site```

**教师端后台首页-示例班级说明**

---

查看示例班级说明(问号)

* ```eventKey: checkExampleClassroom```
* ```category: site```

**班级数据-进入班级数据**

---

点击某个班级进入班级数据页面

* ```eventKey: enterClassroomInfo```
* ```category: site```

**班级数据-选择年级**

---

选择某个年级

* ```eventKey: selectGrade```
* ```category: site```
* 必传字段：
  - 年级ID  ```gradeId: ObjectId```

**班级数据-选择章节**

---

选择某个年级旁的某个章节

* ```eventKey: selectChapter```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**班级数据-选择知识点**

---

选择某个知识点

* ```eventKey: selectTopic```
* ```category: site```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**班级数据-查看完成名单**

---

查看各个知识点的完成名单

* ```eventKey: checkTopicCompleteList```
* ```category: site```

**班级数据-查看视频**

---

查看某个视频

* ```eventKey: checkVideo```
* ```category: site```

**???班级数据-查看习题**

---

查看某一习题

* ```eventKey: checkProblem```
* ```category: site```

**班级数据-展开题目**

---

打开一条题目

* ```eventKey: openOneProblem```
* ```category: site```

**班级数据-收起题目**

---

收起某一条题目

* ```eventKey: closeOneProblem```
* ```category: site```

**班级数据-查看更多错题**

---

查看更多错题

* ```eventKey: checkMoreMistakes```
* ```category: site```

**班级管理-进入班级管理**

---

进入班级管理页

* ```eventKey: enterClassAdmin```
* ```category: site```

**班级管理-开始批量添加**

---

无学生班级管理页，点击“开始批量添加”

* ```eventKey: adminBatchInsert```
* ```category: site```

**班级管理-引导学生注册**

---

无学生班级管理页，点击“开始批量添加”

* ```eventKey: adminNaturalInsert```
* ```category: site```

**班级管理-添加学生**

---

点击“添加学生”图标

* ```eventKey: clickAddStuIntoClassroom```
* ```category: site```

**班级管理-查看更多功能（三个竖点）**

---

点击“查看更多功能”图标

* ```eventKey: clickMoreFeatures```
* ```category: site```

**班级管理-备注姓名**

---

在班级管理页内，学生列表中给学生添加或修改“学生姓名”

* ```eventKey: changeStuNameNote```
* ```category: site```

**班级管理-重置密码**

---

在班级管理页内，学生列表中修改学生的密码，单击钥匙图标，并在弹窗中点“确认重置”

* ```eventKey: changeStuPassword```
* ```category: site```

**班级管理-移出学生**

---

在班级管理页内，把学生从学生列表中移除，单击垃圾桶图标，并在弹窗中点“确认移出”

* ```eventKey: removeStuFromClassroom```
* ```category: site```

**班级管理-生成账号列表**

---

点击...，点“生成账号列表”

* ```eventKey: createClassroomMemberList```
* ```category: site```

**班级管理-编辑班级名称**

---

点击...，点“编辑班级名称”

* ```eventKey: modifyClassroomName```
* ```category: site```

**班级管理-确认修改班级名称**

---

确认给班级改名

* ```eventKey: confirmModifyClassroomName```
* ```category: site```

**班级管理-解散班级**

---

点击...，点“解散班级”

* ```eventKey: disbandClassroom```
* ```category: site```

**班级管理-确认解散班级**

---

确认解散整个班级

* ```eventKey: confirmDisbandClassroom```
* ```category: site```

**添加学生流程-开始批量添加**

---

添加学生页面, 点击“开始批量添加”

* ```eventKey: initBatchInsert```
* ```category: site```

**添加学生流程-引导学生注册**

---

添加学生页面, 点击“引导学生注册”

* ```eventKey: initNaturalInsert```
* ```category: site```

**添加学生流程-拖拽添加人数控制条**

---

拖动控制条

* ```eventKey: dragInsertStuStripe```
* ```category: site```
* 必传字段：
  - 用户拖动终点数字  ```dragIndicator: Number```

**添加学生流程-输入添加人数**

---

直接输入班级人数

* ```eventKey: inputInsertStuNum```
* ```category: site```
* 必传字段：
  - 用户输入数字  ```inputIndicator: Number```

**添加学生流程-确认添加**

---

确认添加学生

* ```eventKey: confirmInsertStu```
* ```category: site```

**添加学生流程-进入批量添加学生成功页面**

---

批量添加学生成功

* ```eventKey: createClassroomSuccess```
* ```category: site```

**添加学生流程-创建账号列表**

---

批量添加学生成功页面，点击“创建账号列表”

* ```eventKey: createStuList```
* ```category: site```

**添加学生流程-进入账号列表**

---

承接上一步进入账号列表页

* ```eventKey: enterStuListPage```
* ```category: site```

**添加学生流程-下载账号列表**

---

在“账号列表页”单击下载

* ```eventKey: downloadStuList```
* ```category: site```

**添加学生流程-打印账号列表**

---

在“账号列表页”单击打印

* ```eventKey: printStuList```
* ```category: site```

**添加学生流程-加入班级指南**

---

引导学生注册页，点击“加入班级指南”

* ```eventKey: clickNaturalInsertGuide```
* ```category: site```

**添加学生流程-设置班级人数——拖拽控制条**

---

引导学生注册页，点击“加入班级指南”并在弹窗中拖拽控制条

* ```eventKey: dragNaturalInsertStripe```
* ```category: site```
* 必传字段：
  - 用户拖动终点数字  ```dragIndicator: Number```

**添加学生流程-设置班级人数——输入框**

---

引导学生注册页，点击“加入班级指南”并在弹窗中填入数字

* ```eventKey: inputNaturalInsertNum```
* ```category: site```
* 必传字段：
  - 用户输入数字  ```inputIndicator: Number```

**添加学生流程-确认设置班级人数**

---

引导学生注册页，点击“加入班级指南”并在弹窗中点击确认

* ```eventKey: confirmNaturalInsert```
* ```category: site```

**添加学生流程-进入注册指南**

---

引导学生注册页，确认加入班级指南后跳转页面打开

* ```eventKey: enterNaturalListPage```
* ```category: site```

**添加学生流程-打印注册指南**

---

引导学生注册页，确认加入班级指南后跳转页面打开，点击“打印”

* ```eventKey: printNaturalList```
* ```category: site```

**添加学生流程-下载注册指南**

---

引导学生注册页，确认加入班级指南后跳转页面打开，点击“下载”

* ```eventKey: downloadNaturalList```
* ```category: site```

**内循环-进入创建班级弹窗**

---

无班级教师内循环，点击“让学生加入”

* ```eventKey: clickBannerInsert```
* ```category: site```

**内循环-创建班级弹窗-确认创建班级**

---

在弹窗内点击“确认创建”

* ```eventKey: confirmBannerCreateClassroom```
* ```category: site```

**内循环-创建班级弹窗-取消**

---

在弹窗内取消创建班级

* ```eventKey: cancelBannerCreateClassroom```
* ```category: site```

**内循环-进入创建班级成功弹窗**

---

创建班级成功后进入"创建班级成功！"的弹窗

* ```eventKey: enterBannerCreateClassroomSuccessModal```
* ```category: site```

**内循环-创建班级成功弹窗-前往添加学生**

---

创建班级成功后，单击“前往添加学生”

* ```eventKey: clickBannerInstantInsertStudent```
* ```category: site```

**内循环-创建班级成功弹窗-取消**

---

创建班级成功后，单击“取消”

* ```eventKey: clickBannerCancelInstantInsertStudent```
* ```category: site```
