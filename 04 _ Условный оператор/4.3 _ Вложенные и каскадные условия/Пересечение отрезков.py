a, b, x, y = int(input()), int(input()), int(input()), int(input())
if a < x and b < y and b < x or a > x and b > y and a > y:
    print('пустое множество')
elif a < x and b < y and b == x:
    print(b)
elif a > x and b > y and a == y:
    print(a)
elif a < x and b <= y:
    print(x, b)
elif x < a and y <= b:
    print(a, y)
elif x >= a and b < y:
    print(x, b)
elif a >= x and y < b:
    print(a, y)
elif a < x and b > y:
    print(x, y)
elif a > x and b < y:
    print(a, b)
elif a == x and b == y:
    print(a, b)