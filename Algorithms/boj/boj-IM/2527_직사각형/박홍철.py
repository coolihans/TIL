import sys
sys.stdin = open("input.txt")

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    check1 = (max(x1, x2) < min(p1, p2))
    check2 = (max(y1, y2) < min(q1, q2))

    check3 = (max(x1, x2) == min(p1, p2))
    check4 = (max(y1, y2) == min(q1, q2))

    if check1 and check2:
        print('a')
    elif (check1 and check4) or (check2 and check3):
        print('b')
    elif check3 and check4:
        print('c')
    else:
        print('d')
