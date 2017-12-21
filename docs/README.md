# robot_chat
使用Python中的itchat和图灵机器人部署聊天机器人

## itchat使用

### 安装

```
sudo pip install itchat
```

### 登陆

```python
itchat.auto_login(hotReload=True，loginCallback=login_success, exitCallback=logout_success)

def login_success():
    print 'login success'

def logout_success():
    print 'logout success'
```

该方法将通过扫描二维码登陆微信

参数hotReload为可选参数，其中：

- hotReload = True：登陆之后会在当前文件夹生成一个静态文件itchat.pkl用于储存登陆信息，保持登陆状
- hotReload = False：默认值为False，登陆之后只能短时间有效，不会长时间保持登陆状态

参数loginCallback为登陆完成后的回调函数，若不设置该参数，登陆完成后将删除二维码图片并清空命令行显示
参数exitCallback为注销完成后的回调函数

### 注册接收消息

