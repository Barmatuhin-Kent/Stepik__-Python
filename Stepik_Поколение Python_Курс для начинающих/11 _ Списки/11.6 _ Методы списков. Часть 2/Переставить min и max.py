numbers = input().split()
min_element = numbers.index(min(numbers, key=int))
max_element = numbers.index(max(numbers, key=int))
numbers[min_element], numbers[max_element] = numbers[max_element], numbers[min_element]
print(' '.join(numbers))