m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, float(m))
    m = m + m * p / 100