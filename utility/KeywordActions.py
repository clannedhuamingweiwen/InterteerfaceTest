#coding:utf-8
from appium import webdriver
from selenium import webdriver

from  Settings import appiumConfig as appconfig


#封装appium -python

class keywords():
    def __init__(self):
        self.desired_caps =appconfig.desired_caps
        self.url =appconfig.romote_url

    #启动appiuim各项服务
    def init(self,time=10):
        global driver
        driver= webdriver.Remote(self.url, self.desired_caps)
        driver.implicitly_wait(time)

    #安装app被测应用
    def install_package(self,apk_path):
        return driver.install_app(apk_path)

    # 选择不同的定位器
    @staticmethod
    def getLocator(exp):
        # selenium内置的元素定位方式
        locator = exp.split(">")[0]
        print "当前的元素选择器是:", locator
        # 识别元素控件的定位表达式
        value = exp.split(">")[1]
        print "对应的表达式是:", value
        if locator == "id":
            return driver.find_element_by_id(value)
        elif locator == "name":
            return driver.find_element_by_name(value)
        elif locator == "classname":
            return driver.find_element_by_class_name(value)
        elif locator == "xpath":
            return driver.find_element_by_xpath(value)
        elif locator == "css":
            return driver.find_element_by_css_selector(value)

    #点击元素
    def clickEle(self,exp1):
        keywords.getLocator(exp1).click()


    #根据元素控件的属性，在文本框输入内容
    def inputText(self,exp1,value):
        keywords.getLocator(exp1).send_keys(value)

    #清除文本输入框中的文本内容
    def clearEle(self,exp2):
        keywords.getLocator(exp2).click()


    #加入休眠时间
    def wait(self,time=10):
        driver.implicitly_wait(time)

    #重置应用
    def destrory(self):
        driver.reset()

     #关闭当前应用的窗口
    def closeApp(self):
        driver.close()

    #后台运行app多少秒
    '''
    :Args:

     - seconds - the duration for the application to remain in the background

用法 driver.background_app(5)   置后台5秒后再运行
    '''
    def before(self,sec):
        driver.background_app(sec)


    # #适用于WebView页面 提交表单动作
    # def sublitView(self):
    #     driver.submit()
    #


    #退出脚本运行并关闭每个相关的窗口连接
    def exit(self):
        driver.quit()


    '''
    在当前窗口/框架（特指 Html 的 iframe ）同步执行 javascript 代码。你可以理解为如果这段代码是睡眠5秒，这五秒内主线程的 javascript 不会执行
    '''
    def jsExcutor(self,ScriptText,*params):
        driver.execute_script(ScriptText,params)







    #获取当前的activity页面名称
    def show_current_Activity(self):
         return driver.current_activity

