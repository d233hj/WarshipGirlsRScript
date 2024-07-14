'''
作者: d233hj
创建日期: <2024-07-13  17:20:31>
最后编辑时间: <2024-07-14  15:55:38>
最后编辑人员: d233hj
FilePath: \WarshipGirl\main.py
'''
"""
作者: d233hj
创建日期: <2024-07-13  17:20:31>
最后编辑时间: <2024-07-13  17:20:51>
最后编辑人员: d233hj
FilePath: \WarshipGirl\test.py
"""

from mod.WarshipGirl import WarshipGirl

warshipGirl = WarshipGirl()
warshipGirl.zhangshu20240712(200, "E2", True)


"""
adb = AdbTool()

img1 = cv2.imread("./img/gamecenter.png")
print(img1)
adb.apper_to_click(img1)
paths = os.walk(r".\tool")
for path, dir_lst, file_lst in paths:
    for file_name in file_lst:
        print(os.path.join(path, file_name))
        print(os.path.getsize(os.path.join(path, file_name)))
"""
