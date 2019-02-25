#coding:utf-8
import string
import xlrd
#excel文件读写数据
data=xlrd.open_workbook(r"C:\Users\win10\Desktop\work\data1.xlsx")

print data.sheets()[0]

#print data.sheet_names()

