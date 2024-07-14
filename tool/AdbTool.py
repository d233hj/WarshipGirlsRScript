"""
作者: d233hj
创建日期: <2023-12-16  15:14:27>
最后编辑时间: <2023-12-16  15:43:27>
最后编辑人员: d233hj
FilePath: \worldTree\tool\tool.py
"""

import os
import subprocess
from pyminitouch import MNTDevice
import cv2
from varname import argname
from PIL import Image
import time
import uiautomator2 as u2


class AdbTool:
    "模拟器操作工具类"
    __adbConnect = "127.0.0.1:16384"
    __img_where = ".\img\\tmp.png"
    __msg = "None"

    def __init__(self):
        self.__center = None
        self.__max_val = None
        # self.__adb_init
        _DEVICE_ID = self.__adbConnect
        self.device = u2.connect(_DEVICE_ID)
        # self.device = MNTDevice(_DEVICE_ID)

    def __image_to_position(self, screen, template):
        "对比图片   \nreturn:__center    图片中心点,\n\t__max_val   相似度"

        image_x, image_y = template.shape[:2]
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, __max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print("prob:", __max_val)
        if __max_val > 0.90:
            __center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
            self.__center = __center
            self.__max_val = __max_val
        else:
            self.__center = False
            self.__max_val = __max_val

    def capture(self) -> bytes:
        """快速截图，直接截图并作为字节保存在内存中"""
        process = subprocess.Popen(
            "adb shell screencap -p", shell=True, stdout=subprocess.PIPE
        )
        data = process.stdout.read()
        data = data.replace(b"\r\n", b"\n")
        return data

    def __take_screenshot(self):
        """ "截图"
        os.system("adb shell screencap -p /data/screenshot.png")
        os.system("adb pull /data/screenshot.png " + self.__img_where)
        print(self.__img_where)"""
        data = self.capture()
        with open(self.__img_where, "wb") as f:
            f.write(data)
            f.close()

    def setMsg(self, msg):
        self.__msg = msg

    def getMsg(self):
        return self.__msg

    def adb_click(self, center, offset=(0, 0)):
        (x, y) = center
        x += offset[0]
        y += offset[1]

        self.device.click(x, y)
        # self.device.tap([(x, y)])

        # os.system(f"adb shell input tap {x} {y}")

    def __adb_init(self):
        """os.system("adb connect " + self.__adbConnect)"""
        """_DEVICE_ID = self.__adbConnect
        device = MNTDevice(_DEVICE_ID)"""

    def research_img(self, template):
        "单纯寻找图片\nreturn:False\n\tTrue"
        self.setMsg("None")
        self.__take_screenshot()
        screen = cv2.imread(self.__img_where)
        self.__image_to_position(screen, template)
        if self.__center != False:
            self.setMsg(
                "#-found img:" + str(self.__center) + "\n -" + str(self.__max_val)
            )
            return True
        else:
            self.setMsg(
                "#-img not found:" + str(self.__center) + "\n -" + str(self.__max_val)
            )
            return False

    def apper_to_click(self, template, name="img"):
        "匹配图片，如果存在则点击中心\ntemplate:需要查找的图片"
        self.setMsg("None")
        self.__take_screenshot()
        screen = cv2.imread(self.__img_where)
        self.__image_to_position(screen, template)
        if self.__center != False:
            self.adb_click(self.__center)
            self.setMsg(
                "#~found img:<"
                + str(name)
                + ">, "
                + str(self.__center)
                + "\t "
                + str(self.__max_val)
            )
            print(self.getMsg())
            return True
        else:
            self.setMsg(
                "#-img not found:" + str(self.__center) + "\n -" + str(self.__max_val)
            )
            return False
