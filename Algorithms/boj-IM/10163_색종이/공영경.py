import sys
sys.stdin = open('input3.txt')

n = int(input())
matrix = [[0] * 1001 for _ in range(1001)]
# 해당 위치에 색종이를 채워넣기
papers = [list(map(int, input().split())) for _ in range(n)]
for idx, paper in enumerate(papers):
    for x in range(paper[0], paper[0] + paper[2]):
        for y in range(paper[1], paper[1] + paper[-1]):
            matrix[x][y] = idx + 1

# 색종이 번호를 세서 넓이 계산
for i in range(n):
    answer = 0
    for row in matrix:
        answer += row.count(i+1)
    print(answer)