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


### 教师线使用手册

**使用手册-进入使用指南**

---

* ```eventKey: enterTeacherGuide```
* ```category: site```

**使用手册-进入第一屏**

---

* ```eventKey: enterFirstGuide```
* ```category: site```

**使用手册第一屏-查看课程内容**

---

使用手册，点击“查看课程内容”

* ```eventKey: clickGuideCourseContent```
* ```category: site```

**使用手册第一屏-让学生加入**

---

使用手册第一屏，点击“让学生加入”

* ```eventKey: clickGuide1InviteStudents```
* ```category: site```

**使用手册-进入第二屏**

---

* ```eventKey: enterSecondGuide```
* ```category: site```

**使用手册第二屏-认知节奏感视频**

---

使用手册第二屏，点击“认知节奏感”视频

* ```eventKey: clickGuide2FirstVideo```
* ```category: site```

**使用手册第二屏-抽象概念可视化视频**

---

使用手册第二屏，点击“抽象概念可视化”视频

* ```eventKey: clickGuide2SecondVideo```
* ```category: site```

**使用手册第二屏-趣味性视频**

---

使用手册第二屏，点击“趣味性”视频

* ```eventKey: clickGuide2ThirdVideo```
* ```category: site```

**使用手册第二屏-查看趣味视频**

---

使用手册第二屏，点击“查看趣味视频”按钮

* ```eventKey: clickGuideFeaturedVideo```
* ```category: site```

**使用手册第二屏-让学生加入**

---

使用手册第二屏，点击“让学生加入”

* ```eventKey: clickGuide1InviteStudents```
* ```category: site```

**使用手册-进入第三屏**

---

* ```eventKey: enterThirdGuide```
* ```category: site```

**使用手册第三屏-查看专题训练**

---

使用手册第三屏，点击“查看专题训练”

* ```eventKey: clickGuideProblemSet```
* ```category: site```

**使用手册第三屏-点击专题标签**

---

使用手册第三屏，点击任何专题标签

* ```eventKey: clickGuideProblemSetTab```
* ```category: site```

**使用手册第三屏-让学生加入**

---

使用手册第三屏，点击“让学生加入”

* ```eventKey: clickGuide3InviteStudents```
* ```category: site```

**使用手册-进入第四屏**

---

* ```eventKey: enterFourthGuide```
* ```category: site```

**使用手册第四屏-查看班级数据**

---

使用手册第四屏，点击“查看班级数据”

* ```eventKey: clickGuideRoomData```
* ```category: site```

**使用手册第四屏-让学生加入**

---

使用手册第四屏，点击“让学生加入”

* ```eventKey: clickGuide4InviteStudents```
* ```category: site```

**使用手册-进入第五屏**

---

* ```eventKey: enterFifthGuide```
* ```category: site```

**使用手册第五屏-北大附中案例预览**

---

使用手册第五屏，点击“北大附中案例预览”

* ```eventKey: clickGuide5FirstView```
* ```category: site```

**使用手册第五屏-北大附中案例下载**

---

使用手册第五屏，点击“北大附中案例下载”

* ```eventKey: clickGuide5FirstDownload```
* ```category: site```

**使用手册第五屏-三十五中案例预览**

---

使用手册第五屏，点击“三十五中案例预览”

* ```eventKey: clickGuide5SecondView```
* ```category: site```

**使用手册第五屏-三十五中案例下载**

---

使用手册第五屏，点击“三十五中案例下载”

* ```eventKey: clickGuide5SecondDownload```
* ```category: site```

**使用手册第五屏-人大附中案例预览**

---

使用手册第五屏，点击“人大附中案例预览”

* ```eventKey: clickGuide5ThirdView```
* ```category: site```

**使用手册第五屏-人大附中案例下载**

---

使用手册第五屏，点击“人大附中案例下载”

* ```eventKey: clickGuide5ThirdDownload```
* ```category: site```

**使用手册第五屏-十一学校案例预览**

---

使用手册第五屏，点击“十一学校案例预览”

* ```eventKey: clickGuide5FourthView```
* ```category: site```

**使用手册第五屏-十一学校案例下载**

---

使用手册第五屏，点击“十一学校案例下载”

* ```eventKey: clickGuide5FourthDownload```
* ```category: site```

**使用手册-进入第六屏**

---

* ```eventKey: enterSixthGuide```
* ```category: site```

**使用手册第六屏-创建班级**

---

使用手册第六屏，点击“创建班级”

* ```eventKey: clickGuideCreateClassroom```
* ```category: site```
