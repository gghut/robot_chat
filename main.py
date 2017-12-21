# -*- coding: UTF-8 -*-
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

def format_uid(uid):
    if uid is None:
        return '00000000000000000000000000000000'
    else:
        hash = hashlib.md5()
        return hash.update(uid.encode('utf-8'))

if __name__ == '__main__':
    main()