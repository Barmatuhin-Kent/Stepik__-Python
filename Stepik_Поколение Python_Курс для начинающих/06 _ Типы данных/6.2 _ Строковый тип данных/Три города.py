a, b, c = input(), input(), input()
min = min(len(a), len(b), len(c))
max = max(len(a), len(b), len(c))
if min == len(a):
    print(a)
elif min == len(b):
    print(b)
elif min == len(c):
    print(c)
if max == len(a):
    print(a)
elif max == len(b):
    print(b)
elif max == len(c):
    print(c)