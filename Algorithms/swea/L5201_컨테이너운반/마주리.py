import sys
sys.stdin = open('input.txt')


def max_transport():
    w.sort()
    t.sort()
    total = 0
    for _ in range(M):      # 트럭의 최대 개수만큼 반목
        if not w:           # 컨테이너가 남아있지 않을 때
            break
        if w[-1] <= t[-1]:  # 화물의 무게가 트럭의 적재용량보다 작거나 같을 때
            total += w.pop()
            t.pop()
        else:               # 화물의 무게가 남은 트럭의 적재용량보다 클 때
            w.pop()
    return total


T = int(input())

for tc in range(1, T + 1):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int, input().split())
    # N개의 화물의 무게 w
    w = list(map(int, input().split()))
    # M개의 트럭의 적재용량 t
    t = list(map(int, input().split()))

    print(f'#{tc} {max_transport()}')
