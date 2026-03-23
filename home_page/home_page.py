# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")

### 未登录手机号

### 遍历九宫格

gridViews=poco(name="android.widget.FrameLayout")
for grid in gridViews :
    grid.click()
    time.sleep(1)
    keyevent("BACK")

### 资讯跳转
poco(text="资讯").click()
time.sleep(1)
poco(text="快讯").click()
time.sleep(1)
poco(text="机会").click()
time.sleep(1)
poco(text="自选").click()
time.sleep(1)
poco(text="要闻").click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_title")[0].click()
keyevent("BACK")
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/iv_go_back").click()

### 全部应用跳转
poco(text="全部应用").click()

### 滑动
while not poco(text="我是有底线的~"):
    swip((600,1900),(600,600))
poco(text="关注").click()
try:
    swip((1000,1300),(200,1300))
    assert poco(text="快讯").attr("selected")== True
    assert poco(text="关注").attr("selected")== False
    swip((200,1300),(1000,1300))
    assert poco(text="快讯").attr("selected")== False
    assert poco(text="关注").attr("selected")== True
except AssertionError as e :
    print(e,"首页左右滑动校验失败")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)