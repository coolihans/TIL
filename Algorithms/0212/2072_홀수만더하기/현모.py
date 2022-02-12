import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    odd_sum = 0
    numbers = list(map(int, input().split()))
    for number in numbers:
        if number%2 == 1:
            odd_sum += number

    print(f'#{tc} {odd_sum}')
