# -*- coding: UTF-8 -*-


from mymods1 import *


pit_cut_line(1)


area=cal_triangle_area(3,4,5)
if area <= 0 :
    print("Error")
else:
    print('Area=%d'%area)
