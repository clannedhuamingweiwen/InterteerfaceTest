#coding:utf-8
import os

#结束已经开启的chromeDriver进程
def cleanUp(idx):
    process_list = {
        1: "chrome.exe",
        2: "idea64.exe"
    }
    cmd ="taskkill /f /im {} /t ".format(process_list[idx])
    os.system(cmd)

print cleanUp(2)