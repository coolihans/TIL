# import sys
# sys.stdin = open("input.txt")
#
#
#
# for tc in range(1, 11):
#     length, start = map(int, input().split())
#     lst = list(map(int, input().split()))
#     visited = []
#     con = {}
#     # 겹치는 거 제외
#     for i in range(0, length, 2):
#         if lst[i] not in con:
#             con[lst[i]] = []    # { 'lst[i]' : [] ....}
#         if lst[i+1] not in con[lst[i]]:
#             con[lst[i]].append(lst[i+1])    # { 'lst[i]' : [lst[i+1]] }
#
#     # print(con[3])

from collections import deque
import sys
sys.stdin = open('input.txt')


def setGraph(input_str):
    for i in range(n):
        if i % 2:
            _from = input_str[i - 1]
            _to = input_str[i]

            graph[_from].append(_to)


def bfs(start):
    queue = deque()
    visited[start] = True

    if graph[start]:
        for next in graph[start]:
            if not visited[next]:
                queue.append(next)
    else:
        return start

    while queue:
        r = len(queue)
        last = []

        for i in range(r):  # queue 의 갯수만큼
            now = queue.popleft()

            if not visited[now]:  # 실제로 연락이 들어가면
                visited[now] = True
                last.append(now)  # 마지막으로 연락받은 사람 목록에 추가
                for next in graph[now]:
                    if not visited[next]:
                        queue.append(next)

    return max(last)


for tc in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    visited = [False] * 101
    visited[0] = True

    input_str = list(map(int, input().split()))
    setGraph(input_str)

    print(f'#{tc} {bfs(start)}')
