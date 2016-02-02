Tacking Events Changelog (PC/Web v3.1.5) 待续
--

注：页面位置以PRD序号为准
保留原注册登录逻辑中的全部埋点

### 外页

* 进入2.10页面
    - `enterQQUserChooseIdentity`

* 2.10页面，点击“老用户”
    - `clickChooseExistedUser`

* 2.10页面，点击“新用户”
    - `clickChooseNewUser`

* 2.10页面，点击“下一步”
    - `clickQQUserIdentityNext`

* 进入2.12页面
    - `enterQQNewUserRoleSelection`

* 2.12页面，点击“老师”
    - `clickQQNewUserChooseTeacher`

* 2.12页面，点击“学生”
    - `clickQQNewUserChooseStudent`

* 2.12页面，点击“下一步”
    - `clickQQNewUserRoleNext`

* 进入2.11页面
    - `enterQQOldUserBind`

* 2.11页面，点击“忘记密码”
    - `clickQQOldUserForgetPasswd`

* 2.11页面，点击“立即绑定”
    - `clickQQOldUserBindAccount`

* 2.11页面，点击“立即绑定”后，绑定成功
    - `clickQQOldUserBindSuccess`

* 2.11页面，点击“立即绑定”后，绑定失败
    - `clickQQOldUserBindFailure`
    - `{error: String}`

* 2.11页面，点击“放弃绑定”
    - `clickQQOldUserAbortBinding`

* 2.11页面，点击“放弃绑定”后，在弹窗中选择“继续绑定”
    - `clickQQOldUserContinueBinding`

* 2.11页面，点击“放弃绑定”后，在弹窗中选择“放弃绑定”
    - `clickQQOldUserConfirmAbort`

* 

##PC端个人中心
注:默认保留原个人中心中的全部埋点,如果有重复、冲突埋点，默认保留原埋点


* 3.1 修改邮箱
	- `modifyEmailInMyProfile`
* 3.1 修改手机号
	- `modifyPhoneInMyProfile`
* 3.1 修改昵称
 	- `modifyNicknameInMyProfile`
* 3.1 修改姓名
  	- `modifyNameInMyProfile`
* 3.1 修改学校
  	- `modifySchoolInMyProfile`
* 3.1 修改年级
  	- `modifyGradeInMyProfile`
* 3.2 邮箱格式错误(如果之前有埋，保留原埋点)
	- `enterWrongEmailInMyProfile`
* 3.2 手机号码格式错误
	- `enterWrongPhoneNumberInMyProfile`
* 3.3 邮箱占用
	- `dupMailInMyProfile`
* 3.3 手机号占用
	- `dupPhoneNumberInMyProfile`
* 0.2 进入个人资料页发现没有设置密码的弹窗
	- `nonePasswordAlertInMyProfile`
* 0.2 弹窗中单击 以后再说
	- `setPassWordNextTimeAlertInMyProfile`
* 0.2 弹窗中单击 去设置密码
	- `clickEnterSetPasswordAlertInMyProfile`
* 3.4 个人资料设置成功“保存成功”弹窗
	- `saveSuccessAlertInMyProfile`
* 3.4 个人资料设置成功“保存成功”弹窗 单击”确定“
	- `clickOkInSaveSuccessAlertInMyProfile`
* 3.5 修改资料后未保存去往其它页面时，弹出“修改尚未保存页”
	- `notSaveChangeAlertInMyProfile`
* 3.5 “修改尚未保存页” 单击不保存
	- `clickNotSaveChangeAlertInMyProfile`
* 3.5 “修改尚未保存页” 单击"保存修改"
	- `clickSaveChangeAlertInMyProfile`

## PC 个人中心密码管理部分
注： 默认优先保留之前埋点


* 3.6 进入密码管理页
	- `enterModifyPasswordPage`

其余埋点保留之前所有的

## PC个人中心社交账户绑定
注： 默认优先保留之前埋点

* 3.10 进入社交账绑定页
	- `enterBindSocialAccounts`
* 3.10 绑定失败
	- `bindQQFailure`
	- 可能的话，传入出错原因或错误码，帮助产品判断绑定失败原因 `{eventKey: <error message>}`
* 3.10 重复绑定弹窗
	- `qqDupBindAlert`
* 3.11 单击解绑
	- `unBindQQ`
* 3.11 单击解绑后 弹出“你的账号还没设置手机邮箱”
	- `unsetMailPhoneInUnbindQQAlert`
* 3.11 在弹出“你的账号还没设置手机邮箱”中
	- 取消解绑 `clickCancelInUnBindQQAlert`
	- 设置 `clickSetInUnBindQQAlert`

* 3.11 弹出“你的账号还没设置密码”
	- `notSetPasswordAlertInUnbindQQ`
* 在弹出“你的账号还没设置密码”中：
	- 取消解绑 `clickCancelInNotSetPasswordAlertInUnbindQQ`
	- 设置密码 `clickSetPassWordInNotSetPasswordAlertInUnbindQQ`
* 解绑成功弹窗
	- `unBindQQSuccessAlert`



