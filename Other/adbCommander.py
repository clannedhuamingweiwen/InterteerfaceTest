#coding:utf-8
import os
import zipfile
import unittest

class Commandor(unittest.TestCase):

    def setUp(self):

        self.path=r"D:\devices\apk"
        self.fullNameList=["edu.yjyx.teacher","edu.yjyx.student","edu.yjyx"]

        self.iosPath=r"D:\devices\ios"
        self.product=r"C:\Users\win10\Desktop\product\pro"
        self.uiPath=r"C:\Users\win10\Desktop\product\历史版本更新详情"

        self.opt={1:"最终稿",2:"ui"}


    def test_CreateFiles(self):


        num =[x for x in range(1,10)]
        for fileName in num:
            folder = r"D:\devices\{}".format(fileName)
            os.mkdir(folder)



    #利用安卓adb命令进行apk装包 
    def test_install(self):

        #显示当前目录的位置切换到adb工具所在的目录下
        os.chdir(self.path)
        # path = os.curdir

        #显示当前处于连接的设备名称列表
        rst = os.system("adb devices")
        print ">>>starting to install the prepared package>>>"
        try:

            #卸载当前手机上已安装的apk应用
            for packageName in self.fullNameList:
                exitCmd = "adb uninstall {}".format(packageName)
                os.system(exitCmd)

            # 查看当前目录下的文件
            f = os.listdir(self.path)
            #安装待测试apk包
            for apk_Name in f:
                cmd = "adb install {}".format(apk_Name)
                print " The apk name is:",apk_Name
                # os.remove(apk_Name)
                os.system(cmd)

        except IOError:
            return "安装过程失败,请稍后重试！"

        return rst

    #遍历某目录下的文件
    def test_clear(self):
        os.chdir(self.path)
        removeFile =os.listdir(self.path)
        for f in removeFile:
            os.remove(f)

    #对压缩文件进行解压
    def test_zip(self):
        f_name = r"D:\devices\apk\1.zip"

        path = r"D:\devices\tara"
        print zipfile.is_zipfile(f_name)

        zipf = zipfile.ZipFile(f_name)
        # 获取待解压的文件列表
        print zipf.namelist()
        zipf.extractall(path)



    #更新git 产品原型以及Ui图
    def test_fresh_Git(self,cmd="git pull"):

        answer=int(raw_input("你是要更新产品原型图还是ui图?:"))
        if answer is 1:
            os.chdir(self.product)
            os.system(cmd)
        else:
            os.chdir(self.uiPath.decode("utf-8").encode("gbk"))
            os.system(cmd)


    def test_connection(self):
        print "开始检测当前的网路情况"
        for i in range(1,30):
            os.system("ping www.baidu.com")









    # 清理已经安装好的apk包
    def tearDown(self):
        os.chdir(self.path)
        removeFile = os.listdir(self.path)
        for f in removeFile:
            os.remove(f)




if __name__ == '__main__':

    #实现自动化安装测试包的工作test_connection
    case_Name = "test_install"
    # case_Name="test_fresh_Git"
    # case_Name ="test_CreateFiles"
    # case_Name="test_zip"
    # case_Name="test_connection"
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Commandor(case_Name))
    # 执行测试
    runner = unittest.TextTestRunner()

    runner.run(suite)





