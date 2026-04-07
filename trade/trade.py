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
if poco(text="清算提醒通知").exists():
    poco(text="确认").click()
    
### 清算提醒
if poco(text="清算提醒通知").exists() :
    poco(text="确认").click()
#  基础菜单遍历
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_buy").click() #买
time.sleep(2)
poco(desc="返回").click()

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_sale").click() #卖
time.sleep(2)
poco(desc="返回").click()

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_withdrawal").click() #撤
time.sleep(2)
poco(desc="返回").click()

### 跳转查询，遍历查询
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_search").click()
time.sleep(2)
search_menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for search_item in search_menu:
    search_item.click()
    time.sleep(2)
    if poco(desc="返回").exists():
        poco(desc="返回").click()
    else:
        poco(name="android.widget.ImageView")[0].click()
poco(desc="返回").click()

poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_holdings").click() #持仓
time.sleep(2)
poco(name="android.widget.ImageView")[0].click()

#银证转账
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_transfer_accounts").click() 
time.sleep(2)
poco(text="转入").click()
poco(text="转出").click()
poco(text="查询").click()
if poco(text="没有转账记录。").exists():
    poco(text="确定").click()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_history_transfer_record").click()
time.sleep(2)
poco(name="android.widget.ImageView").click() #返回
if poco(text="没有转账记录。").exists():
    poco(text="确定").click()
poco(name="android.widget.ImageView").click() #返回

###当日成交
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_trade_today").click() 
time.sleep(2)
poco(desc="返回").click()

###当日委托
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_wt_today").click() 
time.sleep(2)
poco(desc="返回").click()
###新股
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/v_new_stock_purchase").click() 
time.sleep(1)
if poco(text="申购风险提示").exists():
    poco(text="我已知晓").click()
    #待缴款 
poco(text="待缴款").click()
poco(text="中签待缴款查询").parent().parent().offspring(name="android.widget.ImageView").click()
    #新股日历
poco(text="新股日历").click()
poco(desc="返回").click()
    #申购查询
poco(text="申购查询").click()
menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_menu_text")
for item in menu:
    item.click()
    poco(name="android.widget.ImageView")[0].click()
poco(name="android.widget.ImageView")[0].click() #返回按钮
poco(name="android.widget.ImageView")[0].click() #返回按钮

###基金交易
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/fl_title").offspring(text="基金交易").click()
#### 开放式基金
poco(text="开放式基金").click()
menu_list=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for item in menu_list:
    item.click()
    time.sleep(1)
    poco(desc="返回").click()
swipe((500,1800),(500,1300))
poco(text="基金信息查询").click()
time.sleep(1)
poco(desc="返回").click()
poco(desc="返回").click()

jj_menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for i in range(1,6):
    jj_menu[i].click()
    menu_list=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
    for item in menu_list:
        item.click()
        time.sleep(1)
        poco(desc="返回").click()
poco(desc="返回").click()

###银证转账
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/fl_title").offspring(text="基金交易").click()
poco(desc="返回").click()

###多银行存管
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/fl_title").offspring(text="多银行存管").click()
dyh_menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for item in dyh_menu:
    item.click()
    poco(desc="返回").click()
poco(desc="返回").click()

### 国债逆回购
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/fl_title").offspring(text="国债逆回购").click()
poco(text="更多").click()
poco(text="收起").click()
poco(text="1天期")[0].click()
time.sleep(1)
poco(name="android.widget.ImageView")[0].click() # 返回按钮
time.sleep(1)
poco(text="委托/撤单").click()
poco(text="成交记录").click()
poco(name="android.widget.ImageView")[0].click() # 返回按钮

swipe((600,2000),(600,600))
###会员中心
poco(text="会员中心test").click()
keyevent("BACK")

###港股通
poco(text="港股通").click()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ggt_buy").click()
poco(desc="返回").click()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ggt_sale").click()
poco(desc="返回").click()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ggt_withdrawals").click()
poco(desc="返回").click()
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ggt_chicang").click()
poco(desc="返回").click()
poco(text="查询").click()
ggt_query_menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for item in ggt_query_menu :
    item.click()
    timm.sleep(1)
    poco(desc="返回").click()
poco(text="投票及公司行为申报").click()
ggt_vote_menu=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/menu_name")
for item in ggt_vote_menu:
    item.click()
    time.sleep(1)
    poco(desc="返回").click()
poco(desc="返回").click()
time.sleep(1)
poco(desc="返回").click()

### 新三板
poco(text="新三板").click()
ll_types=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_type")
for ll_type in ll_types:
    ll_type.click()
    time.sleep(1)
    poco(desc="返回").click()

tv_titles=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_title")
for title in tv_titles:
    title.click()
    time.sleep(1)
    poco(desc="返回").click()
poco(desc="返回").click()

### 债券交易
poco(text="债券交易").click()
##匹配成交
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_buy").click()
time.sleep(1)
poco(text="匹配成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_sale").click()
time.sleep(1)
poco(text="匹配成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_cancel").click()
time.sleep(1)
poco(text="匹配成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_position").click()
time.sleep(1)
poco(text="匹配成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()
time.sleep(1)
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/ll_query").click()
menu_list=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_menu_text")
for tv_menu_text in menu_list:
    tv_menu_text.click()
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/hx_page_root").child(name="android.widget.RelativeLayout").offspring(name="android.widget.ImageView")[0].click()
poco(text="匹配成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()
##点击成交
poco(text="点击成交").click()
poco(text="回复").click()
poco(text="行情").click()
poco(text="撤单").click()
poco(text="查询").click()
poco(text="委托查询").click()
poco(text="回复").click()
poco(text="报价").click()
poco(text="委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="成交查询").click()
poco(text="成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="点击成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()

##询价查询
poco(text="询价成交").click()
poco(text="报价申报").click()
poco(text="报价回复").click()
poco(textMatches=".*撤单.*").click() 
poco(text="报价").click()
poco(text="询价").click()
poco(text=" 查询 ").click() #撤单和查询一样，前一个空格后一个空格凑成4字符

poco(text="委托查询").click()
poco(text="报价申报").click()
poco(text="报价回复").click()
poco(text="询价申报").click()
poco(text="委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()

poco(text="成交查询").click()
poco(text="成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="询价成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()

##协商成交
poco(text="成交申报").click()
poco(text="成交回复").click()
poco(textMatches=".*撤单.*").click() 
poco(text=" 查询 ").click() #撤单和查询一样，前一个空格后一个空格凑成4字符
poco(text="委托查询").click()
poco(text="委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="成交查询").click()
poco(text="成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="协商成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()

##竞买成交
poco(text="竞买成交").click()
poco(text="发起申报").click()
poco(text="应价申报").click()
poco(textMatches=".*撤单.*").click() 
poco(text="发起申报").click()
poco(text="应价申报").click()
poco(text="预约申报").click()
poco(text=" 查询 ").click() #撤单和查询一样，前一个空格后一个空格凑成4字符
poco(text="竞买预约信息查询").click()
poco(text="竞买预约信息查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="竞买应价信息查询").click()
poco(text="竞买应价信息查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="委托查询").click()
poco(text="发起申报").click()
poco(text="应价申报").click()
poco(text="预约申报").click()
poco(text="委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="成交查询").click()
poco(text="成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="竞买成交").parent().parent().offspring(name="android.widget.ImageView")[0].click()

##交易员信息维护
poco(text="交易员信息维护").click()
poco(text="交易员信息维护").parent().parent().offspring(name="android.widget.ImageView")[0].click()

poco(text="债券交易").parent().parent().offspring(name="android.widget.ImageView")[0].click()

###北交所可转债
poco(text="北交所可转债").click()

###条件单
poco(text="条件单").click()
poco(text="条件单").parent().parent().child().child(name="android.widget.ImageView").click()

###基金交易
poco(text="基金交易").click()
poco(desc="返回").click()

###行情测试
poco(text="行情测试").click()
poco(text="交易").click()

###先行赔付
poco(text="先行赔付").click()
poco(text="申报结果查询").click()
poco(text="先行赔付结果查询").parent().parent().offspring(name="android.widget.ImageView").click()
poco(text="先行赔付").parent().parent().offspring(name="android.widget.ImageView").click()

###网络投票
poco(text="网络投票").click()
poco(text="股东大会").click()
poco(text="投票查询").click()
poco(text="深圳投票查询").click()
poco(text="上海投票查询").click()
poco(text="投票查询").parent().parent().offspring(name="android.widget.ImageView").click()
poco(text="股东大会").parent().parent().offspring(name="android.widget.ImageView").click()
poco(text="先行赔付受偿申报").click()
poco(text="申报结果查询").click()
poco(text="先行赔付结果查询").parent().parent().offspring(name="android.widget.ImageView").click()
poco(text="先行赔付").parent().parent().offspring(name="android.widget.ImageView").click()
poco(text="网络投票").parent().parent().offspring(name="android.widget.ImageView").click()

#滑动
swipe((600,2000),(600,600))

###OTC&天天汇利
poco(text="OTC").click()
poco(text="交易").click()
poco(text="天天汇利").click()
poco(text="交易").click()

###可转债转股
poco(text="可转债转股").click()
poco(desc="返回").click()

###要约收购
poco(text="要约收购").click()
poco(name="预受要约").click()
poco(name="预受要约").parent().offspring(name="android.view.View").click()
poco(name="解除要约").click()
poco(name="解除要约").parent().offspring(name="android.view.View").click()
poco(name="要约收购").parent().offspring(name="android.view.View").click()

###盘后固定价格交易
poco(text="盘后固定价格交易").click()
poco(text="卖出").click()
poco(text="撤单").click()
poco(text="买入").click()
poco(text="查询").click()
poco(text="盘后固定价格当日委托查询").click()
poco(text="盘后固定价格当日委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="盘后固定价格当日成交查询").click()
poco(text="盘后固定价格当日成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="盘后固定价格历史委托查询").click()
poco(text="盘后固定价格历史委托查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="盘后固定价格历史成交查询").click()
poco(text="盘后固定价格历史成交查询").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="盘后定价交易").parent().parent().offspring(name="android.widget.ImageView")[0].click()

###修改密码
poco(text="修改密码").click()
poco(text="修改交易密码").click()
poco(text="修改交易密码").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(text="修改资金密码").click()
poco(text="修改资金密码").parent().parent().offspring(name="android.widget.ImageView")[0].click()
poco(desc="返回").click()

###模拟大赛
poco(text="模拟大赛").click()
poco(text="模拟炒股").parent().children()[1].click()

swipe((600,2000),(600,600))

###活期产品&定期产品
poco(text="活期产品").click()
poco(text="交易").click()
poco(text="定期产品").click()
poco(text="交易").click()
poco(text="基金专区").click()
poco(text="交易").click()
poco(text="高端理财").click()
poco(text="交易").click()

###退出登陆
poco(text="退出登录").click()
poco(text="确认").click()