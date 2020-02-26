import math
import os

h = 39000  # 初始高度

v = 0  # 初速
g = -9.8  # 重力場視為固定
m = 110  # Baumgartner及其裝備之質量
t = 0  # 初始時間
a = 0.8395  # 阻力係數與迎風截面積之乘積


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
print('Height is', h)

while True:

    if t > 264:  # 開傘後
        v = -12
    else:  # 開傘前之下墜過程
        v = v + (g + f(v, a, h) / m) * dt

    h = h + v * dt
    t = t + dt
    if t < 264:
        print('_' * int(39 - (h / 1000)) + "B" + ' ' * int((h / 1000)+1) + '| V:', int(v), 't:', str(int(t)) + ' '*20, end='\r')
    else:
        print('_' * int(37 - (h / 1000)) + "(>B" + ' ' * int((h / 1000)+1) + '| V:', int(v), 't:', str(int(t)), end='\r')
    if h < 0:  # 落地
        break
print('_' * int(37 - (h / 1000)) + "(>B" + ' ' * int((h / 1000)+1) + '| V:', int(v), 't:', str(int(t)))
print('Landing!!!!')
print('_'*20)
print('landing in '+str(int(t))+'(sec)')  # 落地時間
print('actually is', t, 'sec.')
os.system('pause')
