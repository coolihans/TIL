N = int(input())

# 제일 큰 값은 비어 있는 방향의 반대.
# 1 <> 2
# 3 <> 4
north = []
south = []
east = []
west = []
big = 0
small = 0
for i in range(1, 7):
    S, L = list(map(int, input().split()))
    if S == 4: # 북
        north.append(L)
        north.append(i)
    if S == 3: # 남
        south.append(L)
        south.append(i)
    if S == 2: # 서
        west.append(L)
        west.append(i)
    if S == 1: # 동
        east.append(L)
        east.append(i)
# 경우의 수는 총 24개. (형태 x 꼭지점 갯수)
if len(north)==2:
    if len(east)==2:
        big = east[0]*north[0]
        if north[1] <= 2:
            small = west[2]*south[0]
        if north[1] == 3:
            small = west[2]*south[2]
        if north[1] == 4:
            small = west[0]*south[2]
        if north[1] == 5:
            small = west[0]*south[0]
        if north[1] == 6:
            small = west[2]*south[0]

    else: # 오른쪽 아래가 비어 있음
        big = west[0]*north[0]
        if west[1] <= 2:
            small = south[2] * east[0]
        if west[1] == 3:
            west = south[2] * east[2]
        if west[1] == 4:
            small = south[0] * east[2]
        if west[1] == 5:
            small = south[0] * east[0]
        if west[1] == 6:
            small = south[2] * east[0]

else:
    if len(east)==2:
        big = east[0]*south[0]
        if east[1] <= 2:
            small = north[2] * west[0]
        if east[1] == 3:
            small = north[2] * west[2]
        if east[1] == 4:
            small = north[0] * west[2]
        if east[1] == 5:
            small = north[0] * west[0]
        if east[1] == 6:
            small = north[2] * west[0]
    else: # 오른쪽 위가 비어 있음
        big = west[0]*south[0]
        if south[1] <= 2:
            small = east[2] * north[0]
        if south[1] == 3:
            small = east[2] * north[2]
        if south[1] == 4:
            small = east[0] * north[2]
        if south[1] == 5:
            small = east[0] * north[0]
        if south[1] == 6:
            small = east[2] * north[0]
print((big-small)*N)