#coding:utf-8

import os
import subprocess

# 得到手机信息
def get_phone_info(devices):
    cmd = "adb -s "+ devices +" shell cat /system/build.prop "
    phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    l_list = {}
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model.geny-def=" #型号 针对Genymotion模拟器
    brand = "ro.product.brand.geny-def=" # 品牌  针对Genymotion模拟器
    device = "ro.product.device.geny-def=" # 设备名  针对Genymotion模拟器
    for line in phone_info:
         for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                l_list["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                l_list["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                l_list["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                l_list["device"] = temp[len(device) :]
                break
    print(l_list)
    return l_list


if __name__ == '__main__':
    test = get_phone_info('192.168.42.101:5555')
