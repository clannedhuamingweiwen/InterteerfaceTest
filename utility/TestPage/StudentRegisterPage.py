#coding:utf-8
from utility import KeywordActions as kd
from locatorgroup.t_locator import auth_list
import unittest



class Student():
    def __init__(self):
        self.pageName ="学生端自注册"

    @staticmethod
    def single():
        k = kd()
        return k

    # def signUp(self):

