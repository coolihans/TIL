N, M = map(int, input().split())
matrix = []
cnt_lst = []
for _ in range(N):
    matrix.append(input())

for start_i in range(N-7):
    for start_j in range(M-7):
        # 1번 경우 2번 경우 => 왼쪽위를 흑 백 뭘로 정하느냐에 따라.
        cnt_1, cnt_2 = 0, 0
        for i in range(start_i, start_i + 8):
            for j in range(start_j, start_j + 8):
                # 짝수 칸들 다 똑같아야됨
                if (i + j) % 2 == 0:
                    # 백이 아닐 때
                    if matrix[i][j] != 'W':
                        cnt_1 += 1
                    # 흑이 아닐 때
                    if matrix[i][j] != 'B':
                        cnt_2 += 1
                # 홀수 칸 다 똑같아야됨
                else:
                    # 백이 아닐 때
                    if matrix[i][j] != 'W':
                        cnt_2 += 1
                    # 흑이 아닐 때
                    if matrix[i][j] != 'B':
                        cnt_1 += 1
        cnt = min(cnt_1, cnt_2)
        cnt_lst.append(cnt)

print(min(cnt_lst))
