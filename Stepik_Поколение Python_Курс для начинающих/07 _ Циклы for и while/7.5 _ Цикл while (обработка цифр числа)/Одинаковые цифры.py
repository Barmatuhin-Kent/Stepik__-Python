num = int(input())
number = True
digit = num % 10

while num != 0:
    if digit != num % 10:
        number = False
    digit = num % 10
    num //= 10
print('YES' if number == True else 'NO')