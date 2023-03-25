from math import *

a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d > 0:
    x1 = (-b - sqrt(d)) * 0.5 / a
    x2 = (-b + sqrt(d)) * 0.5 / a
    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
elif d == 0:
    print(-b * 0.5 / a)
else:
    print('Нет корней')