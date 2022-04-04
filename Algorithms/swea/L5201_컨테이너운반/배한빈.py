import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # max(containers)를 계속 비교
    # max(containers)를 담을 수 있는 트럭이 있다면 max(containers)랑 해당 트럭 remove
    # 없다면 max(containers)만 remove 하고 그 다음 max(containers)를 비교
    # containers 리스트가 빌 때까지 반복
    answer = 0
    while containers:
        for truck in trucks:
            if max(containers) <= truck:
                answer += max(containers)
                trucks.remove(truck)
                check = 1
                break
        containers.remove(max(containers))

    print(f'#{tc} {answer}')
