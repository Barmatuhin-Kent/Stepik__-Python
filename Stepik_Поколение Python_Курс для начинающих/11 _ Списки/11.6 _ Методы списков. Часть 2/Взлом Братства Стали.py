n = input()
n = int(n[1:])
lst = []

for i in range(n):
    temp = input().split('#')[0]
    temp = temp.rstrip()
    lst.append(temp)
print(*lst, sep='\n')