import sys
sys.stdin = open('input2.txt')

width, height = map(int, input().split())
x, y = map(int, input().split())
N = int(input())
'''
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
time = 0
x_direction = 0
y_direction = 1
while time < N:
    x = x + dxs[x_direction]
    y = y + dys[y_direction]
    if y == 0 or y == height:
        y_direction = (y_direction + 2) % 4
    if x == 0 or x == width:
        x_direction = (x_direction + 2) % 4
    time += 1
print(x, y)
'''
# 시간 초과 코드

surplus_x, surplus_y = width-x, height-y
if N <= surplus_x:
    x_dis = x + N
if N <= surplus_y:
    y_dis = y + N
else:
    if ((N-surplus_x) // width) % 2 == 0:
        x_dis = width - (N - surplus_x) % width
    else:
        x_dis = (N - surplus_x) % width

    if ((N-surplus_y) // height) % 2 == 0:
        y_dis = height - (N - surplus_y) % height
    else:
        y_dis = (N - surplus_y) % height
print(x_dis, y_dis)