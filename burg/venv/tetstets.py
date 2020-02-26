import math

h = 39000  # 初始高度

v = 0  # 初速
g = -9.8  # 重力場視為固定
m = 110  # Baumgartner及其裝備之質量
t = 0  # 初始時間
a = 0.7322  # 阻力係數與迎風截面積之乘積

a_new = 140

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


while True:
    h = 38969  # 初始高度

    v = 0  # 初速
    g = -9.8  # 重力場視為固定
    m = 110  # Baumgartner及其裝備之質量
    t = 0  # 初始時間
    a = 0.7322  # 阻力係數與迎風截面積之乘積
    dt = 0.01
    #t = 0
    a_new += 0.01
    while True:

        if h < 2440:  # 開傘後
            v = v + (g + f(v, a_new, h) / m) * dt
        else:  # 開傘前之下墜過程
            #at = t
            v = v + (g + f(v, a, h) / m) * dt

        h = h + v * dt
        t = t + dt

        if h < 1363:  # 落地
            break
    if t>543:
        break
    #print(t, a_new)

print(t, a_new)
