import sys

sys.stdin = open("input3.txt")

N = int(input())

if N <= 1:
    print(1)
else:
    numbers = list(map(int, input().split()))

    maximum = 0
    count = 0

    for i in range(N-1):
        if numbers[i] <= numbers[i+1]:
            count += 1
        else:
            maximum = count if count > maximum else maximum
            count = 0
    maximum = count if count > maximum else maximum
    count = 0

    for i in range(N-1, 0, -1):
        if numbers[i] <= numbers[i-1]:
            count += 1
        else:
            maximum = count if count > maximum else maximum
            count = 0
    maximum = count if count > maximum else maximum
    count = 0

    print(maximum+1)






