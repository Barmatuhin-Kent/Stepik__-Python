a, b = int(input()), int(input())

for number in range(a, b + 1):
    simple = 0
    for delitel in range(1, number + 1):
        if number % delitel == 0:
            simple += 1
    if simple == 2:
        print(number)