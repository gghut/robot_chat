import itchat
import requests
import hashlib

def main():
    itchat.auto_login(hotReload=True)
    itchat.send_msg(msg='Test Message')
    itchat.run()
    pass

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def rsponse(msg):
    print msg
    r = robot(msg['Content'],msg['FromUserName'])
    itchat.send_msg(r, toUserName=msg['FromUserName'])
    pass

def robot(msg, uid):
    url = 'http://www.tuling123.com/openapi/api'
    key = '588700afd2ca4a5bbecc7498114917fe'
    hash = hashlib.md5()
    uid = hash.update(uid.encode('utf-8'))
    data = {}
    data['key'] = key
    data['info'] = msg
    data['userid'] = uid
    print uid
    try:
        response = requests.post(url, data=data).json()
        print response
        return response.get('text')
    except:
        return 'Hello World'

if __name__ == '__main__':
    main()