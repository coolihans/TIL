import sys
sys.stdin = open('input.txt')

matrix = [[0]*100 for _ in range(100)]
 
squares = [list(map(int, input().split())) for _ in range(4)]
 
for square in squares:
    for i in range(square[0], square[2]):
        for j in range(square[1], square[3]):
            matrix[i][j] = 1
 
total = 0
for k in range(100):
    for l in range(100):
        if matrix[k][l]:
            total +=1
print(total)