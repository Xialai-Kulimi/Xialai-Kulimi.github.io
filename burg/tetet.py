import os
import math
# from PIL
import numpy as np
import cv2


# # Create a black image
# img = np.zeros((512, 512, 3), np.uint8)
#
# # Draw a diagonal blue line with thickness of 5 px
# img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
#
# cv2.imshow('My Image', img)

# os.system('pause')

orin_p = open('BlankPic.jpg', 'rb')
new_p = open('NewPic.jpg', 'wb')
new_p.write(orin_p.read())
orin_p.close()
new_p.close()


img = cv2.imread('NewPic.jpg')


h = 38969  # 初始高度

v = 0  # 初速
g = -9.8  # 重力場視為固定
m = 110  # Baumgartner及其裝備之質量
t = 0  # 初始時間
a = 0.7322  # 阻力係數與迎風截面積之乘積
mv = 0

def T(h):  # 溫度對高度函數
    if h < 11000:
        return 288.14 - 0.00649 * h
    elif h > 25000:
        return 141.89 + 0.00299 * h
    else:
        return 216.64


def p(h):  # 氣壓對高度函數
    if h < 11000:
        return 101.29 * (T(h) / 288.08) ** 5.256
    elif h > 25000:
        return 2.488 * (T(h) / 216.6) ** (-11.388)
    else:
        return 22.65 * math.e ** (1.73 - 0.000157 * h)


def r(h):  # 密度對高度函數
    return p(h) / (0.2869 * T(h))


def f(v, a, h):  # 阻力函數
    return (1 / 2) * r(h) * v * v * a


dt = 0.001
print(h)
print(img.shape)
x0 = (0, img.shape[0]+int(v))

while True:

    if h < 2440:  # 開傘後
        v = v + (g + f(v, 140.6816, h) / m) * dt
    else:  # 開傘前之下墜過程
        mv = v
        v = v + (g + f(v, a, h) / m) * dt

    # if v < mv:
    #    mv = v
    h = h + v * dt
    t = t + dt

    if h < 1363:  # 落地
        break
    x1 = (int((38969-h)/35), img.shape[0]+int(v))
    img = cv2.line(img, x0, x1, (255, 0, 0), 3)
    x0 = x1

print(t)  # 落地時間
print(h)
print(v)
print(mv)
cv2.namedWindow('My Image')

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
