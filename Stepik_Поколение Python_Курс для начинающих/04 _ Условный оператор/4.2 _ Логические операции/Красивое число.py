x = int(input())
if 1 <= (x // 1000) <= 9 and ((x % 7) == 0 or (x % 17) == 0):
    print('YES')
else:
    print('NO')