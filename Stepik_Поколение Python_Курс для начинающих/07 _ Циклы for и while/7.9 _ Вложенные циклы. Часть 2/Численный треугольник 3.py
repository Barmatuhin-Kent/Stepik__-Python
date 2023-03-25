n = int(input())
num = 1
row = 0
for i in range(1, n + 1):
    row += 1
    for j in range(row):
        print(num, end=' ')
        num += 1
    print()