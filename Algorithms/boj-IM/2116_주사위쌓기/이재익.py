import sys
sys.stdin = open('input.txt')
import copy

N = int(input()) # 주사위 갯수
M = [list(map(int, input().split())) for i in range(N)] # 주사위 정보가 담겨있는 리스트
cnt = 0 # 최대값 저장

"""
시간 제한이 2초고 주사위는 1,000개 이하이므로 시간 제한이 중요한 문제는 아니었다
경우의 수를 나눠서(A-F, B-D, C-E) 각각 위 아래면을 차지할 때 90, 180, 270도를 회전할 수 있으니
위아래면을 제외한 수 중 최대를 구하면 되므로
max 함수를 사용해서 풀면 되는 문제였다고 생각한다
"""

for i in range(6): # 첫번째 주사위의 밑면(i번째로 생각)
    stack = 0
    B = copy.deepcopy(M) # 깊은 복사
    cnt_now = 0 # 최댓값의 합을 모을 곳
    l = B[0] # 주사위 맨 밑번째는 B[0]

    if i == 0: # 밑면이 A칸이라면
        a = B[0][i]
        b = B[0][5]
        stack += b # 윗칸에 F를 추가
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    elif i == 1: # 밑면이 B칸이라면
        a = B[0][i]
        b = B[0][3]
        stack += b
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    elif i == 2: # 밑면이 C칸이라면
        a = B[0][i]
        b = B[0][4]
        stack += b
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    elif i == 3: # 밑면이 D칸이라면
        a = B[0][i]
        b = B[0][1]
        stack += b
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    elif i == 4: # 밑면이 E칸이라면
        a = B[0][i]
        b = B[0][2]
        stack += b
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    elif i == 5: # 밑면이 F칸이라면
        a = B[0][i]
        b = B[0][0]
        stack += b
        l.remove(a)
        l.remove(b)
        cnt_now += max(l)

    for j in range(1, N):

        l = B[j]
        c = 0
        c += l.index(stack) # c번째에 맨 밑칸이 있음
        stack = 0

        if c == 0:  # 밑면이 0이면
            a = l[c]
            b = l[5]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

        elif c == 1:
            a = l[c]
            b = l[3]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

        elif c == 2:
            a = l[c]
            b = l[4]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

        elif c == 3:
            a = l[c]
            b = l[1]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

        elif c == 4:
            a = l[c]
            b = l[2]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

        elif c == 5:
            a = l[c]
            b = l[0]
            stack += b
            l.remove(a)
            l.remove(b)
            cnt_now += max(l)

    if cnt_now > cnt:
        cnt = cnt_now

print(cnt)