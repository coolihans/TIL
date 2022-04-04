import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))       # N개
    trucks = list(map(int, input().split()))        # M개

    weights.sort(reverse=True)      # 큰 것부터 욱여넣으려고
    trucks.sort(reverse=True)

    already = [0]*M     # 화물을 탑재했는지 여부
    answer = 0

    for weight in weights:
        for idx, truck in enumerate(trucks):
            if truck >= weight and already[idx] == 0:   # 화물을 싣기 여유롭고 아직 싣지 않은 트럭이라면
                already[idx] = 1
                answer += weight
                break

    print(f"#{tc} {answer}")
