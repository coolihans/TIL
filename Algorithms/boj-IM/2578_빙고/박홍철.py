import sys
sys.stdin = open("input.txt")

# 매번 탐색하긴 힘드니 빙고인지 판단하는 리스트를 만들자
global bingo_count
bingo_count = [0] * 12

global board
board = [list(map(int, input().split())) for _ in range(5)]


# 반복문이 복잡하니 빙고 수 찾고 bingo 찾는 것은 함수로
def find_bingo(on_focus):
    count = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == finding:
                bingo_count[i] += 1
                if bingo_count[i] == 5:
                    count += 1
                bingo_count[5+j] += 1
                if bingo_count[5+j] == 5:
                    count += 1

                if i == j:
                    bingo_count[10] += 1
                    if bingo_count[10] == 5:
                        count += 1
                if i + j == 4:
                    bingo_count[11] += 1
                    if bingo_count[11] == 5:
                        count += 1
                return count


check = 0
for m in range(5):
    spoken = [int(i) for i in input().split()]
    for n in range(5):
        finding = spoken[n]
        check += find_bingo(finding)
        if check >= 3:
            result = m*5 + n + 1
            break
    else:
        continue
    break

print(result)

