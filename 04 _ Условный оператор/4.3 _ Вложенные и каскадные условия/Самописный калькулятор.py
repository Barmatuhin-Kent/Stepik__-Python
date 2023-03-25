a, b, str = int(input()), int(input()), input()
if str == '+':
    print(a + b)
elif str == '-':
    print(a - b)
elif str == '*':
    print(a * b)
elif str == '/':
    if b != 0:
        print(a / b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')