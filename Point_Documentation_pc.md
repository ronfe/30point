# v3.0 Points Documentation (PC)

by ronfe  
Last Modified: 15NOV24  

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

登录页，用户登录成功

* ```eventKey: loginSuccess```
* ```category: site```

**登录页-登录失败**

---

登录页，用户登录失败

* ```eventKey: loginFailure```
* ```category: site```
* 必传字段：
  - 登录失败原因  ```String```

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

注册页，用户注册成功

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

**外循环页-打开章节**

---

外循环页，打开某章节

* ```eventKey: startChapter```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**外循环页-进入知识点**

---

外循环页，打开章节并点击某一知识点（非引入视频）

* ```eventKey: enterTopic```
* ```category: site```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**外循环页-引入视频**

---

外循环页，打开章节并点击引入视频

* ```eventKey: startGuideVideo```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**外循环页-商店**

---

外循环页，点击商店图标

* ```eventKey: enterShop```
* ```category: site```

**外循环页-兑换头像**

---

商店页，点击任一头像“兑换”

* ```eventKey: changeProfileAvatar```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID  ```newAvatarId: ObjectId```

**外循环页-兑换头像成功**

---

商店页，成功兑换头像

* ```eventKey: changeProfileAvatarSuccess```
* ```category: site```
* 必传字段：
  - 用户兑换之头像ID  ```newAvatarId: ObjectId```

**外循环页-关注我们**

---

外循环页，点击“关注我们”区域任一按钮

* ```eventKey: clickFollowUs```
* ```category: site```
* 必传字段：
  - 用户所关注的社交媒体  ```followPlatform: String, enum: ['qqGroup', 'wechat', 'weibo']```

**外循环页-目标**

---

外循环页，设定（或更改）每周目标

* ```eventKey: changePersonalGoal```
* ```category: site```
* 必传字段：
  - 用户变更后的目标  ```newGoal: String, enum: ['standard', 'advanced']```
