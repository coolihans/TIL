N, M, V = map(int, input().split())

matrix = [[0]*(N+1) for i in range(N+1)]

#방문한곳체크기록할 리스트
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

# 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
for i in range(M):
  a, b =map(int, input().split())
  matrix[a][b] = matrix[b][a] = 1

