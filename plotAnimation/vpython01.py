# -*- coding: utf8 -*- # 匯入視覺化套件
from vpython import * #產⽣生⼀一個寬400像素，⾼高400像素的3度空間以進⾏行行繪圖
# scene = display(width=400, height=400,center=vector(0,0.06,0)) #產⽣生⼀一個扁長形⽅方塊，當做是地板
floor = box(pos=vector(0,0,0), length=0.3, height=0.005, width=0.1)
#產⽣生⼀一個正立⽅方物體
cube = box(pos=vector(0, 0.05/2, 0), length=0.05, height=0.05, width=0.05)
#讓物體運動
while cube.pos.x < 0.1:
    rate(100)
    cube.pos.x = cube.pos.x + 0.001