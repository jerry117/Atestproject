#coding:utf-8

import time
from appium import webdriver


caps = {}

caps['platformName'] = 'Android'
caps['platformVersion'] = '6.0'
caps['deviceName'] = 'N79SIV5PVCSODAQC'
caps['appPackage'] = 'com.tmall.wireless'
caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'
#隐藏键盘
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)


# 获取屏幕的size
size = driver.get_window_size()
print(size)
# 获取屏幕宽度 width
width = size['width']
print(width)
# 获取屏幕高度 height
height = size['height']
print(height)



# 执行滑屏操作,向下（下拉）滑动
x1 = width*0.5
y1 = height*0.25
y2 = height*0.8
time.sleep(3)
print("滑动前")
driver.swipe(x1,y1,x1,y2)
print("滑动后")
# 增加滑动次数，滑动效果不明显，增加滑动次数

for i in range(5):
    print("第%d次滑屏"%i)
    time.sleep(3)
    driver.swipe(x1,y1,x1,y2)
time.sleep(3)


class AppiumUtils():
    '''
        滑动功能
    '''
    def swipeToUp(self, driver, n=5):
        '''定义向上滑动方法'''
        print("定义向上滑动方法")
        x1 = width * 0.5
        y1 = height * 0.9
        y2 = height * 0.25
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeToDown(self,driver, n = 5):
        '''定义向下滑动方法'''
        print("定义向下滑动方法")
        x1 = width*0.5
        y1 = height*0.25
        y2 = height*0.9
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeToLeft(self, driver, n = 5):
        '''定义向左滑动方法'''
        print("定义向左滑动方法")
        x1 = width*0.8
        x2 = width*0.2
        y1 = height*0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x2, y1)


    def swipeToRight(self, driver, n = 5):
        '''定义向右滑动方法'''
        print("定义向右滑动方法")
        x1 = width*0.2
        x2 = width*0.8
        y1 = height*0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            driver.swipe(x1, y1, x2, y1)



# TODO  处理driver1，判断元素存在
    def isElementExits(self, driver1, by):
        try:
            driver.find_element(by)
            print("元素存在")
            return True


        except Exception as e:
            print("元素不存在!error: "+ e)
        # TODO 测试返回逻辑
        return False



    def getEndCoordinate(self):
        pass