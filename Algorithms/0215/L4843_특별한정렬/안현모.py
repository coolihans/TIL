import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    number = input()
    num_list = list(map(int, input().split()))
    max_list = num_list.sort()
    result = []
    for i in range(10):         # 10개만 뽑기..
        if i % 2 == 0:
            result.append(num_list[-1-(i//2)])
        if i % 2 == 1:
            result.append(num_list[(i//2)])

    print(f'#{tc}', end=" ")
    print(*result)