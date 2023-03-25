a, b, x, y = int(input()), int(input()), int(input()), int(input())
if a - x == b - y or a + b == x + y or a == x or b == y:
    print('YES')
else:
    print('NO')