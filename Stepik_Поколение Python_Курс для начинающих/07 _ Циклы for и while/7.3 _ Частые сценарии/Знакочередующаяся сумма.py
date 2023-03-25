total1 = 0
total2 = 0
n = int(input())
for i in range(1, n + 1, 2):
    total1 += i
for i in range(2, n + 1, 2):
    total2 += i
print(total1 - total2)