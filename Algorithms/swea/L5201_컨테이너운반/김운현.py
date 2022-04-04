import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    W = list(map(int, input().split()))  # 화물의 무게
    T = list(map(int, input().split()))  # 트럭의 적재용량

    weight = sorted(W, reverse=True)
    volume = sorted(T, reverse=True)
    result = [0 for i in range(M)]

    for i in range(N):  # 화물
        for j in range(M):  # 트럭
            if weight[i] <= volume[j]:
                if not result[j]:
                    result[j] = weight[i]
                    break

    print(f'#{tc} {sum(result)}')