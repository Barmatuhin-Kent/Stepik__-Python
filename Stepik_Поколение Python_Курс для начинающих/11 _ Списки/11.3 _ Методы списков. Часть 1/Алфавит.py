str = []
x = 1
for i in range(97, 123):
    str.append(chr(i) * x)
    x += 1
print(str)