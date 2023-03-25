number = int(input())
small = 9
large = 0
while number != 0:
    if number % 10 > large:
        large = number % 10
    if number % 10 < small:
        small = number % 10
    number //= 10
print('Максимальная цифра равна', large)
print('Минимальная цифра равна', small)