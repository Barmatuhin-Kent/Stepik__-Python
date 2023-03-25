numbers = [8, 9, 10, 11]
numbers[1] = 17
lst = [4, 5, 6]
numbers.extend(lst)
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)