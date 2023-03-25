n = int(input())
lst_n = []
for i in range(n):
    lst_n.append(input())
k = int(input())
lst_k = []
for i in range(k):
    zapros = input()
    lst_k.append(zapros.lower())
for element in lst_n:
    counter = 0
    for zapros in lst_k:
        if zapros in element.lower():
            counter += 1
            if counter == len(lst_k):
                print(element)