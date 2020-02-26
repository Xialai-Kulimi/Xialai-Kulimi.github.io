import math
import os
import time

time.sleep(20)

h = 38969  # Initial height

v = 0  # Initial speed
g = -9.8  # The gravity field is considered fixed
m = 110  # The mass of Baumgartner and his equipment
t = 0  # Initial time
a = 0.7322  # The product of the coefficient of confrontation and the cross-sectional area of​the windward


def T(h):  # Temperature versus height function
    if h < 11000:
        return 288.14 - 0.00649 * h
    elif h > 25000:
        return 141.89 + 0.00299 * h
    else:
        return 216.64


def p(h):  # Air pressure versus height function
    if h < 11000:
        return 101.29 * (T(h) / 288.08) ** 5.256
    elif h > 25000:
        return 2.488 * (T(h) / 216.6) ** (-11.388)
    else:
        return 22.65 * math.e ** (1.73 - 0.000157 * h)


def r(h):  # Density versus height function
    return p(h) / (0.2869 * T(h))


def f(v, a, h):  # Resistance function
    return (1 / 2) * r(h) * v * v * a


dt = 0.001
print('Height is', h)

while True:

    if h < 2440:  # After opening the parachute
        v = v + (g + f(v, 140.6816, h) / m) * dt
    else:  # Before opening the parachute
        v = v + (g + f(v, a, h) / m) * dt

    h = h + v * dt
    t = t + dt

    if h > 2440:
        print('_' * int(39 - (h / 1000)) + "B" + ' ' * int((h / 1000)) + '| V:', int(v), 't:', str(int(t)) + ' '*20, end='\r')
    else:
        print('_' * int(37 - (h / 1000)) + "(>B" + ' ' * int((h / 1000)) + '| V:', int(v), 't:', str(int(t)) + ' '*20, end='\r')

    if h < 1363:  # Landing
        break
print('_' * int(37 - (h / 1000)) + "(>B" + ' ' * int((h / 1000)-1) + '| V:', int(v), 't:', str(int(t)) + ' '*20)
print('Landing!!!!')
print('landing in '+str(int(t))+'(sec)')  # Landing time
print('actually is', t, 'sec.')
os.system('pause')
