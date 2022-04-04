import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = 2**N
    if M % n == n - 1:
        result = "ON"
    else:
        result = "OFF"

    print(f'#{tc} {result}')
