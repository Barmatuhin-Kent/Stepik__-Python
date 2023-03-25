str = input()

middle = str[str.index('h') + 1:str.rindex('h')]
new_str = str[:str.index('h') + 1] + middle[::-1] + str[str.rindex('h'):]
print(new_str)