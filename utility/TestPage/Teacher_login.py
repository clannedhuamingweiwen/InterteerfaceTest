#coding:utf-8
from utility import KeywordActions as kd
from locatorgroup.t_locator import auth_list
import unittest

class teacher:

    def __init__(self):
        self.pageName="身份认证"


    #创建一个新的单例模式
    @staticmethod
    def single():
        k = kd()
        return k

     #老师身份认证
    def idc(self):
        teacher.single().init()
        # clear操作
        # teacher.single().clearEle(ele1_list["username"])
        #
        # #输入用户名
        # teacher.single().inputText(teacher_list["username"][0],teacher_list["username"][1])
        # #输入密码
        # teacher.single().inputText(teacher_list["password"][0],teacher_list["password"][1])
        #
        # #点击登录按钮
        # teacher.single().clickByLocator(teacher_list["btn"])
        #休眠
        # teacher.single().wait()
        #点击我
        teacher.single().clickEle(auth_list["mine"])
        #休眠
        teacher.single().wait()
        #点击“身份认证”
        teacher.single().clickEle(auth_list["auth"])
        # 休眠
        teacher.single().wait()
        #输入认证姓名
        teacher.single().inputText(auth_list["name"][0],auth_list["name"][1])
        #输入认证身份证号
        teacher.single().inputText(auth_list["idCard"][0],auth_list["idCard"][1])
        # 休眠
        teacher.single().wait()
        #****************点击正面照片********************
        teacher.single().clickEle(auth_list["pos"])
        # 休眠
        teacher.single().wait()
        #选择手机上传
        teacher.single().clickEle(auth_list["chooseStyle"])
        # 休眠
        teacher.single().wait()

        # 休眠
        teacher.single().wait()
        #从默认选择的相册中选择要上传的photo
        teacher.single().clickEle(auth_list["upload"])
        # 休眠
        teacher.single().wait()
        #点击确定，确定上传
        teacher.single().clickEle(auth_list["success"])
        # 休眠
        teacher.single().wait()

        # ****************点击反面照片********************
        teacher.single().clickEle(auth_list["back"])
        # 休眠
        teacher.single().wait()
        # 选择手机"相册"上传
        teacher.single().clickEle(auth_list["chooseStyle"])
        # 休眠
        teacher.single().wait()
        # 从默认选择的相册中选择要上传的photo
        teacher.single().clickEle(auth_list["upload2"])
        # 休眠
        teacher.single().wait()
        # 点击确定，确定上传
        teacher.single().clickEle(auth_list["success"])
        # 休眠
        teacher.single().wait()
        #点击“提交认证
        teacher.single().clickEle(auth_list["finish"])





t_teacher =teacher()

print t_teacher.idc()








