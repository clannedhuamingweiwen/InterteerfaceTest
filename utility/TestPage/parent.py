#coding:utf-8
from utility import KeywordActions as kd
from Settings.P_locator import *



class parent:

    def __init__(self):
        pass


    @staticmethod
    def single():
        k = kd()
        return k

    def vip(self):
        parent.single().init()

        parent.single().clickEle(vip_list["start"])
        parent.single().wait()

        parent.single().clickEle(vip_list["pay"])
        parent.single().wait()
        parent.single().clickEle(vip_list["num1"])

    def register(self):
        parent.single().init()
        #填写注册信息





p =parent()
print p.vip()





