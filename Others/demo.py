#coding:utf-8
import os
import sys
import itertools


exp="xpath=aaaa"
exp1="login.name1>id=bbb"
exp2="login.name2>classname=ccc"
exp3="xx=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


d ="xpath=//*[@text='我的']"

#methods
rst=d.split("=")[0]

value=d.split("=")[1]
print value

# if rst=="xpath":
#     print value
# elif rst =="xx":
#     print value
# elif rst=="id":
#     print value
#

# n =itertools.count(1)
# for i in n:
#     # print i





# t_p ="C:\Users\win10\Desktop\copy.txt"
# #print os.path.getctime("C:\Users\win10\Desktop\copy.txt")
# print os.path.basename(t_p)
#
# print  "split after is:",os.path.split(t_p)