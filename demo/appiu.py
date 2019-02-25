#coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import unittest
from selenium import webdriver

''''
a simple test demo
'''
class activityTest(unittest.TestCase):

    def setUp(self):
        pass


    #个人中心设置
    def test_launchApp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "edu.yjyx.teacher",
            "noReset": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "deviceName": "HUAWEI MAT7-CL00",
            "appActivity": "edu.yjyx.main.activity.SplashActivity"
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        # driver.find_element_by_id("edu.yjyx:id/forgetPsw_tv").click()
        # driver.find_element_by_class_name("android.widget.EditText").send_keys("aaaa")
        p ='//*[@text="我的"]'
        driver.find_element_by_xpath(p).click()




        # #点击"注册"
        # driver.find_element_by_id("edu.yjyx:id/register_new").click()
        # driver.implicitly_wait(10)
        #
        # #填写注册信息
        # driver.find_element_by_id("edu.yjyx:id/et_name").send_keys("test01")
        # driver.find_element_by_id("edu.yjyx:id/et_phone").send_keys("150671185190")
        # driver.find_element_by_id("edu.yjyx:id/et_code").send_keys("1234")
        #
        # driver.find_element_by_id("edu.yjyx:id/et_psw").send_keys("0011")
        # driver.find_element_by_id("edu.yjyx:id/et_confirmPsw").send_keys("0011")






       # print driver.page_source
        # driver.find_element_by_id("edu.yjyx.student:id/userEdit").send_keys("15067118511")
        # driver.find_element_by_id("edu.yjyx.student:id/pwdEdit").send_keys("888888")
        # driver.find_element_by_id("edu.yjyx.student:id/submit").click()
        # driver.find_element_by_id("edu.yjyx.student:id/tab_icon_imv").click()
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("edu.yjyx.student:id/setting").click()
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("edu.yjyx.student:id/rl_name").click()
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("edu.yjyx.student:id/setting_modify_edit").click()
        # driver.find_element_by_id("edu.yjyx.student:id/student_title_confirm").click()
        #










if __name__ == '__main__':
    #构造测试集
    suite =unittest.TestSuite()
    suite.addTest(activityTest("test_launchApp"))
    #执行测试
    runner =unittest.TextTestRunner()
    runner.run(suite)


