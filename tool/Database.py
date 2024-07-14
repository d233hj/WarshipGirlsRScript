"""
作者: d233hj
创建日期: <2024-07-14  02:56:53>
最后编辑时间: <2024-07-14  03:01:46>
最后编辑人员: d233hj
FilePath: \WarshipGirl\tool\database.py
"""

import json


class Database:
    _dataSrc = "./data/"

    def __init__(self) -> None:
        self.data = {"runComplete": True}

    def writeDb(self):
        with open(self._dataSrc + "data.json", "w") as json_file:
            json.dump(self.data, json_file, indent=4)

    def loadDb(self):
        with open(self._dataSrc + "data.json", "r") as json_file:
            self.data = json.load(json_file)
        return self.data
