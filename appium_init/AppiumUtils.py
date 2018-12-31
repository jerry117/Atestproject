#coding:utf-8

from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
sleep(3)
print("滑动前")
driver.swipe(x1,y1,x1,y2)
print("滑动后")
# 增加滑动次数，滑动效果不明显，增加滑动次数

for i in range(5):
    print("第%d次滑屏"%i)
    sleep(3)
    driver.swipe(x1,y1,x1,y2)
sleep(3)


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
        sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeToDown(self,driver, n = 5):
        '''定义向下滑动方法'''
        print("定义向下滑动方法")
        x1 = width*0.5
        y1 = height*0.25
        y2 = height*0.9
        sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            sleep(3)
            driver.swipe(x1, y1, x1, y2)

    def swipeToLeft(self, driver, n = 5):
        '''定义向左滑动方法'''
        print("定义向左滑动方法")
        x1 = width*0.8
        x2 = width*0.2
        y1 = height*0.5

        sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            sleep(3)
            driver.swipe(x1, y1, x2, y1)


    def swipeToRight(self, driver, n = 5):
        '''定义向右滑动方法'''
        print("定义向右滑动方法")
        x1 = width*0.2
        x2 = width*0.8
        y1 = height*0.5

        sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            sleep(3)
            driver.swipe(x1, y1, x2, y1)



# TODO  处理对应不同的获取元素方法的处理。并判断元素是否存在
    def isElementExits(self, identifyBy, c):
        sleep()
        flag = None
        try:
            if identifyBy == 'id':
                driver.find_element_by_id(c)
            elif identifyBy == 'xpath':
                driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                driver.find_element_by_css_selector(c)
            flag = True

        except NoSuchElementException as e:
            flag = False
        finally:
            return flag
            print("元素存在")
            return True

#直接判断元素是否在
    def findItem(self, el):
        source = driver.page_source
        if el in source:
            return True
        else:
            return False

    def getEndCoordinate(self):
        pass