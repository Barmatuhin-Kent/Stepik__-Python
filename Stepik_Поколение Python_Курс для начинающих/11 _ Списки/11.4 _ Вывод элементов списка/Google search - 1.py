n = int(input())
lst = []
for i in range(n):
    lst.append(input())
request = input()
for str in lst:
    if request.lower() in str.lower():
        print(str)