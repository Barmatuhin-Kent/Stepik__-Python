n = int(input())
step = 0
for j in range(1, n + 1):
    step += 1
    for i in range(step):
        print(i+1, end='')
    for i in range(step, 1, -1):
        print(i-1, end='')
    print()