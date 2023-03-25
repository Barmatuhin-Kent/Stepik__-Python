n = int(input())
digit = n % 10
while n != 0:
    digit = n % 10
    n //= 10
print(digit)