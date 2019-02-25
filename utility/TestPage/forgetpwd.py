#coding:utf-8

from locatorgroup.t_locator import ele1_list
from utility import KeywordActions as kd
from locatorgroup.P_locator import ele_list
from Settings.dataGroups import values
import unittest

'''
app移动端 用户忘记密码流程
'''

class forget(kd,unittest.TestCase):
    def setUp(self):
        pass


    @staticmethod
    def singleInstance():
        k = kd()
        return k
    
    #家长端"忘记密码"流程
    def parent_Forget(self):
        forget.singleInstance().init()
        #clear操作
        forget.singleInstance().clearEle(ele_list["p_forget"])
        #点击"忘记密码"
        forget.singleInstance().clickById("edu.yjyx:id/forgetPsw_tv")

        #加入休眠时间
        forget.singleInstance().wait()
        #输入手机号码
        forget.singleInstance().inputText(ele_list["phone"],values["phonenumber"])
        # 加入休眠时间
        forget.singleInstance().wait()
        #点击“确定”按钮
        forget.singleInstance().clickById(ele_list["submit"])
        # 加入休眠时间
        forget.singleInstance().wait()
        #点击"短信验证码找回"
        forget.singleInstance().clickById(ele_list["sms_reback"])
        # 加入休眠时间
        forget.singleInstance().wait()
        # #输入验证码
        # forget.singleInstance().inputText( ele_list["verfty"],values["rcode"])
        #输入新密码
        forget.singleInstance().inputText(ele_list["pwd1"],values["pwd2"])

        #输入确认密码
        forget.singleInstance().inputText(ele_list["pwd2"],values["pwd2"])

    # 老师端"忘记密码"流程
    def teacher_Forget(self):
        forget.singleInstance().init()
        # clear
        forget.singleInstance().clearEle("edu.yjyx.teacher:id/userEdit")
        # 点击忘记密码
        forget.singleInstance().clickById()
        forget.singleInstance().wait()
        # 输入手机号码
        forget.singleInstance().inputText(e1["phone"], "15067118510")
        # 加入休眠时间
        forget.singleInstance().wait()
        # 点击“确定”按钮
        forget.singleInstance().clickById(e1["submit"])
        # 加入休眠时间
        forget.singleInstance().wait()
        # 点击"短信验证码找回"
        forget.singleInstance().clickById(e1["sms_reback"])
        # 加入休眠时间
        forget.singleInstance().wait()
        # 输入验证码
        forget.singleInstance().inputText(e1["verfty"], "110")
        # 输入新密码
        forget.singleInstance().inputText(e1["pwd1"], "15067118510")

        # 输入确认密码
        forget.singleInstance().inputText(e1["pwd2"], "15067118510")


f =forget()













