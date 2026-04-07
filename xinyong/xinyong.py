# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")
start_app('com.hexin.plat.android.ZhongyuanSecurity')
poco = AndroidUiautomationPoco()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/hx_page_bottom_bar").offspring(text="交易").click()
time.sleep(2)

poco(text="融资融券").click()
poco(text="登录").click()
if poco(text="请先登录普通交易账号！").exists(): 
    poco(text="确定").click()

### 登录普通交易该如何处理，直接结束任务还是跳转去登录
   
# 807000840
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/weituo_edit_account").set_text("807000840")
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/weituo_edit_trade_password").set_text("123000")
poco(text="融资融券登录").click()

poco(text="融资买入").click()
poco(desc="返回").click()

poco(text="担保品买入").click()
poco(desc="返回").click()

poco(text="融券卖出").click()
poco(desc="返回").click()

poco(text="担保品卖出").click()
poco(desc="返回").click()

poco(text="撤单").click()
poco(desc="返回").click()

poco(text="信用持仓").click()
poco(desc="返回").click()

###担保品划转
poco(text="担保品划转").click()
poco(text="担保品转入").click()
poco(desc="返回").click()
poco(text="担保品转出").click()
poco(desc="返回").click()
poco(text="担保品撤单").click()
poco(desc="返回").click()
poco(text="担保品查询").click()
poco(desc="返回").click()
poco(desc="返回").click()

###资产负债
poco(text="资产负债").click()
poco(text="证券持仓").click()
poco(text="融资负债").click()
poco(text="融券负债").click()
poco(text="其他负债").click()
poco(text="综合查询").click()
poco(desc="返回").click()

###银证转账
poco(text="银证转账").click()
poco(text="转出").click()
poco(text="转入").click()
poco(text="查询").click()
poco(desc="返回").click()

###查询
poco(text="查询")
menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for menu_name in menu:
    menu_name.click()
    poco(desc="返回").click()
poco(desc="返回").click()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)