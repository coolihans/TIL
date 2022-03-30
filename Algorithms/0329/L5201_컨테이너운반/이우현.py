import sys
sys.stdin = open('input.txt')


def get_maximum_loads(containers, trucks):
    trucks.sort(reverse=True)                   # 내림차순 정렬
    containers.sort(reverse=True)               # 내림차순 정렬
    moved = [0] * N                             # 옮긴 화물인지 확인할 체크리스트
    loads = 0                                   # 옮긴 화물의 총 무게
    for i in range(M):                          # 트럭을 돌면서,
        j = 0
        while j < N:                            # 옮긴 화물이 아니고, 트럭의 적재 용량 이하라면,
            if not moved[j] and trucks[i] >= containers[j]:
                moved[j] = 1                    # 옮긴 화물 체크!
                loads += containers[j]          # 총 무게 갱신
                break
            j += 1                              # 조건에 안맞으면 다음 화물 검사

    return loads


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    ans = get_maximum_loads(containers, trucks)
    print(f'#{tc} {ans}')



