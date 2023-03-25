str = input()
count = 0
ind = 0
if str.count('f') == 0:
    print('-2')
elif str.count('f') == 1:
    print('-1')
else:
    for i in range(len(str)):
        if str[i] == 'f':
            ind += 1
            if ind == 2:
                print(i)