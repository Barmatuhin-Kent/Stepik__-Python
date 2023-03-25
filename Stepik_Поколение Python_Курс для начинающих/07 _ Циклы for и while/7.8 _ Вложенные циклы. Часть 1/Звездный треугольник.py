from math import ceil
n = int(input())
middle = ceil(n / 2 + 1)
for i in range(1, middle):
    print(i * '*')
for i in range(middle - 2, 0, -1):
    print(i * '*')