import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 노드의 수, 리프 노드의 수, 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    # 받은 리프 노드의 값 집어 넣기
    for _ in range(M):
        i, j = map(int, input().split())
        tree[i] = j
    # 하나 씩 뒤에서 부터 더하기
    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')

# n//2 = n + (n+1) = > 그냥 하나씩 넣으면 짝홀 구분 없이 할 수 있음

# subtree 같이 하면 다르게 할 수 있을 것 같다..
