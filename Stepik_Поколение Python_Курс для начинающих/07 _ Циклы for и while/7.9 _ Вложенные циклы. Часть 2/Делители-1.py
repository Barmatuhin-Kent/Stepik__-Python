a, b = int(input()), int(input())
num = a

max_sum = 0
for number in range(a, b + 1):
    sum = 0
    for delitel in range(1, number + 1):
        if number % delitel == 0:
            sum += delitel
    if sum >= max_sum:
        max_sum, num = sum, number
print(num, max_sum)