import sys
sys.stdin = open('input.txt')

# 세로 합 구하는 함수
def sero(numbers, s):
    cnt = 0
    for q in range(5):
        cnt += numbers[q][s]
    return cnt

# 왼쪽 대각선 합 구하는 함수
def dael(numbers):
    cnt = 0
    for q in range(5):
        cnt += numbers[q][q]
    return cnt

# 오른쪽 대각선 합 구하는 함수

def daer(numbers):
    cnt = 0
    for q in range(5):
        cnt += numbers[q][4-q]
    return cnt

my_bingo = [list(map(int, input().split())) for _ in range(5)]
A = [list(map(int, input().split())) for _ in range(5)]

numbers = []

for i in range(5):
    for j in range(5):
        numbers.append(A[i][j])

bingo = 0
bingo_row = []
bingo_col = []
bingo_dael = 0
bingo_daer = 0

for i in range(25):

    for j in range(5):

        for k in range(5):

            if my_bingo[j][k] == numbers[i]:
                my_bingo[j][k] = 0
    # 빙고를 없애는 것과 동시에 빙고를 체크하지 말고
    # 빙고 숫자를 없애고 나서 차근차근 다시 점검할 것
    if i>10:
        for j in range(5):
            # not in bingo_row나 bingo_col의 경우는
            # 이미 세놓은 빙고를 또 셀수 있으므로 또 세는 것 방지장치임
            if sum(my_bingo[j]) == 0 and j not in bingo_row:
                bingo += 1
                bingo_row.append(j)
            if sero(my_bingo, j) == 0 and j not in bingo_col:
                bingo += 1
                bingo_col.append(j)
            if dael(my_bingo) == 0 and bingo_dael < 1:
                bingo += 1
                bingo_dael = 1
            if daer(my_bingo) == 0 and bingo_daer < 1:
                bingo += 1
                bingo_daer = 1
    # 빙고 숫자가 갑자기 4개 이상이 될 수도 있으므로 bingo >= 3으로 설정할 것
    if bingo >= 3:
        print(i+1)
        break