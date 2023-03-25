num, str = int(input()), input()
for c in str:
    ind = ord(c)
    if ind - num > 96:
        print(chr(ind - num), end='')
    else:
        print(chr(ind - num + 26), end='')