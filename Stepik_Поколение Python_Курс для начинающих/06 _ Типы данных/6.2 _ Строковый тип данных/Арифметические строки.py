a, b, c = len(input()), len(input()), len(input())
min = min(a, b, c)
max = max(a, b, c)
middle = a + b + c - max - min
print('YES' if middle - min == max - middle else 'NO')