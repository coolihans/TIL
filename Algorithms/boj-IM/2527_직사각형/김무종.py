import sys
sys.stdin = open('input.txt')

for i in range(4):
    list1 = list(map(int, input().split()))
    rectangle_a = list1[:4]
    width_a, height_a = rectangle_a[2] - rectangle_a[0], rectangle_a[3] - rectangle_a[1]
    rectangle_b = list1[4:]
    width_b, height_b = rectangle_b[2] - rectangle_b[0], rectangle_b[3] - rectangle_b[1]
    if rectangle_a[0] < rectangle_b[0]:
        if rectangle_a[0] + width_a < rectangle_b[0]:
            print("d")
        elif rectangle_a[0] + width_a == rectangle_b[0]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("c")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("b")
            elif rectangle_a[1] == rectangle_b[1]:
                print("b")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("c")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("b")
        elif rectangle_b[0] < rectangle_a[0] + width_a < rectangle_b[2]:
            # b의 선분 안에 있음
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        elif rectangle_a[0] + width_a == rectangle_b[2]:
            # b의 오른쪽 점 접근
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        elif rectangle_a[0] + width_a > rectangle_b[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
            # b의 오른쪽 점 초과

    elif rectangle_a[0] == rectangle_b[0]:
        if rectangle_b[0] < rectangle_a[0] + width_a < rectangle_b[2]:
        # b의 선분 안에 있음
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        elif rectangle_a[0] + width_a == rectangle_b[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        # b의 오른쪽 점 접근
        elif rectangle_a[0] + width_a > rectangle_b[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        # b의 오른쪽 점 초과

    else:
        if rectangle_b[0] + width_b < rectangle_a[0]:
            print("d")
        elif rectangle_b[0] + width_b == rectangle_a[0]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("c")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("b")
            elif rectangle_a[1] == rectangle_b[1]:
                print("b")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("c")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("b")
        elif rectangle_a[0] < rectangle_b[0] + width_b < rectangle_a[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        elif rectangle_b[0] + width_b == rectangle_a[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")
        elif rectangle_b[0] + width_b > rectangle_a[2]:
            if rectangle_a[1] < rectangle_b[1]:
                if rectangle_a[1] + height_a < rectangle_b[1]:
                    print("d")
                elif rectangle_a[1] + height_a == rectangle_b[1]:
                    print("b")
                elif rectangle_b[1] < rectangle_a[1] + height_a:
                    print("a")
            elif rectangle_a[1] == rectangle_b[1]:
                print("a")
            else:
                if rectangle_b[1] + height_b < rectangle_a[1]:
                    print("d")
                elif rectangle_b[1] + height_b == rectangle_a[1]:
                    print("b")
                elif rectangle_a[1] < rectangle_b[1] + height_b:
                    print("a")

