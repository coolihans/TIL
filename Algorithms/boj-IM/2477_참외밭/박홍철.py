# ㄱ자이기에 가로 큰변, 세로 큰변, 가로 작은변1, 세로 작은변1, 가로 작은변2, 세로 작은변2의 돌림 혹은 대칭으로 수가 주어질 것이다.
# 밭의 넓이는 가로 큰변 * 세로 큰변 - 세로 작은변1 * 가로 작은변2 일 것이다.
# 여튼 가로 세로 제인 큰 변의 곱에서 그 큰변과 접하지 않은 작은 변의 곱을 빼면 된다!
# 가로 큰변과 세로 큰 변 위에서 이동한 방향은 6번의 움직임 중 1번 씩만 나온다
# 큰 변에서 2칸 떨어진 변은 무조건 움푹 패인 부분의 변!
import sys
sys.stdin = open("input.txt")

num_in_unit = int(input())

edges = [list(map(int, input().split())) for _ in range(6)]

big_edges = [0, 0]
small_edges = [0, 0]

for i in range(2):
    if edges[i][0] == edges[2+i][0]:
        big_edges[i] = edges[4+i][1]
        small_edges[i] = edges[1+i][1]
    else:
        if edges[i][1] > edges[2+i][1]:
            big_edges[i] = edges[i][1]
            small_edges[i] = edges[3+i][1]
        else:
            big_edges[i] = edges[2 + i][1]
            small_edges[i] = edges[(5+i)%6][1]

print(num_in_unit * ((big_edges[0] * big_edges[1]) - (small_edges[0] * small_edges[1])))



