import sys
sys.stdin = open('input1.txt')

w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())


# x 좌표는 맞닥뜨릴때마다 오른쪽, 왼쪽으로 방향을 바꿔서 계속 움직일 뿐이고
# y 좌표도 벽에 맞닥뜨리면 방향을 바꿔서 계속 움직일 뿐이다.

# 맨 처음에는 무조건 오른쪽위(x도 오른쪽 방향, y도 위쪽 방향)으로 움직이므로 오른쪽 끝에 도달할 만큼의 값을 분자에서 빼준다.

if ((t - (w-p)) // w) % 2: # 몫이 홀수라면 몫만큼 나눴을 때
    # 현재 위치는 0이므로 0부터 다시 오른쪽으로 움직인 만큼이 x 좌표이다.
    x = ((t - (w-p)) % w)
else: # 몫이 짝수라면 몫만큼 나눴을 때
    # 현재 위치는 오른쪽 끝이므로 오른쪽 끝부터 다시 왼쪽으로 이동한 만큼이 x 좌표이다.
    x = w - ((t - (w-p)) % w)

if ((t - (h-q)) // h) % 2: # y좌표도 x좌표와 동일한 방식으로 구할 수 있다.
    y = ((t - (h-q)) % h)
else:
    y = h - ((t - (h-q)) % h)

print(x, y)
""" 시간초과 나는 방법
x = p
y = q

cnt = 0
direction = 0 # 0은 우상향, 1은 좌상향, 2는 좌하향, 3은 우하향

while cnt < t:

    if direction == 0: # 우상향
        if x < w and y < h: # 우상향 계속 될 때
            x = x+1
            y = y+1
        elif x == w and y < h: # 오른쪽 벽에 도달했을 때
            x = x-1
            y = y+1
            direction = 1 # 좌상향으로
        elif x < w and y == h: # 위쪽 벽에 도달했을 때
            x = x+1
            y = y-1
            direction = 3 # 우하향으로
        elif x == w and y == h: # 오른쪽 위 구석에 도달했을 때
            x = x-1
            y = y-1
            direction = 2 #좌하향으로
    elif direction == 1: # 좌상향
        if x > 0 and y < h:
            x = x-1
            y = y+1
        elif x == 0 and y < h: # 왼쪽 벽에 도달했을 때
            x = x+1
            y = y+1
            direction = 0 # 우상향으로
        elif x > 0 and y == h: # 위쪽 벽에 도달했을 때
            x = x-1
            y = y-1
            direction = 2 # 좌하향으로
        elif x == 0 and y == h: # 왼쪽 위 구석에 도달했을 때
            x = x+1
            y = y-1
            direction = 3 # 우하향으로
    elif direction == 2: # 좌하향
        if x > 0 and y > 0: # 좌하향 계속 될 때
            x = x-1
            y = y-1
        elif x == 0 and y > 0: # 왼쪽 벽에 도달했을 때
            x = x+1
            y = y-1
            direction = 3 # 우하향으로
        elif x > 0 and y == 0: # 아래쪽 벽에 도달했을 때
            x = x-1
            y = y+1
            direction = 1 # 좌상향으로
        elif x == 0 and y == 0: # 왼쪽 아래 구석에 도달했을 때
            x = x+1
            y = y+1
            direction = 0 # 우상향으로
    elif direction == 3: # 우하향
        if x < w and y > 0: # 우하향 계속 될 때
            x = x + 1
            y = y - 1
        elif x == w and y > 0:  # 오른쪽 벽에 도달했을 때
            x = x-1
            y = y-1
            direction = 2 # 좌하향으로
        elif x > 0 and y == 0:  # 아래쪽 벽에 도달했을 때
            x = x+1
            y = y+1
            direction = 0 # 우상향으로
        elif x == w and y == 0: # 오른쪽 아래 구석에 도달했을 때
            x = x-1
            y = y+1
            direction = 1 # 좌상향으로
    cnt += 1
    if cnt == t:
        print(x, y)
"""