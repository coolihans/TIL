import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    # V => 정점의 개수, E => 간선의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    # 간선 정보만 들어옴 => 간선의 개수 만큼 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    print(graph)

