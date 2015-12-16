# v3.0 Points Documentation (PC)

by ronfe  
Last Modified: 15DEC16 

本文档基于产品埋点需求文档 v151030 之埋点描述，适用于3.0 PC端埋点。  

## 首页、登录、注册、新手引导

**进入首页**[tested]

---

进入首页

* ```eventKey: enterHome```
* ```category: site```

**切换教师版**[tested]

---

首页，点击“教师版”按钮

* ```eventKey: switchTeacherHome```
* ```category: site```

**切换学生版**[tested]

---

首页，点击“学生版”按钮

* ```eventKey: switchStudentHome```
* ```category: site```

**首页-点击登录**[tested]

---

首页，点击“登录”按钮

* ```eventKey: clickLoginBtn```
* ```category: site```

**首页-点击注册**[tested]

---

首页，点击“注册”按钮

* ```eventKey: clickSignupBtn```
* ```category: site```

**学生首页-免费使用**[tested]

---

学生版首页第一屏，点击“免费使用”

* ```eventKey: clickFreeForUseSS```
* ```category: site```

**学生首页-应用下载**[tested]

---

学生版首页第一屏，点击“应用下载”

* ```eventKey: clickDownloadApp```
* ```category: site```

**学生首页-观看视频**[tested]

---

学生版首页第二屏，点击“点击观看”

* ```eventKey: clickWatchingVideoSample```
* ```category: site```

**学生首页-iOS下载**[tested]

---

学生版首页末屏，点击“下载iOS版”

* ```eventKey: clickDownloadIosSS```
* ```category: site```

**学生首页-安卓下载**[tested]

---

学生版首页末屏，点击“下载Android版”

* ```eventKey: clickDownloadAndoridSS```
* ```category: site```

**学生首页-Windows下载**[tested]

---

学生版首页末屏，点击“下载Windows版”

* ```eventKey: clickDownloadWindowsSS```
* ```category: site```

**教师首页-看看微课**[tested]

---

教师版首页第一屏，点击“看看微课”

* ```eventKey: clickHaveALook```
* ```category: site```

**教师首页-免费使用**[tested]

---

教师版首页第一屏，点击“免费使用”

* ```eventKey: clickFreeForUseTC```
* ```category: site```

**教师首页-引入视频**[tested]

---

教师版首页第二屏全章引入视频，点击“点击观看”

* ```eventKey: clickWatchGuideVideo```
* ```category: site```

**教师首页-基础视频**[tested]

---

教师版首页第二屏基础视频，点击“点击观看”

* ```eventKey: clickWatchElementaryVideo```
* ```category: site```

**教师首页-提高视频**[tested]

---

教师版首页第二屏提高视频，点击“点击观看”

* ```eventKey: clickWatchAdvancedVideo```
* ```category: site```

**教师首页-详情点击**[pending]

---

教师版首页第四屏，点击“详情点击”

* ```eventKey: clickLearnMoreLink```
* ```category: site```

**教师首页-请戳**[pending]

---

教师版首页第四屏，点击“请戳”

* ```eventKey: clickClickMe```
* ```category: site```

**教师首页-iOS下载**[tested]

---

教师版首页末屏，点击“下载iOS版”

* ```eventKey: clickDownloadIosTC```
* ```category: site```

**教师首页-安卓下载**[tested]

---

教师版首页末屏，点击“下载Android版”

* ```eventKey: clickDownloadAndroidTC```
* ```category: site```

**教师首页-Windows下载**[tested]

---

教师版首页末屏，点击“下载Windows版”

* ```eventKey: clickDownloadWindowsTC```
* ```category: site```

**登录页-进入登录页**[tested]

---

进入登录页

* ```eventKey: enterLoginPage```
* ```category: site```

**登录页-忘记密码**[tested]

---

登录页，点击“忘记密码？”

* ```eventKey: clickForgetPasswd```
* ```category: site```

**登录页-QQ登录**[tested]

---

登录页，点击“QQ账号登录”

* ```eventKey: loginQQ```
* ```category: site```

**登录页-登录成功**[tested]

---

登录页，用户登录成功 (此埋点发送GA)

* ```eventKey: loginSuccess```
* ```category: site```

**登录页-未登录活跃**

---

用户无需登录即进入循环。(此埋点发送GA)

* ```eventKey: userVigoured```
* ```category: site```

**登录页-批量创建用户激活**[tested]

---

登录页，批量创建用户首次登录。（此埋点发送GA）

* ```eventKey: userActivate```
* ```category: site```

**登录页-登录失败**[tested]

---

登录页，用户登录失败

* ```eventKey: loginFailure```
* ```category: site```
* 必传字段：
  - 登录失败原因  ```errorMessage: String```

**注册页-进入注册页面**[tested]

---

进入注册页

* ```eventKey: enterSignupPage```
* ```category: site```

**注册页-选择学生**[tested]

---

注册页，选择“我是学生”

* ```eventKey: chooseStudentRole```
* ```category: site```

**注册页-选择老师**[pending]

---

注册页，选择“我是老师”

* ```eventKey: chooseTeacherRole```
* ```category: site```

**注册页-注册成功**[tested]

---

注册页，用户注册成功 （此埋点发送GA）

* ```eventKey: signupSuccess```
* ```category: site```

**注册页-注册失败**[tested]

---

注册页，用户注册失败

* ```eventKey: signupFailure```
* ```category: site```

**新手引导页-跳过**[tested]

---

新手引导页，跳过新手引导

* ```eventKey: chooseSkipNewbieGuide```
* ```category: site```

**新手引导页-开始**[tested]

---

新手引导页，开始新手引导

* ```eventKey: chooseStartNewbieGuide```
* ```category: site```

**新手引导页-观看视频**[tested]

---

新手引导页，开始观看视频

* ```eventKey: startNewbieGuideVideo```
* ```category: site```

**新手引导页-提交答案**[tested]

---

新手引导页，提交问题答案

* ```eventKey: submitNewbieGuideAnswer```
* ```category: site```

**新手引导页-选择教材**[tested]

---

新手引导页，成功选择教材

* ```eventKey: chooseNewbieBook```
* ```category: site```
* 必传字段：
  - 所选择的教材版本ID  ```bookId: ObjectId```

**新手引导页-选择年级**[tested]

---

新手引导页，成功选择年级

* ```eventKey: chooseNewbieGrade```
* ```category: site```
* 必传字段：
  - 所选择的的年级ID  ```gradeId: ObjectId```

**新手引导页-选择目标**[pending]

---

新手引导页，成功选择目标

* ```eventKey: chooseNewbieTarget```
* ```category: site```
* 必传字段：
  - 所选择的的目标  ```target: String, enum: ['standard', 'advanced']```

**新手引导页-完成**[tested]

---

新手引导页，完成新手引导

* ```eventKey: finishNewbieGuide```
* ```category: site```

## 外循环

**外循环页-我的学习**[tested]

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

**学习模块-完成学习**  

---

完成学习模块，弹出完成页面。

* ```eventKey: completeLearning```
* ```category: course```
* 必传字段：
 - 所在知识点ID topicId: ObjectId


## 练习模块

**练习模块-开始专题**[tested]

---

在练习模块页，点击“开始专题”

* ```eventKey: startProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-开始挑战**[tested]

---

在练习模块页，点击“开始挑战“

* ```eventKey: startChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-退出专题**[tested]

---

关闭退出某个专题

* ```eventKey: quitProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-退出挑战**[tested]

---

关闭退出某个挑战

* ```eventKey: quitChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-中止专题**[tested]

---

专题题目页，用户退出某个专题

* ```eventKey: terminateProblemSet```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```
  - 所在专题ID  ```problemSetId: ObjectId```

**练习模块-中止挑战**[tested]

---

挑战题目页，退出挑战

* ```eventKey: terminateChallenge```
* ```category: course```
* 必传字段：
  - 所在知识点ID  ```topicId: ObjectId```

**练习模块-进入题目**[pending]

---

进入某一题目

* ```eventKey: enterProblem```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```

**练习模块-答题**[tested]

---

开始答题(开始选择选项（选择）或开始输入第一个字符（填空）)

* ```eventKey: answerProblem```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```

**练习模块-修改**[tested]

---

答题过程中修改选择题选项(仅限于选择题)

* ```eventKey: modifyChoice```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```

**练习模块-提交答案**[tested]

---

题目页，用户点击提交按钮

* ```eventKey: submitAnswer```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 用户选择选项  ```userChoice: String```
  - 用户选择正误  ```correctness: Boolean```

**练习模块-查看解析**[tested]

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

**练习模块-选择错因**[tested]

---

题目页，选择错因

* ```eventKey: reasonOfMistake```
* ```category: problem```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```
  - 所选的错误原因 ```mistakeReason: String```

**练习模块-继续到下一题**[tested]

---

题目页，用户点击继续按钮

* ```eventKey: clickNextProblem```
* ```category: site```
* 必传字段：
  - 题目ID  ```problemId: ObjectId```

**练习模块-专题失败**[pending]

---

专题页，用户未通过专题

* ```eventKey: problemSetFailure```
* ```category: course```
* 必传字段：
  - 专题ID  ```problemSetId: ObjectId```
  - 是否为重复完成 ```isRepeated: Boolean```

**练习模块-专题通过**[tested]

---

专题页，用户通过专题

* ```eventKey: problemSetSuccess```
* ```category: course```
* 必传字段：
  - 专题ID  ```problemSetId: ObjectId```
  - 是否为重复完成 ```isRepeated: Boolean```

**练习模块-挑战失败**[pending]

---

专题页，用户未通过挑战

* ```eventKey: challengeFailure```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```
  - 是否为重复完成 ```isRepeated: Boolean```

**练习模块-挑战通过**[tested]

---

专题页，用户通过挑战

* ```eventKey: challengeSuccess```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```
  - 是否为重复完成 ```isRepeated: Boolean```

**练习模块-完成练习模块**[tested]

---

用户完成专题及挑战，弹出练习完成页面

* ```eventKey: completeMaster```
* ```category: course```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```
