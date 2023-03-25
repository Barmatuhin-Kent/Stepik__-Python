n = int(input())
large, largest = 0, 0

for i in range(n):
    num = int(input())
    if num > largest:
        largest, large = num, largest
    elif num > large:
        large = num
print(largest)
print(large)