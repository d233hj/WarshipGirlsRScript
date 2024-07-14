from tool.AdbTool import AdbTool
from tool.ImgMaster import ImgMaster
import time
import datetime
from tool.Database import Database
import func_timeout

adbTool = AdbTool()
imgMaster = ImgMaster()
print(adbTool.getMsg())
database = Database()


class WarshipGirl:
    _fightTime__ = 0
    _restTime__ = 0
    _startTime__ = 0

    def __init__(self) -> None:
        pass

    def zhangshu20240712(self, times: int, map: str, continues=False):
        "当期活动专用，出门点只打一次，刷战术 /n times :战斗次数 /n map :选择地图 /n continues :False或True 是否继续上次的任务"
        self._startTime__ = time.perf_counter()
        self._startTimeStr__ = datetime.datetime.now()
        try:
            database.loadDb()
            print(database.data)
            if continues and not database.data["runComplete"]:
                "自动恢复"
                try:
                    self._fightTime__ = database.data["restTime"]
                    self._restTime__ = database.data["restTime"]
                    map = database["map"]
                except BaseException as err:
                    print(err)
            else:
                self._fightTime__ = times
                self._restTime__ = times
        except BaseException as err:
            print(err)
        finally:
            self.selectMap(map)
            self.fightnomal()
            while 1:
                if self._restTime__ <= 0:
                    self.chetui()
                    break
                if not self.fightnow():
                    self._restTime__ = self._restTime__ - 1
                    "存储任务进度，下次自动恢复"
                    database.data.update(
                        {
                            "fightTime": self._fightTime__,
                            "restTime": self._restTime__,
                            "map": map,
                            "runComplete": False,
                        }
                    )
                    database.writeDb()
                    "计算当前时间和开始时间，估计预期结束时间"
                    timenow = time.perf_counter()
                    costtime = timenow - self._startTime__
                    futuretime = (
                        float(self._restTime__) / (self._fightTime__ - self._restTime__)
                    ) * costtime

                    hours = int(futuretime // 3600)
                    minutes = int((futuretime % 3600) // 60)
                    print(
                        "========# All Times:"
                        + str(self._fightTime__)
                        + " | The restTimes:"
                        + str(self._restTime__)
                        + "|| StartTime: <"
                        + str(self._startTimeStr__)
                        + ">  PreTime: <"
                        + str(hours)
                        + "h"
                        + str(minutes)
                        + "m>  #========"
                    )
                    continue
            database.data.update({"runComplete": True, "restTime": 0})
            database.writeDb()

    def selectMap(self, map):
        "选择地图和难度:E1,E2,E3..."
        map = "Map" + map
        if adbTool.apper_to_click(imgMaster.getImg("huodonT").getImg(), "huodonT"):
            pass
        for image in imgMaster._imgDict.keys():
            if adbTool.research_img(imgMaster.getImg(map).getImg()):
                break
            elif adbTool.apper_to_click(
                imgMaster.getImg("MapRight").getImg(), "MapRight"
            ):
                continue
            else:
                while adbTool.apper_to_click(imgMaster.getImg("MapLeft").getImg()):
                    pass

    def fightnomal(self):
        "战斗内逻辑，处理出征前进撤退"

        while 1:
            "进入开始出征界面"
            if adbTool.apper_to_click(imgMaster.getImg("huodonT").getImg(), "huodonT"):
                continue
            if adbTool.apper_to_click(
                imgMaster.getImg("jingjiQK").getImg(), "jingjiQK"
            ):
                continue

            if adbTool.apper_to_click(imgMaster.getImg("buchuli").getImg(), "buchuli"):
                continue

            if adbTool.research_img(imgMaster.getImg("kaishiCZ").getImg()):
                break

        while 1:
            "出征准备"
            if adbTool.apper_to_click(
                imgMaster.getImg("qijianDP").getImg(), "qijianDP"
            ):
                "旗舰大破"
                "出现大破，准备快修"
                while 1:
                    if adbTool.apper_to_click(
                        imgMaster.getImg("kuaisuXL").getImg(), "kuaisuXL"
                    ):
                        continue
                    if adbTool.apper_to_click(
                        imgMaster.getImg("quanbuXL").getImg(), "quanbuXL"
                    ):
                        break

            if adbTool.apper_to_click(imgMaster.getImg("dapoQX").getImg(), "dapoQX"):
                "出现大破，准备快修"
                while 1:
                    if adbTool.apper_to_click(
                        imgMaster.getImg("kuaisuXL").getImg(), "kuaisuXL"
                    ):
                        continue
                    if adbTool.apper_to_click(
                        imgMaster.getImg("quanbuXL").getImg(), "quanbuXL"
                    ):
                        break

            if adbTool.apper_to_click(
                imgMaster.getImg("kaishiCZ").getImg(), "kaishiCZ"
            ):
                continue

            if adbTool.research_img(imgMaster.getImg("qianjin").getImg()):
                break

    def fightnow(self, night=False):
        "出征中，不可修理"
        while 1:
            "正常出征进入战斗"
            if adbTool.apper_to_click(imgMaster.getImg("qianjin").getImg(), "qianjin"):
                continue
            if adbTool.research_img(
                imgMaster.getImg("kaishiCZ").getImg(),
            ):
                break
            if adbTool.research_img(imgMaster.getImg("zhen").getImg()):
                break

        while 1:
            "大破相关"
            if adbTool.apper_to_click(
                imgMaster.getImg("qijianDP").getImg(), "qijianDP"
            ):
                self.chetui()
                return False
            elif adbTool.apper_to_click(imgMaster.getImg("dapoQX").getImg(), "dapoQX"):
                self.chetui()
                return False
            if adbTool.apper_to_click(
                imgMaster.getImg("kaishiCZ").getImg(), "kaishiCZ"
            ):
                continue

            if adbTool.research_img(imgMaster.getImg("zhen").getImg()):
                break

        while 1:
            "战斗中及战斗结束"
            if night and adbTool.apper_to_click(
                imgMaster.getImg("zhuiji").getImg(), "zhuiji"
            ):
                continue
            if not night and adbTool.apper_to_click(
                imgMaster.getImg("fangqi").getImg(), "fangqi"
            ):
                continue

            if adbTool.research_img(imgMaster.getImg("zhen").getImg()):
                time.sleep(3)
                continue

            if adbTool.apper_to_click(
                imgMaster.getImg("zhandouJG").getImg(), "zhandouJG"
            ):
                break

        while 1:
            if adbTool.apper_to_click(
                imgMaster.getImg("zhandouJG").getImg(), "zhandouJG"
            ):
                continue
            if adbTool.research_img(imgMaster.getImg("qianjin").getImg()):
                break

    @func_timeout.func_set_timeout(120)
    def chetui(self):
        while 1:
            if adbTool.research_img(imgMaster.getImg("jingjiQK").getImg()):
                break
            if adbTool.apper_to_click(imgMaster.getImg("huodonT").getImg(), "huodonT"):
                continue
            if adbTool.apper_to_click(
                imgMaster.getImg("chetuiQR").getImg(), "chetuiQR"
            ):
                continue
            if adbTool.apper_to_click(imgMaster.getImg("chetui").getImg(), "chetui"):
                continue
            if adbTool.apper_to_click(imgMaster.getImg("chetui1").getImg(), "chetui1"):
                continue
