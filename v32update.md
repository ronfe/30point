Event Track Update v3.2 (web/app)
--

Note: 新增埋点如无说明，默认`category`为`site`

### Web

* ```enterOuterPage``` 的```eventValue```加上```subject```。若用户进入物理外循环页，则```subject: "physics"```，否则```subject: null```

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

* ```enterChapterListPage``` 的```eventValue```加上```subject```。若用户进入物理外循环页，则```subject: "physics"```，否则```subject: null```

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

