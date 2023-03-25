total = 0
for i in range(10):
    num = int(input())
    if num % 2 == 1:
        total += 1
print('YES' if total == 0 else 'NO')