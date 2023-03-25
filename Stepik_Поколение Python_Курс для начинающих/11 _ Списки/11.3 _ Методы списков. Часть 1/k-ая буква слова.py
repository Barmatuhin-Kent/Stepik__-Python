n = int(input())
str = []
for i in range(n):
    str.append(input())
k = int(input())
for element in str:
    if len(element) >= k:
        print(element[k - 1], end='')