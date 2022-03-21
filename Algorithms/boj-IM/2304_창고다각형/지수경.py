N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
graph.sort()
height = max(graph, key= lambda x:x[1])  # 최고 높이
for i in range(len(graph)):  # 최고 높이의 막대기 위치 찾기
    if graph[i][1] == height[1]:
        top = i
        break

result = 0
max = graph[0]
for idx in range(1,top+1):  # top 막대기 왼쪽 막대기들
    if graph[idx][1] > max[1]:
        result += max[1] * (graph[idx][0] - max[0])
        max = graph[idx]

max = graph[-1]
for idx in range(N-1,top-1,-1):  # top 막대기 오른쪽 막대기들
    if graph[idx][1] >= max[1]:
        result += max[1] * (max[0]-graph[idx][0])
        max = graph[idx]

print(result+height[1])  # 왼쪽 넓이 + 오른쪽 넓이 + top막대기 높이 * 1
