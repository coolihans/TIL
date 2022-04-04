import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    max_weight = 0
    cargo_weights = list(map(int, input().split()))
    truck_weights = list(map(int, input().split()))  # 여기까지 입력받기

    while True:
        heaviest_cargo = max(cargo_weights)  # 가장 무거운 화물과, 가장 큰 차량부터 뽑아내기
        heaviest_truck = max(truck_weights)
        if heaviest_truck >= heaviest_cargo:  # 만약 가장 큰 차에 가장 무거운 화물을 실을 수 있다면,
            max_weight += heaviest_cargo
            cargo_weights.remove(heaviest_cargo)  # 화물 출고
            truck_weights.remove(heaviest_truck)  # 차량 출발

        elif heaviest_cargo > heaviest_truck:  # 반대로 가장 큰 차에도 가장 큰 화물을 실을 수 없다면,
            cargo_weights.remove(heaviest_cargo)  # 화물 재고행

        if not cargo_weights or not truck_weights:  # 트럭이 다 소진되거나 화물이 다 소진된다면, 브레이크
            break

    print(f'#{tc} {max_weight}')  # 출력
