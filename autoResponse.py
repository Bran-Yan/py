import itchat
import requests


# 上传获得消息内容到图灵机器人
def getMessage(msg):
    # apiURL = 'http://www.tuling123.com/openapi/api'
    # data = {
    #     'key': '53827c5de4f141569470222c87611254',
    #     'info': msg,
    #     'userID': '403'
    # }
    apiURL="http://api.qingyunke.com/api.php?key=free&appid=0&msg="+msg
    # r = requests.post(apiURL, data=data).json()
    r = requests.get(apiURL).json()
    # print('答：' + r.get('text'))
    # return r.get('text')
    print('答：' + r.get('content').replace("{br}", "\n").replace("菲菲", "帅哥我"))
    return r.get('content').replace("{br}", "\n").replace("菲菲", "帅哥我")


# 监听个人微信聊天
@itchat.msg_register(itchat.content.TEXT)
def return_message(msg):
    try:
        print('问：' + msg['Text'])
    except Exception as e:
        print(e)
    return getMessage(msg['Text'])



#监听微信群聊天
@itchat.msg_register([itchat.content.TEXT],isGroupChat=True)
def return_message(msg):
  if '@403' in msg['Text']:
    return "您好，现在在忙，稍后给您回复！"

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
