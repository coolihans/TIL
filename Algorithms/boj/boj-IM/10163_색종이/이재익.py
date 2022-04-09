import sys
sys.stdin = open('input3.txt')

# 입력의 첫 번째 줄에는 색종이의 장수를 나타내는 정수 N (1 ≤ N ≤ 100)이 주어진다.
# 이어서 N장의 색종이에 관한 입력이 각 색종이마다 한 줄씩 차례로 주어진다.
# 색종이가 놓이는 평면은 가로 최대 1001칸, 세로 최대 1001칸으로 구성된 격자 모양이다.
# 격자의 각 칸은 가로, 세로 길이가 1인 면적이 1인 정사각형이다.
# 색종이가 놓인 상태는 가장 왼쪽 아래 칸의 번호와 너비, 높이를 나타내는 네 정수로 표현한다.
# (1,4)가 가장 왼쪽 아래에 있고 너비 3, 높이 2이므로 1 4 3 2로 표현한다.

# 입력에서 주어진 순서에 따라 N장의 색종이를 평면에 놓았을 때,
# 입력에서 주어진 순서대로 각 색종이가 보이는 부분의 면적을 한 줄에 하나씩 하나의 정수로 출력한다.
# 만약 색종이가 보이지 않는다면 정수 0을 출력한다.

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

M = [[0]*1001 for _ in range(1001)]
for i in range(N):
    x = 1000 - P[i][1] #왼쪽 아래 x축 좌표
    y = P[i][0] #왼쪽 아래 y축 좌표
    cnt = [[] for _ in range(N)]
    for j in range(1000-P[i][1], 1000-P[i][1]-P[i][3], -1): # row
        for k in range(P[i][0], P[i][0]+P[i][2]): #col
            M[j][k] = i+1
for i in range(N):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if M[j][k] == i+1:
                cnt += 1
    print(cnt)