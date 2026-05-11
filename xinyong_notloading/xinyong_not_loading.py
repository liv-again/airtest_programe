# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/10AF6A0D7X0082P?cap_method=ADBCAP&touch_method=MAXTOUCH&",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")
### 登录
poco(text="登录").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

### 基础交易
count=len(poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/textView"))
note_count=0
for i in range(count):
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/textView").click()
    if poco(text="请先登录普通交易账号！").exists() :
        note_count+=1
        poco(text="确定").click()
assert note_count==10

### 一键打新
poco(text="一键打新").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

### 直接还款
poco(text="直接还款").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

### 卖券还款
poco(text="卖券还款").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

### 直接还券
poco(text="直接还券").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

### 买券还券
poco(text="买券还券").click()
assert poco(text="请先登录普通交易账号！").exists()
poco(text="确定").click()

swipe([550,2000],[550,800])

### 列表菜单
count=len(poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name"))
note_count=0
for i in range(count):
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name").click()
    if poco(text="请先登录普通交易账号！").exists() :
        note_count+=1
        poco(text="确定").click()
assert note_count==4

# generate html report
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)