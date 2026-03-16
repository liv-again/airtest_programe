# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
auto_setup(__file__)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

start_app('com.hexin.plat.android.ZhongyuanSecurity')
print("start...")
poco = AndroidUiautomationPoco()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/hx_page_bottom_bar").offspring(text="交易").click()
time.sleep(2)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/button_dynamic_login").click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/weituo_edit_account").set_text("7113121")
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/weituo_edit_trade_password").set_text("123000")
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/weituo_btn_login").click()
if poco(text="请申请安全登录证书").exists():
    poco(text="去申请").click()
    time.sleep(1)
    poco(text="确定提交").click()
if poco(text="温馨提示").exists():
    poco(text="继续登录").click()
    
if poco(text="系统信息").exists():
    print("登录失败")
    raise exception("登录失败，请确认原因")

#  基础菜单遍历
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_buy").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_sale").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_withdrawal").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_search").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_holdings").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_trasfer_accounts").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_trade_today").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_twt_today").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/v_new_stock_purchase").click()
time.sleep(2)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))
