n = int(input())
last_digit = n % 10
digit_3 = 0
count_last_digit = 0
count_even_digit = 0
sum_digit = 0
proizv = 1
count_0_5 = 0

while n > 0:
    temp_last_digit = n % 10
    if temp_last_digit == 3:
        digit_3 += 1
    if temp_last_digit == last_digit:
        count_last_digit += 1
    if temp_last_digit % 2 == 0:
        count_even_digit += 1
    if temp_last_digit > 5:
        sum_digit += temp_last_digit
    if temp_last_digit > 7:
        proizv *= temp_last_digit
    if temp_last_digit == 0 or temp_last_digit == 5:
        count_0_5 += 1
    n //= 10
print(digit_3)
print(count_last_digit)
print(count_even_digit)
print(sum_digit)
print(proizv)
print(count_0_5)