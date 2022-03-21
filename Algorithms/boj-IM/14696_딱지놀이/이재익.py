import sys
sys.stdin = open('input1.txt')

N = int(input())
M = [list(map(int, input().split())) for i in range(N*2)]

for i in range(N):
    cnt_A_4 = 0
    cnt_A_3 = 0
    cnt_A_2 = 0
    cnt_A_1 = 0
    cnt_B_4 = 0
    cnt_B_3 = 0
    cnt_B_2 = 0
    cnt_B_1 = 0
    for j in range(1, len(M[2*i])):
        if M[2*i][j] == 4:
            cnt_A_4 += 1
        elif M[2*i][j] == 3:
            cnt_A_3 += 1
        elif M[2*i][j] == 2:
            cnt_A_2 += 1
        elif M[2*i][j] == 1:
            cnt_A_1 += 1

    for j in range(1, len(M[2*i+1])):
        if M[2*i+1][j] == 4:
            cnt_B_4 += 1
        elif M[2*i+1][j] == 3:
            cnt_B_3 += 1
        elif M[2*i+1][j] == 2:
            cnt_B_2 += 1
        elif M[2*i+1][j] == 1:
            cnt_B_1 += 1

    if cnt_A_4 > cnt_B_4:
        print('A')
    elif cnt_A_4 < cnt_B_4:
        print('B')
    elif cnt_A_4 == cnt_B_4:
        if cnt_A_3 > cnt_B_3:
            print('A')
        elif cnt_A_3 < cnt_B_3:
            print('B')
        elif cnt_A_3 == cnt_B_3:
            if cnt_A_2 > cnt_B_2:
                print('A')
            elif cnt_A_2 < cnt_B_2:
                print('B')
            elif cnt_A_2 == cnt_B_2:
                if cnt_A_1 > cnt_B_1:
                    print('A')
                elif cnt_A_1 < cnt_B_1:
                    print('B')
                elif cnt_A_1 == cnt_B_1:
                    print('D')