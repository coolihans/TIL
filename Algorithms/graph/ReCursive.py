import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True

    for new_v in graph[v]:
        if not visited[new_v]:
            dfs(new_v)


T = int(input())

for tc in range(1, T+1):
    # V 정점의 개수, E 간선의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())
    visited = [False for _ in range(V+1)]

    dfs(S)
    print(visited[G])