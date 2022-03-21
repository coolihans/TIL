# from sys import stdin
import sys
sys.stdin = open("input.txt")

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
opposite = [5, 3, 4, 1, 2, 0]  # 한 면을 정했을 때 맞은편 idx
max_sum = 0  # 답

# 제일 처음 주사위 면을 정하면 사실 모두가 정해진다
# 그래서 그 경우의 수에 대한 최대값를 구한다
for i in range(6):
    total = 0
    bottom = matrix[0][i]
    top = matrix[0][opposite[i]]
    for j in range(N):  # 모든 층에 대하여
        temp_list = [0, 1, 2, 3, 4, 5, 6]  # 여섯 면: idx 헷갈리지 않으려고 처음에 0을 넣음
        max_num = 0  # 해당 층에서 위아래 뺀 네 개의 수 중 가장 최대값
        for k in temp_list:
            if k != bottom and k != top:  # 여섯 면 중 위아래가 아니면
                if k > max_num:
                    max_num = k
        # 해당 층의 가장 최대값을 더해준다
        total += max_num
        # 가장 상위층은 그 다음 위층을 고려할 필요가 없으므로 break
        if j == N-1:
            break
        # 위층을 위한 bottom top 세팅
        for n in range(6):
            if matrix[j+1][n] == top:  # top과 같은 위층 면을 찾으면
                bottom = matrix[j+1][n] 
                top = matrix[j+1][opposite[n]]
                break
    # 첫 번째 주사위의 해당 면에 의해 정해진 total들의 최댓값을 구함
    if total > max_sum:
        max_sum = total

print(max_sum)
