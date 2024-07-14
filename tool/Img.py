"""
作者: d233hj
创建日期: <2024-07-13  16:54:25>
最后编辑时间: <2024-07-13  17:07:01>
最后编辑人员: d233hj
FilePath: \WarshipGirl\tool\Img.py
"""

import cv2


class Img:
    "单个图片对象，存储相关信息"
    _name = ""
    _src = ""
    _img = ""
    _axis = (0, 0)

    def __init__(self, name, src):
        self._name = name
        self._src = src
        self._img = cv2.imread(self._src)

    def getName(self):
        return self._name

    def getSrc(self):
        return self._src

    def getAxis(self):
        return self._axis

    def setAxis(self, axis):
        self._axis = axis

    def getImg(self):
        return self._img
