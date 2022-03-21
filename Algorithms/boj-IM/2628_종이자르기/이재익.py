import sys
sys.stdin = open('input.txt')

# X와 Y 길이 입력
X, Y = list(map(int, input().split()))
# 자를 횟수 입력
N = int(input())
# 방향, 자르는 점 입력
XP = [0]
YP = [0]
for i in range(N):
    D, P = list(map(int, input().split()))
    if D: # 세로로 자를 때
        XP.append(P)
    else: # 가로로 자를 때
        YP.append(P)
XP.append(X) # 끝점을 추가
YP.append(Y) # 끝점을 추가

# 버블 소팅을 통해 점을 순서대로 정리함
for i in range(len(XP)-1):
    for j in range(len(XP)-1-i):
        if XP[j] > XP[j+1]:
            XP[j], XP[j+1] = XP[j+1] , XP[j]
for i in range(len(YP)-1):
    for j in range(len(YP)-1-i):
        if YP[j] > YP[j+1]:
            YP[j], YP[j+1] = YP[j+1] , YP[j]

# 점 사이의 거리를 각각 저장
XL = []
YL = []
for i in range(len(XP)-1):
    XL.append(XP[i+1]-XP[i])
for i in range(len(YP)-1):
    YL.append(YP[i+1]-YP[i])

# 거리들을 각각 곱한 값만큼 네모가 나옴
max_area = 0
for i in range(len(XL)):
    for j in range(len(YL)):
        if XL[i]*YL[j] > max_area:
            max_area = XL[i]*YL[j]

print(max_area)