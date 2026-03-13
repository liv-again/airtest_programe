# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


# 函数写得还有问题，感觉需要加一下参数，
#列表数据刷新
def check_listitem_refresh():
    block=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0]
    data_old=block.offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/item_content").child().attr("name")
    time.sleep(5)
    data_new=block.offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/item_content").child().attr("name")
    return  data_new != date_old 

###列表数据跳转校验跳转是否正确
def check_listitem_redirect(n):
    block=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[n]
    listitem=block.offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/item_header").child()
    listitem_name=listitem.attr("name").split('#')[0]
    listitem.click()
    stock_name=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/navi_title").attr("text")
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/backButton").click()
    return stock_name == listitem_name
    
price_old=poco(
       text="上证指数"
   ).parent().parent().offspring(
       resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_stock_price"
   ).get_text()
print(price_old)