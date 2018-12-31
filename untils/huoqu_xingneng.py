#coding:utf-8

#获取手机性能的数据

import platform,os


#获取所运行的系统获取adb不一样的筛选条件。
def getsystemsta():
    system = platform.system()
    if system == 'Windows':
        find_manage = 'findstr'
    else:
        find_manage = 'grep'
    return find_manage
find = getsystemsta()

#获取CPU信息
def getcpusta(packagename,devices):
    try:
        cpu = 'adb -s {} shell top -n 1 | {} {} '.format(devices,find,packagename)
        re_cpu=os.popen(cpu).read().split()[2]
        return re_cpu
    except:
        pass

#获取使用的物理内存
def getmemorysta(packagename,devices):
    try:
        cpu = 'adb -s {} shell top -n 1 | {} {} '.format(devices, find, packagename)
        re_cpu =os.popen(cpu).read().split()[6]
        re_cpu_m = str(round(int(re_cpu[:-1])/1024))+'M'
        return re_cpu_m
    except:
        pass

if __name__ == '__main__':
    test = getcpusta('phone','192.168.42.101:5555')
    test1 = getmemorysta('phone','192.168.42.101:5555')
    print(test)
    print(test1)