# robot_chat
使用Python中的itchat和图灵机器人部署微信聊天机器人

[ITChat](https://itchat.readthedocs.io/zh/latest/)

[WXBot](https://github.com/liuwons/wxBot)

## itchat使用

### 安装

```
sudo pip install itchat
```

### 登陆

```python
itchat.auto_login(hotReload=True,loginCallback=login_success, exitCallback=logout_success)

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

itchat将根据接收到的消息类型寻找已注册的对应方法，若没有找到与之对应的方法，那么该条消息将会被抛弃，消息类型如下：

- TEXT：文本消息
- MAP：位置分享
- CARD：名片
- SHARGING：分享
- PICTURE：图片
- RECORDING:语音消息
- ATTACHMENT:附件
- VIDEO:小视频
- FRIENDS：好友请求
- SYSTEM:系统消息
- NOTE：通知消息

```python
@itchat.msg_register(msgType, isFriendChat=True, isGroupChat=True,isMpChat=True)
def message_listener(msg):
    flag = msg.isAt
    message = msg['Text']
    uid = message['FromUserName']
```

## 发送消息

```python
send(msg="Text Message", toUserName=None)
```

- msg：文本消息内容，@fil@path发送文件，@img@path发送图片，@vid@path发送视频
- toUserName：消息发送对象，None为发送给自己

```python
itchat.send_msg("hello world.")
itchat.send_file("/tmp/test.txt")
itchat.send_img("/tmp/test.txt")
itchat.send_video("/tmp/test.txt")
```

## 图灵聊天机器人接口

号称中文语境下智能度最高的机器人大脑

 ```python
 def robot(msg, uid):
    url = 'http://www.tuling123.com/openapi/api'
    key = '********************************'
    data = {}
    data['key'] = key
    data['info'] = msg
    data['loc'] = '成都市高新区'
    data['userid'] = format_uid(uid)
    print uid
    try:
        response = requests.post(url, data=data).json()
        return response.get('text')
    except:
        return 'Hello World'
```

## QQ Python机器人

[QQBot](https://github.com/pandolia/qqbot/)