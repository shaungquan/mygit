import pyautogui
import time
import pyperclip
from test_case.gadget import weather_test


def openwx():
    pyautogui.hotkey("ctrl", "alt", "w")
    time.sleep(1)


# 接收信息的好友名字
def send_name(name):
    pyautogui.hotkey("ctrl","f")
    pyperclip.copy(name)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)
    pyautogui.hotkey("enter")


# 需要发送的信息
def send_msg(msg):
    time.sleep(1)
    pyperclip.copy(msg)
    pyautogui.hotkey("ctrl","v")

    pyautogui.hotkey("enter")


a = weather_test.weather()

datas = "定时消息，明日天气预报\n城市：{}\n日期：{}\n温度：{}\n天气：{}\n风向：{}\n昼夜温差：{}\n穿衣建议：{}\n\n\n请勿回复，此消息为机器人发送"\
    .format(a[0], a[1],a[2], a[3], a[4], a[6], a[5])
openwx()
send_name("懒猪猪")
send_msg(datas)
print(datas)
# print(weather_test.weather())
