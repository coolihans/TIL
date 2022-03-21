# from sys import stdin
import sys
sys.stdin = open("input.txt")

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
max_height_idx = -1

# in sequence
for seq in range(N-1, 0, -1):
    for x in range(seq):
        if matrix[x][0] > matrix[x+1][0]:
            matrix[x][0], matrix[x+1][0] = matrix[x+1][0], matrix[x][0]
            matrix[x][1], matrix[x+1][1] = matrix[x+1][1], matrix[x][1]

# highest
for i in range(N):
    if matrix[i][1] > max_height:
        max_height = matrix[i][1]
        max_height_idx = i

# left
left_max = max_height_idx
left_edge = []
while left_max != 0:
    sub_max = -1
    for j in range(left_max):
        if matrix[j][1] > sub_max:
            sub_max = matrix[j][1]
            left_max = j
    left_edge.append(matrix[left_max])

left = len(left_edge)  # 나중에 edge에서 highest idx 알기 위해 기록

# right
right_max = max_height_idx
right_edge = []
while right_max != N-1:
    sub_max = -1
    for k in range(right_max+1, N):
        if matrix[k][1] > sub_max:
            sub_max = matrix[k][1]
            right_max = k
    right_edge.append(matrix[right_max])

# area
edge = []
# left_edge는 순서의 반대대로 쌓였을 거라 다시 차례대로 pop해서 넣어준다
for n in range(len(left_edge)):
    edge.append(left_edge.pop())

edge.append(matrix[max_height_idx])
edge.extend(right_edge)
# 여기까지 edge 차례대로 넣어서 완성

edge_max_idx = left  # 아까 highest 기록했던 거 가져와서 넣는다
area = 0
# 꼭지에 대해서만 면적이 바뀌므로 거길 기준으로 그 앞을 계산해준다고 생각하면 된다
for l in range(edge_max_idx):
    area += (edge[l+1][0]-edge[l][0])*edge[l][1]

for r in range(edge_max_idx+1, len(edge)):
    area += (edge[r][0]-edge[r-1][0])*edge[r][1]

area += edge[edge_max_idx][1]

print(area)
