a = int(input())
if a % 2 == 1:
    print('YES')
elif 2 <= a <= 4 and a % 2 == 0 or a > 20 and a % 2 == 0:
    print('NO')
elif 6 <= a <= 20 and a % 2 == 0:
    print('YES')