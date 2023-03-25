count = 0
proizv = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        proizv *= x
        count += 1
if count > 0:
    print(count)
    print(proizv)
else:
    print('NO')