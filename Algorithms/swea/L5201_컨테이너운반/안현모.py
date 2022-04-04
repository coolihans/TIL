import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    # 내림차순 정렬
    wi = sorted(wi, reverse=True)
    ti = sorted(ti, reverse=True)
    used_truck = []
    answer = 0
    # 트럭당 한개만 운반
    for i in range(N):
        for j in range(M):
            if wi[i] <= ti[j] and j not in used_truck:
                used_truck.append(j)
                answer += wi[i]
                break
    print(f'#{tc} {answer}')
