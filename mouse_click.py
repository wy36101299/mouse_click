from pymouse import PyMouse
from time import sleep

m = PyMouse()
sleep(5)
x=969
y=581
a = 1
while a == 1:
    m.click(x,y)#移動到(x,y)並且點擊
    sleep(0.1)
    p = m.position() #獲取目前位置
    if not 900<p[0]<1000: #x座標不在 900~1000內 離開迴圈
        break