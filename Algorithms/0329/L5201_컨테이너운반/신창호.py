import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    idx = answer = 0
    # 적재용량이 큰 트럭부터 차례로 적재용량하에 가장 무거운 컨테이너를 운반
    for truck in trucks:
        # 종료조건: 남은 컨테이너가 없는 경우
        if idx == N:
            break

        # 트럭에 담을 수 없는 무게면 넘어감
        while idx != N:
            if truck >= containers[idx]:
                answer += containers[idx]
                idx += 1
                break
            idx += 1
    print(f'#{tc}', answer)
