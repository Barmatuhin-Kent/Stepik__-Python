a = int(input())
if 1 <= a <= 36:
    if (1 <= a <= 10 or 19 <= a <= 28) and a % 2 == 0:
        print('черный')
    elif (11 <= a <= 18 or 29 <= a <= 36) and a % 2 != 0:
        print('черный')
    else:
        print('красный')
elif a == 0:
    print('зеленый')
else:
    print('ошибка ввода')