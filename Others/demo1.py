#coding:utf-8
import os
import sys

#测试 centos7环境



def isfile(file_path):
    if os.path.isfile(file_path):
        print os.listdir(file_path)
    else:
        print "你要找的并不是目录！"


def print_win(path):
    test=os.listdir(path)
    if test is None:
        return "要查找的文件路径不存在!"
    else:
        return os.listdir(path)




#测试本地文件路径，打印输出结果xxyy
data=print_win("C:\Users\win10\Desktop\pack")
for i in print_win("C:\Users\win10\Desktop\pack"):
     print i,data[i]
