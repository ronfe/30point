## app simulation states

### App related

* 应用退出  
应用退出.  
```Code: -1```
```Next: None```

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
  4: 0.55,
  5: 0.2,
  -1: 0.05,
  -2: 0.2
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
  8: 0.1,
  9: 0.15,
  10: 0.05,
  11: 0.05,
  12: 0.05,
  13: 0.1,
  14: 0.2,
  -1: 0.1,
  -2: 0.15
]

* 注册页,用户选择"老师"  
Code: 8  
User_prop: {
  "role": "teacher"
}  
Next: [
  3: 0.05,
  15: 0.05,
  9: 0.3,
  10: 0.05,
  11: 0.05,
  12: 0.05,
  13: 0.05,
  14: 0.1,
  -1: 0.15,
  -2: 0.15
]

* 注册页,用户填写账号  
Code: 9  
User_prop: {
  "userName": @param-String
}  
Next: [
  3: 0.1,
  [if 8: 15: 0.05; elif 15: 8: 0.05; else: 15: 0.05],
  10: 0.25,
  11: 0.05,
  12: 0.1,
  13: 0.1,
  14: 0.2,
  -1: 0.15,
  -2: 0.15
]

* 注册页,用户填写密码  
Code: 10  
User_prop: {
  "password": @param-String
}  
Next: [
  3: 0.05,
  [
    if 8: 15: 0.05; 
    elif 15: 8: 0.05; 
    else: 15: 0.05
  ],
  9: 0.15
  16: 0.15,
  11: 0.2,
  12: 0.1,
  13: 0.05,
  14: 0.1,
  -1: 0.05,
  -2: 0.15
]

* 注册页,用户更改同意协议复选框  
Code: 11  
User_prop: {
  "agreedLicence": -"agreedLicence"
}  
Next: [
  3: 0.05,
  [
    if 8: 15: 0.05; 
    elif 15: 8: 0.05; 
    else: 15: 0.05
  ],
  9: 0.05,
  10: 0.05,
  k: [
    if 16: 16: 0.1;
    else: 16: 0.05
  ],
  l: [
    if user.aggreedLicence == True: 11: 0.05;
    else : 11: 0.15
  ],
  17: 0.05
  m: [
    if l[0]: 12: 0.2;
    else: 12: 0.1
  ],
  n: [
    if k[0]: 12: 0.15;
    else: 12: 0.2
  ],
  13: 0.05,
  14: 0.05,
  -1: 0.05,
  -2: 0.1
]
