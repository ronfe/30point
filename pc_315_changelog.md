Tacking Events Changelog (PC/Web v3.1.5) 待续
--

注：页面位置以PRD序号为准
保留原注册登录逻辑中的全部埋点

### 外页

* 进入2.10页面 [**tested**]
    - `enterQQUserChooseIdentity`

* 2.10页面，点击“老用户” [**tested**]
    - `clickChooseExistedUser`

* 2.10页面，点击“新用户” [**tested**]
    - `clickChooseNewUser`

* 2.10页面，点击“下一步” [**tested**]
    - `clickQQUserIdentityNext`

* 进入2.12页面 [**tested**]
    - `enterQQNewUserRoleSelection`

* 2.12页面，点击“老师” [**tested**]
    - `clickQQNewUserChooseTeacher`

* 2.12页面，点击“学生” [**tested**]
    - `clickQQNewUserChooseStudent`

* 2.12页面，点击“下一步” [**tested**]
    - `clickQQNewUserRoleNext`

* 进入2.11页面 [**tested**]
    - `enterQQOldUserBind`

* 2.11页面，点击“忘记密码” [**tested**]
    - `clickQQOldUserForgetPasswd`

* 2.11页面，点击“立即绑定” [**tested**]
    - `clickQQOldUserBindAccount`

* 2.11页面，点击“立即绑定”后，绑定成功 [**tested**]
    - `clickQQOldUserBindSuccess`

* 2.11页面，点击“立即绑定”后，绑定失败 [**tested**]
    - `clickQQOldUserBindFailure`
    - `{error: String}`

* 2.11页面，点击“放弃绑定” [**tested**] 
    - `clickQQOldUserAbortBinding`

* 2.11页面，点击“放弃绑定”后，在弹窗中选择“继续绑定” [**tested**]
    - `clickQQOldUserContinueBinding`

* 2.11页面，点击“放弃绑定”后，在弹窗中选择“放弃绑定” [**tested**]
    - `clickQQOldUserConfirmAbort`

* 

##PC端个人中心
注:默认保留原个人中心中的全部埋点,如果有重复、冲突埋点，默认保留原埋点


* 3.1 修改邮箱 [**tested**]
	- `modifyEmailInMyProfile`
* 3.1 修改手机号 [**tested**]
	- `modifyPhoneInMyProfile`
* 3.2 邮箱格式错误(如果之前有埋，保留原埋点)[**tested**]
	- `enterWrongEmailInMyProfile`
* 3.2 手机号码格式错误 [**tested**]
	- `enterWrongPhoneNumberInMyProfile`
* 3.3 邮箱占用 [**tested**]
	- `dupMailInMyProfile`
* 3.3 手机号占用 [**tested**]
	- `dupPhoneNumberInMyProfile`
* 0.2 个人资料页发现没有设置密码的弹窗 [**tested**]
	- `nonePasswordAlertInMyProfile`
* 0.2 弹窗中单击 "先不设置" [**tested**]
	- `setPassWordNextTimeAlertInMyProfile`
* 0.2 弹窗中单击 去设置密码 [**tested**]
	- `clickEnterSetPasswordAlertInMyProfile`
* 3.5 修改资料后未保存去往其它页面时，弹出“修改尚未保存 页” [**tested**]
	- `notSaveChangeAlertInMyProfile` 
* 3.5 “修改尚未保存页” 单击不保存 [**tested**]
	- `clickNotSaveChangeAlertInMyProfile`
* 3.5 “修改尚未保存页” 单击"再看看" [**tested**]
	- `clickSaveChangeAlertInMyProfile`

## PC 个人中心密码管理部分
注： 默认优先保留之前埋点

* 3.6 进入密码管理页 [**tested**]
	- `enterModifyPasswordPage`

其余埋点保留之前所有的

## PC个人中心社交账户绑定
注： 默认优先保留之前埋点

* 3.10 进入社交账绑定页 [**tested**]
	- `enterBindSocialAccounts`
* 3.10 绑定失败
	- `bindQQFailure` [**tested**]
	- 可能的话，传入出错原因或错误码，帮助产品判断绑定失败原因 `{eventKey: <error message>}`
* 3.10 重复绑定弹窗 [**tested**]
	- `qqDupBindAlert`
* 3.11 单击解绑 [**tested**]
	- `unBindQQ`
* 3.11 单击解绑后 弹出“你的账号还没设置手机邮箱” [**tested**]
	- `unsetMailPhoneInUnbindQQAlert`
* 3.11 在弹出“你的账号还没设置手机邮箱”中 [**tested**]
	- 取消解绑 `clickCancelInUnBindQQAlert`
	- 设置 `clickSetInUnBindQQAlert` [**tested**]

* 3.11 弹出“你的账号还没设置密码” [**tested**]
	- `notSetPasswordAlertInUnbindQQ`
* 在弹出“你的账号还没设置密码”中： [**tested**]
	- 取消解绑 `clickCancelInNotSetPasswordAlertInUnbindQQ`  [**tested**]
	- 设置密码 `clickSetPassWordInNotSetPasswordAlertInUnbindQQ`  [**tested**]
* 解绑成功弹窗  [**tested**]
	- `unBindQQSuccessAlert`

## 应用商店

* 单击购买 [**tested**]
	- 购买按钮 `buyProfileAvatar`
* 购买弹窗 [**tested**]
	- `cancelBuyProfileAvatar`
	- `confirmBuyProfileAvatar`
		- `{eventValue:avatar/coions}`

## 知识点页APP引流按钮
- `ycApp`



