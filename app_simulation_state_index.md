## app simulation states

### App related

* 应用退出  
应用退出.  
Code: -1  
Next: None

* 应用转到后台  
应用被转到后台.  
Code: -2  
Next: [
  -3: 0.75  
  -1: 0.25
]

* 应用从后台恢复  
应用从后台恢复  
Code: -3  
Next: 与-2状态前一个状态相同  

### 开始-->引导页  

* 打开应用,弹出推送消息Alert  
Code: 0  
Next: [
  1: 0.65,
  2: 0.35
]

* 消息Alert,用户选择"不允许"  
Code: 1  
Next: [
  3: 0.95,
  -1: 0.05
]

* 消息Alert,用户选择"好"  
Code: 2  
Next: [
  3: 0.95,
  -1: 0.05
]

* 进入新手引导页  
Code: 3  
Point: "enterGuidePage"  
Next: [
  4: 0.65,
  5: 0.3,
  -1: 0.05
]

* 新手引导页,用户选择"马上开始"  
Code: 4  
Point: clickExperience  
Next: [
  6: 0.95,
  -1: 0.05
]

* 新手引导页,用户选择"注册或登录"  
Code: 5  
Point: clickUserLogBtn  
Next: [
  7: 0.95,
  -1: 0.05
]

### 注册页  

* 注册页打开  
Code: 7  
Point: enterSignupPage  
User_prop: {
  "role": "student"
}  
Next: [
  3: 0.05,
  8: 0.15,
  9: 0.2,
  10: 0.05,
  11: 0.05,
  12: 0.05,
  13: 0.15,
  14: 0.25,
  -1: 0.05
]
