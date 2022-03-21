import sys
sys.stdin = open('input.txt')

# 행우선 빙고판
bingo_table1 = [list(map(int, input().split())) for _ in range(5)]
# 열우선 빙고판
bingo_table2 = [[0] * 5 for _ in range(5)]
for r in range(5):
    for c in range(5):
        bingo_table2[r][c], bingo_table2[c][r] = bingo_table1[c][r], bingo_table1[r][c]

# 사회자가 부를 숫자들 하나의 리스트에 순서대로 넣기
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))

line_bingo = 0

# 사회자가 하나씩 숫자를 부른다.
for number in range(len(numbers)):
    # 빙고가 3줄 이상이면 break
    if line_bingo >= 3:
        print(number)
        break
    else:
        # 사회자가 부른 숫자가 있는 행찾기
        for row in range(len(bingo_table1)):
            if numbers[number] in bingo_table1[row]:
                # 사회자가 부른 숫자가 있는 열찾기
                for col in range(len(bingo_table1[row])):
                    if bingo_table1[row][col] == numbers[number]:
                        # 사회자가 부른 숫자가 있는 빙고판 자리에 0 넣기
                        bingo_table1[row][col], bingo_table2[col][row] = 0, 0

                        # 방금 0을 넣음과 동시에 빙고판의 해당 행/열이 모두 0이라면
                        if not sum(bingo_table1[row]) or not sum(bingo_table2[col]):
                            # line_bingo 에 += 1
                            line_bingo += int(sum(bingo_table1[row])==0) + int(sum(bingo_table2[col])==0)
                        # 역대각선 위치의 숫자였다면 역대각선 순회하며 모두 0인지 확인하고, 맞다면 line_bingo += 1
                        if row + col == 4:
                            zero = 0
                            for j in range(5):
                                if not bingo_table1[j][-1-j]:
                                    zero += 1
                                    if zero == 5:
                                        line_bingo += 1
                        # 대각선 위치의 숫자였다면 대각선 순회하며 모두 0인지 확인하고, 맞다면 line_bingo += 1
                        if row == col:
                            zero = 0
                            for i in range(5):
                                if not bingo_table1[i][i]:
                                    zero += 1
                                    if zero == 5:
                                        line_bingo += 1
                        break
                break