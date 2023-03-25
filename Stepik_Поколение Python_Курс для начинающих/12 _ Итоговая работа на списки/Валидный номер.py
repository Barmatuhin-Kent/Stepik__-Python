number = [i for i in input().split('-') if i != '7']
if len(number) == 3:
    print('YES' if (len(number[0]) == 3 and number[0].isdigit()) and (len(number[1]) == 3 and number[1].isdigit()) and (len(number[2]) == 4 and number[2].isdigit()) else 'NO')
else:
    print('NO')