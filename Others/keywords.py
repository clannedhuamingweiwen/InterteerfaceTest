#coding:utf-8
import requests
import json
class keywords:
    def __init__(self):
        pass

    # 发送get请求(不需要带cooikes参数的)
    def send_Get(self, url):
        try:
            r = requests.get(url)
        except  Exception  as get_error:
            return "发送get请求失败!"
        else:
            return r.content

    # '''
    # 针对业务需求封装常用的API
    # '''
    # 发送含有cookies的get请求
    def send_Get_cooikes(self, url, d, session_list):
        c = dict(sessionid=session_list)
        r1 = requests.get(url, params=d, cookies=c)
        return r1.content

    # 发送post请求（不需要加cooikes的）
    def send_pure_post(self, post_url, dict_args):
        r = requests.post(post_url, data=dict_args)

        get_token = r.json()["sessionid"]
        return get_token

    # 发送含有cookies的post请求(获取登录生成的sessonid信息)
    def send_post(self, url, params, post_string):
        post_c = dict(sessionid=post_string)
        r = requests.post(url, data=params, cookies=post_c)
        return eval(json.dumps(r.json()))

    # 发送put类型的请求
    def seng_Put_Msg(self, pt_url, put_par, put_string):
        put_c = dict(sessionid=put_string)
        r = requests.put(pt_url, data=put_par, cookies=put_c)
        return r.json()

