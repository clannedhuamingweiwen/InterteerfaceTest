#coding:utf-8
import requests
import json
import unittest
'''
重新封装请求类 >>>引入unittest单元测试框架

'''
class requester(unittest.TestCase):

    def __init__(self,URL,params):
        self.URL =URL
        self.params =params
        self.sessionid =""


    def sendGet(self,**args):

        try:
            r = requests.get(self.URL)
        except  Exception  as get_error:
            return "发送get请求失败!"
        else:
            return r.content

    #发起get类型的请求
    def isGetSession(self,URL,params,request_string):

            try:
                c = dict(sessionid=request_string)
                r = requests.get(url, params=params, cookies=c)
            except  Exception  as get_error:
                return "发送get请求失败!"
            else:
                return "返回的内容为%s" % r.content



    # def log(self):
    #     return self.dict
    #
    # def log1(self):
    #     return self.params
    #
    # def log2(self):
    #     return self.URL

    # def aaa(self,URLs, params):
    #     try:
    #         r = requests.post(URLs, data=params)
    #     except  Exception  as get_error:
    #         return "发送post请求失败!"
    #     else:
    #         return r.json()

    def df(self):

        if self.sessionid is None:
            return "无法取到Session信息"
        else:
            try:
                c = dict(sessionid=self.sessionid)
                r = requests.post(self.URL, data=self.params,cookies=c)
            except Exception as e1:
                return "发送post请求失败！"


    #发送不携带post方法的请求
    def test_send_post(self):
      #  post_c = dict(sessionid=post_string)
        r = requests.post(self.URL, data=self.params)
        self.assertEqual(r.status_code,200)
        return r.json()


       # return eval(json.dumps(r.json()))


    def seng_Put_Msg(self, pt_url, put_par, put_string):
        put_c = dict(sessionid=put_string)
        r = requests.put(pt_url, data=put_par, cookies=put_c)
        return r.json()


url ="http://qa.zgyjyx.net/api/teacher/mobile/login/"


url2="http://qa.zgyjyx.net/api/student/mobile/tasks/"


url3="http://qa.zgyjyx.net/api/teacher/mobile/yj_teachers/"


pa ={
    'username':"15067118511",
    'ostype':0,
    'password':1234567,
    'devicetoken':'AkVNMOxBLUTdm4F1-_mDJm0n2iIeIo_-tAxcO6K14hOD'

        }

renew_params = {
    "action": "changeuserpassword",
    "oldpassword": "1234567",
    "newpassword": "888888"
}


# d =requester(url,pa)
# #获取登录token
# #print getattr(d,"aaa")(url,pa)["sessionid"]
# result =getattr(d,"send_post")()
# print result

# token =getattr(d,"send_post")()["sessionid"]
# print token
# s_str = token.encode('unicode-escape').decode('string_escape')
# print type(s_str)

#请求xx接口
#print getattr(d,"isGetSession")(url2,get_info,token)


#print getattr(d,"seng_Put_Msg")(url3,renew_params,token)



