import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def row_check(check_list):
    bingo = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            if check_metrix[i][j]:
                tmp += 1
            if tmp == 5:
                bingo += 1
    return bingo

def col_check(check_list):
    bingo = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            if check_metrix[j][i]:
                tmp += 1
            if tmp == 5:
                bingo += 1
    return bingo

def diagnoal_check(check_list, row, col):
    bingo = 0
    tmp = 0
    tmp1 = 0

    for i in range(5):
        if check_metrix[i][i]:
            tmp += 1
        if check_metrix[i][4-i]:
            tmp1 += 1
        if i == 4 and tmp == 5:
            bingo += 1
        if i == 4 and tmp1 == 5:
            bingo += 1
    '''
    for num in [-2, -1, 0, 1, 2]:
        if 0 <= row + num < 5 and 0 <= col + num < 5 and check_metrix[row+num][col+num]:
            tmp += 1

        if tmp == 5-col and tmp != 1:
            bingo += 1

        if 0 <= row + num < 5 and 0 <= col - num < 5 and check_metrix[row + num][col - num]:
            tmp1 += 1

        if tmp1 == 5 - col and tmp1 != 1:
            bingo += 1
    '''
    # 문제 잘못봐서 대각선을 능동적으로 구함.
    return bingo

def check(cholsu, a):
    global check_metrix
    for row in range(5):
        for col in range(5):
            if cholsu[row][col] == a:
                check_metrix[row][col] = 1
                return row, col

cholsu = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
mc_list = []
check_metrix = [[0]*5 for i in range(5)]
total = 0
for i in range(5):
    mc_list.extend(mc[i])

cnt = 0

for i in range(len(mc_list)):
    row, col = 0, 0
    row, col = check(cholsu, mc_list[i])
    total = row_check(check_metrix) + col_check(check_metrix) + diagnoal_check(check_metrix, row, col)
    if total >= 3:
        cnt = i
        break


print(cnt+1)

