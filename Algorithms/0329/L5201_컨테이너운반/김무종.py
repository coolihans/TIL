import sys
sys.stdin = open('input.txt')

def choice(truck):
    tmp = 0
    for i in range(N):
        if containers[i] <= truck and i not in used:
            used.append(i)
            tmp = containers[i]
            break
    return tmp

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    used = []
    answer = 0
    for truck in trucks:
        answer += choice(truck)
    print(f'#{tc}', answer)