lower = -10 ** 6
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > lower:
            lower = x
if s == 0:
    print('NO')
else:
    print(s)
    print(lower)