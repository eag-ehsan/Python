# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@ eagMouse  Ver:1.00 2022-18-8   @@@@@@
# @@@@@@ Created by Ehsan Ahmadi Gohari @@@@@@
# @@@@@@ Email: eag.ehsan@gmail.com     @@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@                                        @@
# @@    Functions:                          @@
# @@            moveMouse(x,y)              @@
# @@            click(x,y)                  @@
# @@                                        @@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def moveMouse(x,y):
    win32api.SetCursorPos((x,y))
