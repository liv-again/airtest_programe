# -*- encoding=utf8 -*-
__author__ = "zlq"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])


# script content
print("start...")
poco = AndroidUiautomationPoco()

if poco(text="交易").attr("selected") == False:
    poco(text="交易").click()

if poco(text="普通交易").attr("selected") == False:
    poco(text="普通交易").click()
    
### 交易登录
poco(text="交易登录").click()

    
    
    
    
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)