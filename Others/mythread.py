#coding:utf-8
import threading
import time


# python 多线程
exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name =name
        self.counter=counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name,self.counter,5)
        test()
        print "Exiting " + self.name




def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


def test():
    print "执行本公举！！！"




#创建新线程
thread1 =myThread(1,"TH-1",1)

thread2 =myThread(1,"TH-2",2)

thread3 =myThread(1,"TH-3",2)


thread4 =myThread(1,"TH-4",2)


if __name__ == '__main__':

    #开启线程
    thread1.start()
#    thread2.join()
    thread2.start()
    thread3.start()
    thread4.start()


print "Exiting Main Thread"



