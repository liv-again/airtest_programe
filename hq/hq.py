# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
#from function import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

start_app('com.hexin.plat.android.ZhongyuanSecurity')
# script content
print("start...")
poco = AndroidUiautomationPoco()
if exists(Template(r"tpl1773071084423.png", record_pos=(-0.002, 0.081), resolution=(1080, 2376))) :
    touch(Template(r"tpl1773071097091.png", record_pos=(-0.004, 0.434), resolution=(1080, 2376)))



### 切换行情 ###
touch(Template(r"tpl1772729181893.png", record_pos=(-0.195, 0.979), resolution=(1080, 2376)))

touch(Template(r"tpl1772729215503.png", record_pos=(0.082, -0.904), resolution=(1080, 2376)))

### 切换全球tab ###
touch(Template(r"tpl1772729307704.png", record_pos=(-0.379, -0.781), resolution=(1080, 2376)))
assert_exists(Template(r"tpl1772900692358.png", record_pos=(0.011, -0.706), resolution=(1080, 2376)), "存在国内指数模块")
try:
    price_old=poco(
       text="上证指数"
   ).parent().parent().offspring(
       resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_stock_price"
   ).get_text()
except:
    print("poco 断开")
    time.sleep(2)
    price_old=poco(
       text="上证指数"
   ).parent().parent().offspring(
       resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_stock_price"
   ).get_text()
time.sleep(5)
try:
    price_new=poco(
       text="上证指数"
   ).parent().parent().offspring(
       resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_stock_price"
   ).get_text()
except:
    print("poco 断开")
    time.sleep(2)
    price_new=poco(
       text="上证指数"
   ).parent().parent().offspring(
       resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_stock_price"
   ).get_text()
    
try:
    assert price_old != price_new ,"行情未刷新" 
except AssertionError as e :
    print(e)

touch(Template(r"tpl1772901330290.png", record_pos=(-0.322, -0.581), resolution=(1080, 2376)))
touch(Template(r"tpl1772901356115.png", record_pos=(-0.408, -0.928), resolution=(1080, 2376)))

### 跳转更多 ###
poco(text="国内指数").parent().offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/tv_more").click()

assert_exists(Template(r"tpl1772901709953.png", record_pos=(-0.002, -0.921), resolution=(1080, 2376)), "跳转国内指数更多页正确")

#### 这一段需要重构

block=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0]
data_old=block.offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/item_content").child().attr("name")
time.sleep(5)
data_new=block.offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/item_content")child().attr("name")
try:
    assert data_new != data_old ,"行情未刷新"
except AssertionError as e :
    print(e)



touch(Template(r"tpl1772901356115.png", record_pos=(-0.408, -0.928), resolution=(1080, 2376)))

### 跳转A股 ###
touch(Template(r"tpl1772904199210.png", record_pos=(-0.125, -0.813), resolution=(1080, 2376)))

# 这个函数有风险，可能会陷入死循环

temp=0
while not poco(text="上证指数").exists() and temp <10:
    print("当前页面无上证指数，尝试上划寻找")
    swipe((500,800),(500,1500))
    sleep(1)
    temp +=1
poco(text="上证指数").click()


time.sleep(1)
touch(Template(r"tpl1772901356115.png", record_pos=(-0.408, -0.928), resolution=(1080, 2376)))  #返回
                                                                                            
###刷新###
price_old=poco(text="上证指数").parent().offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/index_price").attr[text]
time.sleep(5)
price_new=poco(text="上证指数").parent().offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/index_price").attr[text]
try:
    assert price_new != price_old ,"行情未刷新"
except AssertionError as e :
    print(e)
                                                                                            
swipe((500,1500),(500,800))                                                                                            
touch(Template(r"tpl1772905627159.png", record_pos=(-0.175, -0.357), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772905642288.png", record_pos=(-0.369, -0.357), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772905652417.png", record_pos=(0.383, -0.478), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772905555244.png", record_pos=(-0.025, -0.693), resolution=(1080, 2376)))         
time.sleep(1)
touch(Template(r"tpl1772905559371.png", record_pos=(-0.052, -0.693), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))

while not poco(text="模块编辑").exists():
    swipe((500,1500),(500,800))
    sleep(1)
poco(text="模块编辑").click()
touch(Template(r"tpl1773564073668.png", record_pos=(-0.419, -0.929), resolution=(1080, 2376)))              
                                                                                            
                                                                                            
                                                                                            
                                                                                            
                                                                                            

###跳转板块###            
touch(Template(r"tpl1772971112832.png", record_pos=(0.002, -0.717), resolution=(1080, 2376)))
ZF_list=find_all(Template(r"tpl1773071985129.png", record_pos=(-0.206, 0.048), resolution=(1080, 2376)))
touch(ZF_list[0])
time.sleep(1)
touch(ZF_list[0])
ZS_list=find_all(Template(r"tpl1773071987496.png", record_pos=(-0.012, 0.058), resolution=(1080, 2376)))
touch(ZS_list[0])
touch(Template(r"tpl1773071988630.png", record_pos=(-0.012, 0.058), resolution=(1080, 2376)))
LB_list=find_all(Template(r"tpl1773072159922.png", record_pos=(0.168, -0.512), resolution=(1080, 2376)))
touch(LB_list[0])
touch(Template(r"tpl1773072173779.png", record_pos=(0.168, -0.519), resolution=(1080, 2376)))
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/view_bankuai_tablayout_item")[0].click()
touch(Template(r"tpl1773072416484.png", record_pos=(-0.408, -0.94), resolution=(1080, 2376)))

touch(Template(r"tpl1773072432034.png", record_pos=(0.378, -0.185), resolution=(1080, 2376)))
touch(Template(r"tpl1773072011358.png", record_pos=(-0.441, -0.931), resolution=(1080, 2376)))
while not poco(text="模块编辑").exists():
    swipe((500,1500),(500,800))
    sleep(1)
poco(text="模块编辑").click()
touch(Template(r"tpl1773564073668.png", record_pos=(-0.419, -0.929), resolution=(1080, 2376))) 
    
    
    


###跳转科创板###
touch(Template(r"tpl1772971102555.png", record_pos=(0.339, -0.714), resolution=(1080, 2376)))
touch(Template(r"tpl1772971187799.png", record_pos=(0.115, -0.6), resolution=(1080, 2376)))
touch(Template(r"tpl1772971197964.png", record_pos=(-0.331, -0.603), resolution=(1080, 2376)))
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/curveview").click()
touch(Template(r"tpl1772901356115.png", record_pos=(-0.408, -0.928), resolution=(1080, 2376))) 
swipe((500,1500),(500,800))
touch(Template(r"tpl1772905627159.png", record_pos=(-0.175, -0.357), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772905642288.png", record_pos=(-0.369, -0.357), resolution=(1080, 2376)))
time.sleep(1)

### 跳转港股###
touch(Template(r"tpl1772971564805.png", record_pos=(0.123, -0.815), resolution=(1080, 2376)))
if exists(Template(r"tpl1773072565072.png", record_pos=(0.001, -0.028), resolution=(1080, 2376))):
    touch(Template(r"tpl1773072576748.png", record_pos=(-0.002, 0.171), resolution=(1080, 2376)))

touch(Template(r"tpl1772971628147.png", record_pos=(0.316, -0.622), resolution=(1080, 2376)))
                    ###需要一个刷新###
touch(Template(r"tpl1772971685380.png", record_pos=(0.0, -0.809), resolution=(1080, 2376)))
touch(Template(r"tpl1772971696587.png", record_pos=(0.337, -0.817), resolution=(1080, 2376)))

touch(Template(r"tpl1772901356115.png", record_pos=(-0.408, -0.928), resolution=(1080, 2376))) 

touch(Template(r"tpl1772972726503.png", record_pos=(-0.139, 0.358), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772972742485.png", record_pos=(0.073, 0.361), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772972760271.png", record_pos=(0.338, 0.362), resolution=(1080, 2376)))
time.sleep(1)

### 跳转其他 ###
touch(Template(r"tpl1772972810493.png", record_pos=(0.377, -0.818), resolution=(1080, 2376)))

hq_other_lables=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/label_text")
for i in renge(len(hq_other_lables)):
    hq_other_lables[i].click()
    time.sleep(1)
    touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
    time.sleep(1)
    
while not poco(text="退市整理可转债").exists():
    swipe((500,1500),(500,800))
    sleep(1)

zq_lables=poco(text="退市整理可转债").parent().parent().offspring(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/label_text")
for i in renge(len(zq_lables)):
    zq_lables[i].click()
    time.sleep(1)
    touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
    time.sleep(1)
    
                                                                                            
### d单个列表跳转
touch(Template(r"tpl1772975449272.png", record_pos=(-0.314, -0.157), resolution=(1080, 2376)))
assert check_listitem_redirect()                                                                                            
### 还需要校验刷新
                       

### 跳转个股详情

check_listitem_redirect(3)
touch(Template(r"tpl1772976389594.png", record_pos=(0.176, -0.924), resolution=(1080, 2376)))
touch(Template(r"tpl1772976392000.png", record_pos=(-0.173, -0.933), resolution=(1080, 2376)))
handle=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/fenshi_headline_view")
handle.click()
handle.click()
five_buy_sale_new=poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/five_buy_sale_new")
five_price_old=five_buy_sale_new.attr(desc)
time.sleep(5)
five_price_new=five_buy_sale_new.attr(desc)
try:
    assert five_price_new != five_price_old,"行情未刷新"
except AssertionError as e :
    print(e)
swipe((500,1500),(500,800))
touch(Template(r"tpl1772977063980.png", record_pos=(0.331, 0.541), resolution=(1080, 2376)))
touch(Template(r"tpl1773589875098.png", record_pos=(-0.285, -0.424), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1773589880815.png", record_pos=(-0.157, -0.425), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1773589901202.png", record_pos=(-0.424, -0.428), resolution=(1080, 2376)))


touch(Template(r"tpl1772983191695.png", record_pos=(0.137, 0.663), resolution=(1080, 2376)))
time.sleep(3)
touch(Template(r"tpl1773589270819.png", record_pos=(0.475, -0.157), resolution=(2376, 1080)))
time.sleep(3)
swipe((500,1500),(500,800))
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/view_newsgroup_item")[0].click() # 点击新闻
touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
touch(Template(r"tpl1772977091172.png", record_pos=(-0.249, 0.201), resolution=(1080, 2376)))
touch(Template(r"tpl1772977100820.png", record_pos=(-0.083, 0.193), resolution=(1080, 2376)))
poco(resourceId="pub_new").child(name="android.view.View")[0].clcik()
touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
touch(Template(r"tpl1772977109854.png", record_pos=(0.121, 0.196), resolution=(1080, 2376)))
poco(resourceId="myf10").offspring(text="更多").click()
touch(Template(r"tpl1772977116816.png", record_pos=(0.319, 0.198), resolution=(1080, 2376)))
poco(text="更多")[0].click()
touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
touch(Template(r"tpl1772976503843.png", record_pos=(0.423, 0.049), resolution=(1080, 2376)))
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/view_newsgroup_item").click()
touch(Template(r"tpl1772905562011.png", record_pos=(-0.447, -0.933), resolution=(1080, 2376)))
touch(Template(r"tpl1772983575185.png", record_pos=(0.206, 0.976), resolution=(1080, 2376)))
touch(Template(r"tpl1772983584269.png", record_pos=(0.206, 0.976), resolution=(1080, 2376)))
touch(Template(r"tpl1772983595786.png", record_pos=(0.402, 0.977), resolution=(1080, 2376)))
touch(Template(r"tpl1772983604349.png", record_pos=(-0.257, 0.811), resolution=(1080, 2376)))
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))
touch(Template(r"tpl1772983667053.png", record_pos=(-0.395, -0.417), resolution=(1080, 2376)))
touch(Template(r"tpl1772983821945.png", record_pos=(0.344, 0.96), resolution=(1080, 2376)))
touch(Template(r"tpl1773589452873.png", record_pos=(0.423, -0.931), resolution=(1080, 2376)))
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))
touch(Template(r"tpl1773589500717.png", record_pos=(-0.069, -0.931), resolution=(1080, 2376)))
touch(Template(r"tpl1773589533790.png", record_pos=(0.295, -0.764), resolution=(1080, 2376)))
touch(Template(r"tpl1773589557354.png", record_pos=(0.415, -0.557), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1773589582547.png", record_pos=(0.41, -0.413), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1773589696340.png", record_pos=(0.411, -0.28), resolution=(1080, 2376)))
time.sleep(1)
touch(Template(r"tpl1773589716504.png", record_pos=(0.411, -0.138), resolution=(1080, 2376)))
time.sleep(1)
swipe((800,500),(100,500))
touch((500,600))
touch(Template(r"tpl1772983618269.png", record_pos=(-0.452, -0.93), resolution=(1080, 2376)))
if exists(Template(r"tpl1773590013269.png", record_pos=(0.003, -0.341), resolution=(1080, 2376))):
    touch(Template(r"tpl1773590030623.png", record_pos=(0.006, -0.341), resolution=(1080, 2376)))
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/search_input_et").set_text("6000")
    add_btns=find_all(Template(r"tpl1773590286776.png", record_pos=(0.431, -0.789), resolution=(1080, 2376)))
    touch(add_btns[0])
    delete_btns=find_all(Template(r"tpl1773590378299.png", record_pos=(0.427, -0.79), resolution=(1080, 2376)))
    touch(delete_btns[0])
    touch(Template(r"tpl1773590409881.png", record_pos=(0.424, -0.926), resolution=(1080, 2376)))
touch(Template(r"tpl1773590058108.png", record_pos=(0.43, -0.928), resolution=(1080, 2376)))
poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/search_pagenavi_editview").set_text("688")
add_btns=find_all(Template(r"tpl1773590286776.png", record_pos=(0.431, -0.789), resolution=(1080, 2376)))
for btn in add_btns:    
    touch(btn)
delete_btns=find_all(Template(r"tpl1773590378299.png", record_pos=(0.427, -0.79), resolution=(1080, 2376)))
touch(delete_btns[0])
touch(Template(r"tpl1773590548116.png", record_pos=(0.42, -0.898), resolution=(1080, 2376)))
swip((500,1600),(500,800))
swip((800,600),(100,600))
try:
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0].long_click(duration=2)
    poco(text="置顶").click()
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0].long_click(duration=2)
    poco(text="置底").click()
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0].long_click(duration=2)
    poco(text="编辑所属分组").click()
    touch(Template(r"tpl1773591277670.png", record_pos=(0.0, 0.971), resolution=(1080, 2376)))
    poco(resourceId="com.hexin.plat.android.ZhongyuanSecurity:id/dragablelistviewitem")[0].long_click(duration=2)
    poco(text="删除").click()
except PocoNoSuchNodeException as e:
    print(e)



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
