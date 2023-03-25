a, b, x, y = int(input()), int(input()), int(input()), int(input())
if (a % 2 == 1 and b % 2 == 1) and (x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1):
    print('YES')
elif (a % 2 == 0 and b % 2 == 0) and (x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1):
    print('YES')
elif (a % 2 == 0 and b % 2 == 1) and (x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0):
    print('YES')
elif (a % 2 == 1 and b % 2 == 0) and (x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0):
    print('YES')
else:
    print('NO')