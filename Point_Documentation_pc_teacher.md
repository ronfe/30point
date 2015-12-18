# v3.0 Points Documentation (PC-Teacher)

by ronfe  
Last Modified: 15DEC16 

本文档基于产品埋点需求文档 v151030 之埋点描述，适用于3.0 PC端埋点（教师线）。  


## 教师端

**教师端后台首页-点击创建班级**[tested]

---

用户单击创建班级button (Pending Test)

* ```eventKey: createClassroom```
* ```category: site```

**教师端后台首页-进入创建班级弹窗**[tested]

---

弹出创建班级的弹窗（Pending Test）

* ```eventKey: enterCreateClassroomModal```
* ```category: site```

**教师端后台首页-弹窗内确认创建班级**[tested]

---

在弹窗内点击“确认创建” (Pending Test)

* ```eventKey: confirmCreateClassroom```
* ```category: site```

**教师端后台首页-弹窗内取消创建班级**[tested]

---

在弹窗内取消创建班级 (Pending Test)

* ```eventKey: cancelCreateClassroom```
* ```category: site```

**教师端后台首页-创建班级成功**[tested]

---

成功创建了一个班级 (Pending Test)

* ```eventKey: createClassroomSuccess```
* ```category: site```

**教师端后台首页-进入创建班级成功的弹窗**[tested]

---

创建班级成功后进入"创建班级成功！"的弹窗 (Pending Test)

* ```eventKey: enterCreateClassroomSuccessModal```
* ```category: site```

**教师端后台首页-前往添加学生**[tested]

---

创建班级成功后，单击“前往添加学生” (Pending Test)

* ```eventKey: clickInstantInsertStudent```
* ```category: site```

**教师端后台首页-取消添加学生**[tested]

---

创建班级成功后，单击“取消” (Pending Testing)

* ```eventKey: clickCancelInstantInsertStudent```
* ```category: site```

**教师端后台首页-查看班级**[tested]

---

查看当前班级状态(Pending Test)

* ```eventKey: checkClassroomStat```
* ```category: site```

**教师端后台首页-示例班级说明**

---

查看示例班级说明(问号)

* ```eventKey: checkExampleClassroom```
* ```category: site```

**班级数据-进入班级数据**[tested]

---

点击某个班级进入班级数据页面（Pending Testing）

* ```eventKey: enterClassroomInfo```
* ```category: site```

**班级数据-选择年级**[tested]

---

选择某个年级 (Pending Test)

* ```eventKey: selectGrade```
* ```category: site```
* 必传字段：
  - 年级ID  ```gradeId: ObjectId```

**班级数据-选择章节** [tested]

---

选择某个年级旁的某个章节 (Pending Test)

* ```eventKey: selectChapter```
* ```category: site```
* 必传字段：
  - 章节ID  ```chapterId: ObjectId```

**班级数据-选择知识点**[tested]

---

选择某个知识点 (Pending Test)

* ```eventKey: selectTopic```
* ```category: site```
* 必传字段：
  - 知识点ID  ```topicId: ObjectId```

**班级数据-查看完成名单**[tested]

---

查看各个知识点的完成名单 (Pending Test)

* ```eventKey: checkTopicCompleteList```
* ```category: site```

**班级数据-查看视频**[tested]

---

查看某个视频 (Pending Test)

* ```eventKey: checkVideo```
* ```category: site```

**班级数据-查看习题**[tested]

---

查看某一习题 (Pending Test)

* ```eventKey: checkProblem```
* ```category: site```

**班级数据-展开题目**

---

打开一条题目 (Pending Test)

* ```eventKey: openOneProblem```
* ```category: site```

**班级数据-收起题目**

---

收起某一条题目 (Pending Test)

* ```eventKey: closeOneProblem```
* ```category: site```

**班级数据-查看更多错题**

---

查看更多错题

* ```eventKey: checkMoreMistakes```
* ```category: site```

**班级管理-进入班级管理**[tested]

---

进入班级管理页 (Pending Test)

* ```eventKey: enterClassAdmin```
* ```category: site```

**班级管理-开始批量添加**[tested]

---

无学生班级管理页，点击“开始批量添加”(Pending Test)

* ```eventKey: adminBatchInsert```
* ```category: site```

**班级管理-引导学生注册**[tested]

---

无学生班级管理页，点击“引导学生注册”(Pending Test)

* ```eventKey: adminNaturalInsert```
* ```category: site```

**班级管理-添加学生**[tested]

---

点击“添加学生”图标(Pending Test)

* ```eventKey: clickAddStuIntoClassroom```
* ```category: site```

**班级管理-查看更多功能（三个竖点）**[tested]

---

点击“查看更多功能”图标 (Pending Test)

* ```eventKey: clickMoreFeatures```
* ```category: site```

**班级管理-备注姓名**[tested]

---

在班级管理页内，学生列表中给学生添加或修改“学生姓名”并确认 (Pending Test)

* ```eventKey: changeStuNameNote```
* ```category: site```

**班级管理-重置密码**[tested]

---

在班级管理页内，学生列表中修改学生的密码，单击钥匙图标，并在弹窗中点“确认重置” (Pending Test)

* ```eventKey: changeStuPassword```
* ```category: site```

**班级管理-移出学生**[tested]

---

在班级管理页内，把学生从学生列表中移除，单击垃圾桶图标，并在弹窗中点“确认移出” (Pending Test)

* ```eventKey: removeStuFromClassroom```
* ```category: site```

**班级管理-生成账号列表**[tested]

---

点击...，点“生成账号列表” (Pending Test)

* ```eventKey: createClassroomMemberList```
* ```category: site```

**班级管理-编辑班级名称**[tested]

---

点击...，点“编辑班级名称” (Pending Test)

* ```eventKey: modifyClassroomName```
* ```category: site```

**班级管理-确认修改班级名称**[tested]

---

确认给班级改名 (Pending Test)

* ```eventKey: confirmModifyClassroomName```
* ```category: site```

**班级管理-解散班级**[tested]

---

点击...，点“解散班级” (Pending Test)

* ```eventKey: disbandClassroom```
* ```category: site```

**班级管理-确认解散班级**[tested]

---

确认解散整个班级 (Pending Test)

* ```eventKey: confirmDisbandClassroom```
* ```category: site```

**添加学生流程-开始批量添加**[tested]

---

添加学生页面, 点击“开始批量添加” (Pending Test)

* ```eventKey: initBatchInsert```
* ```category: site```

**添加学生流程-引导学生注册**[tested]

---

添加学生页面, 点击“引导学生注册” (Pending Test)

* ```eventKey: initNaturalInsert```
* ```category: site```

**添加学生流程-拖拽添加人数控制条**[tested]

---

拖动控制条 (Pending Test)

* ```eventKey: dragInsertStuStripe```
* ```category: site```
* 必传字段：
  - 用户拖动终点数字  ```dragIndicator: Number```

**添加学生流程-输入添加人数**[tested]

---

直接输入班级人数 (Pending Test)

* ```eventKey: inputInsertStuNum```
* ```category: site```
* 必传字段：
  - 用户输入数字  ```inputIndicator: Number```

**添加学生流程-确认添加**[tested]

---

确认添加学生 (Pending Test)

* ```eventKey: confirmInsertStu```
* ```category: site```

**添加学生流程-进入批量添加学生成功页面**[tested]

---

批量添加学生成功 (Pendint Test)

* ```eventKey: batchInsertSuccess```
* ```category: site```

**添加学生流程-创建账号列表**[tested]

---

批量添加学生成功页面，点击“创建账号列表” (Pending Test)

* ```eventKey: createStuList```
* ```category: site```

**添加学生流程-进入账号列表**[tested]

---

承接上一步进入账号列表页 (Pending Test)

* ```eventKey: enterStuListPage```
* ```category: site```

**添加学生流程-下载账号列表**[tested]

---

在“账号列表页”单击下载 (Pending Test)

* ```eventKey: downloadStuList```
* ```category: site```

**添加学生流程-打印账号列表**[tested]

---

在“账号列表页”单击打印 (Pending Test)

* ```eventKey: printStuList```
* ```category: site```

**添加学生流程-加入班级指南**[tested]

---

引导学生注册页，点击“加入班级指南” (Pending Test)

* ```eventKey: clickNaturalInsertGuide```
* ```category: site```


**添加学生流程-进入注册指南**[tested]

---

引导学生注册页，确认加入班级指南后跳转页面打开 (Pending Test)

* ```eventKey: enterNaturalListPage```
* ```category: site```

**添加学生流程-打印注册指南**[tested]

---

引导学生注册页，确认加入班级指南后跳转页面打开，点击“打印”(Pending Test)

* ```eventKey: printNaturalList```
* ```category: site```

**添加学生流程-下载注册指南**[tested]

---

引导学生注册页，确认加入班级指南后跳转页面打开，点击“下载”(Pending Test)

* ```eventKey: downloadNaturalList```
* ```category: site```

**内循环-进入创建班级弹窗**[tested]

---

无班级教师内循环，点击“让学生加入”(Pending Test)

* ```eventKey: clickBannerInsert```
* ```category: site```

**内循环-创建班级弹窗-确认创建班级**[tested]

---

在弹窗内点击“确认创建”(Pending Test)

* ```eventKey: confirmBannerCreateClassroom```
* ```category: site```

**内循环-创建班级弹窗-取消**[tested]

---

在弹窗内取消创建班级(Pending Test)

* ```eventKey: cancelBannerCreateClassroom```
* ```category: site```

**内循环-进入创建班级成功弹窗**[tested]

---

创建班级成功后进入"创建班级成功！"的弹窗(Pending Test)

* ```eventKey: enterBannerCreateClassroomSuccessModal```
* ```category: site```

**内循环-创建班级成功弹窗-前往添加学生**[pending]

---

创建班级成功后，单击“前往添加学生”(Pending Test)

* ```eventKey: clickBannerInstantInsertStudent```
* ```category: site```

**内循环-创建班级成功弹窗-取消**[tested]

---

创建班级成功后，单击“取消”(Pending Test)

* ```eventKey: clickBannerCancelInstantInsertStudent```
* ```category: site```


### 教师线使用手册

**使用手册-进入使用指南** [tested]

---

* ```eventKey: enterTeacherGuide```
* ```category: site```

~~**使用手册-进入第一屏**~~

---

* ```eventKey: enterFirstGuide```
* ```category: site```

**使用手册第一屏-查看课程内容**[tested]

---

使用手册，点击“查看课程内容” (Pending Test)

* ```eventKey: clickGuideCourseContent```
* ```category: site```

**使用手册第一屏-让学生加入**[tested]

---

使用手册第一屏，点击“让学生加入” (Pending Test)

* ```eventKey: clickGuide1InviteStudents```
* ```category: site```

~~**使用手册-进入第二屏**~~

---

* ```eventKey: enterSecondGuide```
* ```category: site```

**使用手册第二屏-认知节奏感视频**

---

使用手册第二屏，点击“认知节奏感”视频 (Pending Test)

* ```eventKey: clickGuide2ThirdVideo```
* ```category: site```

**使用手册第二屏-抽象概念可视化视频**

---

使用手册第二屏，点击“抽象概念可视化”视频 (Pending Test)

* ```eventKey: clickGuide2FirstVideo```
* ```category: site```

**使用手册第二屏-趣味性视频**

---

使用手册第二屏，点击“趣味性”视频 (Pending Test)

* ```eventKey: clickGuide2SecondVideo```
* ```category: site```

**使用手册第二屏-查看趣味视频**[tested]

---

使用手册第二屏，点击“查看趣味视频”按钮 (Pending Test)

* ```eventKey: clickGuideFeaturedVideo```
* ```category: site```

**使用手册第二屏-让学生加入**[tested]

---

使用手册第二屏，点击“让学生加入” (Pending Test)

* ```eventKey: clickGuide2InviteStudents```
* ```category: site```

~~**使用手册-进入第三屏**~~

---

* ```eventKey: enterThirdGuide```
* ```category: site```

**使用手册第三屏-查看专题训练**[tested]

---

使用手册第三屏，点击“查看专题训练” (Pending Test)

* ```eventKey: clickGuideProblemSet```
* ```category: site```

**使用手册第三屏-点击专题标签**[tested]

---

使用手册第三屏，点击任何专题标签 (Pending Test)

* ```eventKey: clickGuideProblemSetTab```
* ```category: site```

**使用手册第三屏-让学生加入**[tested]

---

使用手册第三屏，点击“让学生加入” (Pending Test)

* ```eventKey: clickGuide3InviteStudents```
* ```category: site```

~~**使用手册-进入第四屏**~~

---

* ```eventKey: enterFourthGuide```
* ```category: site```

**使用手册第四屏-查看班级数据**[pending]

---

使用手册第四屏，点击“查看班级数据” (Pending Test)

* ```eventKey: clickGuideRoomData```
* ```category: site```

**使用手册第四屏-让学生加入**[tested]

---

使用手册第四屏，点击“让学生加入” (Pending Test)

* ```eventKey: clickGuide4InviteStudents```
* ```category: site```

~~**使用手册-进入第五屏**~~

---

* ```eventKey: enterFifthGuide```
* ```category: site```

**使用手册第五屏-北大附中案例预览**[tested]

---

使用手册第五屏，点击“北大附中案例预览” (Pending Test)

* ```eventKey: clickGuide5FirstView```
* ```category: site```

**使用手册第五屏-北大附中案例下载**[tested]

---

使用手册第五屏，点击“北大附中案例下载” (Pending Test)

* ```eventKey: clickGuide5FirstDownload```
* ```category: site```

**使用手册第五屏-三十五中案例预览**[tested]

---

使用手册第五屏，点击“三十五中案例预览” (Pending Test)

* ```eventKey: clickGuide5SecondView```
* ```category: site```

**使用手册第五屏-三十五中案例下载**[pending]

---

使用手册第五屏，点击“三十五中案例下载” (Pending Test)

* ```eventKey: clickGuide5SecondDownload```
* ```category: site```

**使用手册第五屏-人大附中案例预览**[tested]

---

使用手册第五屏，点击“人大附中案例预览” (Pending Test)

* ```eventKey: clickGuide5ThirdView```
* ```category: site```

**使用手册第五屏-人大附中案例下载**[tested]

---

使用手册第五屏，点击“人大附中案例下载” (Pending Test)

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

~~**使用手册-进入第六屏**~~

---

* ```eventKey: enterSixthGuide```
* ```category: site```

**使用手册第六屏-创建班级**[tested]

---

使用手册第六屏，点击“创建班级” (Pending Test)

* ```eventKey: clickGuideCreateClassroom```
* ```category: site```
