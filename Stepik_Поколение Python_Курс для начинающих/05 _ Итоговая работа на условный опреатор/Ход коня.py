a, b, x, y = int(input()), int(input()), int(input()), int(input())
if x == a + 1 and y == b + 2 or x == a + 1 and y == b - 2:
    print('YES')
elif x == a + 2 and y == b + 1 or x == a + 2 and y == b - 1:
    print('YES')
elif x == a - 1 and y == b + 2 or x == a - 1 and y == b - 2:
    print('YES')
elif x == a - 2 and y == b + 1 or x == a - 2 and y == b - 1:
    print('YES')
else:
    print('NO')