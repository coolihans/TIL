import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    for number in numbers:
        total += number

    result = round(total/len(numbers))

    print(f'#{tc} {result}')
