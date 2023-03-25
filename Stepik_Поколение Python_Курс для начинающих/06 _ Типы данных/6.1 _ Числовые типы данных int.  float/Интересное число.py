num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
print('Число интересное' if max(a, b, c) - min(a, b, c) == a + b + c - max(a, b, c) - min(a, b, c) else 'Число неинтересное')