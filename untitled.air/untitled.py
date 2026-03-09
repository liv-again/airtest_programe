# -*- encoding=utf8 -*-
__author__ = "20305"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app('com.hexin.plat.android.ZhongyuanSecurity')
if exists(Template(r"tpl1772468859749.png", record_pos=(-0.002, 0.031), resolution=(1080, 2376))):
    touch(Template(r"tpl1772468934645.png", record_pos=(-0.001, 0.672), resolution=(1080, 2376)))

touch(Template(r"tpl1772469500556.png", record_pos=(-0.2, 0.981), resolution=(1080, 2376)))
touch(Template(r"tpl1772469517607.png", record_pos=(0.079, -0.906), resolution=(1080, 2376)))
touch(Template(r"tpl1772468995117.png", record_pos=(-0.37, -0.78), resolution=(1080, 2376)))
touch(Template(r"tpl1772469540503.png", record_pos=(-0.315, -0.505), resolution=(1080, 2376)))
touch(Template(r"tpl1772469003110.png", record_pos=(-0.393, -0.894), resolution=(1080, 2376)))
#touch(Template(r"tpl1772469556457.png", record_pos=(0.374, -0.648), resolution=(1080, 2376)))
poco(resourceId='com.hexin.plat.android.ZhongyuanSecurity:id/tv_more')[0].click()
swipe(Template(r"tpl1772469679879.png", record_pos=(-0.368, 0.544), resolution=(1080, 2376)), vector=[-0.0569, -0.3386])

touch(Template(r"tpl1772469701615.png", record_pos=(-0.369, 0.963), resolution=(1080, 2376)))
touch(Template(r"tpl1772469003110.png", record_pos=(-0.393, -0.894), resolution=(1080, 2376)))
touch(Template(r"tpl1772469003110.png", record_pos=(-0.393, -0.894), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469031503.png", record_pos=(0.003, 0.172), resolution=(1080, 2376)), vector=[-0.0752, -0.2986])
touch(Template(r"tpl1772469032711.png", record_pos=(-0.146, -0.761), resolution=(1080, 2376)))
touch(Template(r"tpl1772469751849.png", record_pos=(-0.284, -0.174), resolution=(1080, 2376)))
touch(Template(r"tpl1772469044547.png", record_pos=(-0.383, -0.888), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469047800.png", record_pos=(-0.195, 0.588), resolution=(1080, 2376)), vector=[-0.0404, -0.3503])
swipe(Template(r"tpl1772469050080.png", record_pos=(-0.184, 0.561), resolution=(1080, 2376)), vector=[-0.0404, -0.2869])
touch(Template(r"tpl1772469051995.png", record_pos=(0.349, 0.083), resolution=(1080, 2376)))
touch(Template(r"tpl1772469053811.png", record_pos=(-0.427, -0.881), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469057372.png", record_pos=(-0.109, 0.59), resolution=(1080, 2376)), vector=[-0.0128, -0.2669])
swipe(Template(r"tpl1772469058593.png", record_pos=(-0.111, 0.509), resolution=(1080, 2376)), vector=[-0.0385, -0.3211])
swipe(Template(r"tpl1772469059848.png", record_pos=(-0.133, 0.634), resolution=(1080, 2376)), vector=[-0.0073, -0.3361])
swipe(Template(r"tpl1772469061989.png", record_pos=(-0.056, 0.463), resolution=(1080, 2376)), vector=[-0.033, -0.226])
touch(Template(r"tpl1772469067928.png", record_pos=(-0.019, -0.717), resolution=(1080, 2376)))
touch(Template(r"tpl1772469073404.png", record_pos=(0.356, -0.511), resolution=(1080, 2376)))
touch(Template(r"tpl1772469077667.png", record_pos=(-0.429, -0.906), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469084223.png", record_pos=(-0.157, 0.548), resolution=(1080, 2376)), vector=[-0.0073, -0.402])
swipe(Template(r"tpl1772469085717.png", record_pos=(-0.137, 0.586), resolution=(1080, 2376)), vector=[-0.0642, -0.3328])
touch(Template(r"tpl1772469087373.png", record_pos=(0.306, -0.671), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469090021.png", record_pos=(0.206, 0.05), resolution=(1080, 2376)), vector=[-0.5725, 0.01])
touch(Template(r"tpl1772469091358.png", record_pos=(0.194, -0.429), resolution=(1080, 2376)))
swipe(Template(r"tpl1772469093171.png", record_pos=(0.098, 0.025), resolution=(1080, 2376)), vector=[-0.5266, 0.01])
swipe(Template(r"tpl1772469097854.png", record_pos=(-0.161, 0.683), resolution=(1080, 2376)), vector=[0.0092, -0.3987])
touch(Template(r"tpl1772469099248.png", record_pos=(-0.101, 0.263), resolution=(1080, 2376)))
touch(Template(r"tpl1772469100361.png", record_pos=(0.072, 0.27), resolution=(1080, 2376)))
touch(Template(r"tpl1772469103261.png", record_pos=(-0.137, 0.706), resolution=(1080, 2376)))
touch(Template(r"tpl1772469105774.png", record_pos=(-0.396, -0.913), resolution=(1080, 2376)))


