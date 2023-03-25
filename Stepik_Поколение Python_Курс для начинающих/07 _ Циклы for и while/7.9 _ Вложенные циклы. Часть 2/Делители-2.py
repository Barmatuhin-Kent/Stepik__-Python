n = int(input())

for number in range(1, n + 1):
    sum_del = 0
    for delitel in range(1, number + 1):
        if number % delitel == 0:
            sum_del += 1
    print(number, '+' * sum_del, sep='')