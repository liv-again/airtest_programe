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

###一键打新
poco(text="一键打新").click()
if poco(text="申购风险提示").exists():
    poco(text="我已知晓").click()
    
poco(text="待缴款").click()
poco(text="中签待缴款查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()

poco(text="申购查询").click()
poco(text="新股新债申购配号查询").click()
poco(text="新股新债中签查询").click()
poco(text="新股新债申购委托查询").click()
poco(text="申购查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()

poco(text="新股日历").click()
poco(text="打新日历").parent().parent().offspring(name="android.widget.ImageView")[0].click()

poco(text="北证A股").click()
poco(text="新股一键申购").click()
poco(text="公开发行申购").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="询价委托查询").click()
poco(text="询价委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="申购委托查询").click()
poco(text="申购委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="询价结果查询").click()
poco(text="询价结果查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="申购结果查询").click()
poco(text="申购结果查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="北交所新股申购").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(name="android.widget.ImageView")[0].click()


###四种还款还券
poco(text="直接还款").click()
poco(desc="返回").click()
poco(text="直接还券").click()
poco(desc="返回").click()
poco(text="卖券还款").click()
poco(desc="返回").click()
poco(text="买券还券").click()
poco(desc="返回").click()

###盘后交易
poco(text="创业板盘后固定价格交易").click()
poco(text="卖出").click()
poco(text="撤单").click()
poco(text="查询").click()
menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_menu_text")
for item in menu :
    item.click()
    poco(name="android.widget.ImageView")[0].click()
poco(name="android.widget.ImageView")[0].click()

swipe([700,2000],[700,500])

###合约展期
poco(text="合约展期").click()
poco(text="合约展期申请查询").click()
poco(desc="返回").click()
poco(text="合约展期批量申请").click()
poco(desc="返回").click()
poco(desc="返回").click()

###修改密码
poco(text="修改密码").click()
poco(text="修改交易密码").click()
poco(desc="返回").click()
poco(text="修改资金密码").click()
poco(desc="返回").click()
poco(desc="返回").click()

poco(text="条件单").click()
poco(name="android.widget.ImageView")[1].click()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)