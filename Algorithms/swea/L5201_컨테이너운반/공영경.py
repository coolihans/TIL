import sys
sys.stdin = open('input.txt')

def get_weight(loads, trucks):
    # 트럭의 용량이 큰 순으로 정렬
    trucks.sort(reverse=True)

    # 옮길 수 있는 화물의 무게를 0으로 초기화
    weight = 0

    for truck in trucks:
        load = -1
        idx = -1
        # 트럭의 용량을 가장 많이 채울 수 있는 화물선택
        for i in range(len(loads)):
            if load <= loads[i] <= truck:
                load = loads[i]
                idx = i
        # 선택한 화물이 있다면
        if idx != -1:
            weight += load
            loads.pop(idx)
    
    return weight

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    loads = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    answer = get_weight(loads, trucks)
    print(f'#{tc+1} {answer}')
