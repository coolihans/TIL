import sys
sys.stdin = open("input.txt")

K= int(input())


matrix = [list(map(int, input().split())) for _ in range(6)]
max_r = 0
max_c = 0

for i in range(6):
    if i % 2 == 0:
        if matrix[i][1] > max_r:
            max_r = matrix[i][1]
            idx_r = i
        remain_r = matrix[(idx_r + 3) % 6][1]
    else:
        if matrix[i][1] > max_c:
            max_c = matrix[i][1]
            idx_c = i
        remain_c = matrix[(idx_c + 3) % 6][1]


result =  K *(max_r * max_c - remain_r * remain_c)

print(f'{result}')