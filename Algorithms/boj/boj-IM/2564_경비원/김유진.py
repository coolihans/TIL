import sys
sys.stdin = open("input.txt")

garo, sero = map(int, input().split())
store_nums = int(input())

store_matrix = [list(map(int, input().split())) for _ in range(store_nums)]

dong_direct, dong_block = map(int, input().split())

for i in range(store_nums):
    if store_matrix[i][0] == dong_direct:
        distance = abs(store_matrix[i][1]-dong_block)

