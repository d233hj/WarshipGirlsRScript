"""
作者: d233hj
创建日期: <2024-07-13  16:49:55>
最后编辑时间: <2024-07-13  18:05:47>
最后编辑人员: d233hj
FilePath: \WarshipGirl\tool\ImgMaster.py
"""

import os
from queue import Full
import cv2
from PIL import Image
from tool.Img import Img


class ImgMaster:
    "图片管理与导入，用于脚本将用到的大量ui图片"
    _srcImg = "./img"
    _imgDict = {}

    def __init__(self):
        "遍历图像目录，创建单个图片对象并装入字典"
        paths = os.walk(self._srcImg)
        for path, dir_lst, file_lst in paths:
            for file_name in file_lst:
                imgSrc = os.path.join(path, file_name)
                img = Img(file_name, imgSrc)
                self._imgDict.update({file_name: img})

    def getImg(self, imgName: str) -> Img:
        imgName = imgName + ".png"
        return self._imgDict[imgName]
