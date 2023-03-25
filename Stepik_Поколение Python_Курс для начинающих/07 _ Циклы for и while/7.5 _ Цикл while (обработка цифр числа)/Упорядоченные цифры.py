num = int(input())
high = True
temp = num % 10

while num != 0:
    if num % 10 < temp:
        high = False
    temp = num % 10
    num //= 10

print('YES' if high == True else 'NO')