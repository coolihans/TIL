import sys
sys.stdin = open('input.txt')


def bfs():
    visited = [False for _ in range(V+1)]

    to_visits = [S]

    while to_visits:
        current = to_visits.pop(0)
        if not visited[current]:
            visited[current] = True
            print(current, end='=>')
            if current == G:
                return visited[G]
        to_visits += graph[current]


T = int(input())

for tc in range(1, T+1):
    # V 정점의 개수, E 간선의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    print(bfs())



