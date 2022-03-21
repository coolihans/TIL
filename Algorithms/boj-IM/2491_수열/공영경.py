import sys
sys.stdin = open('input1.txt')

n = int(input())
numbers = list(map(int, input().split()))

# 최대길이와 현재 수열의 길이를 1로 초기화
max_length = 1
length = 1

# 내림차순 찾기
for i in range(1, n):
    if numbers[i-1] >= numbers[i]:
        length += 1
    else:
        length = 1
    if max_length < length:
        max_length = length

# 오름차순 찾기
length = 1
for i in range(1, n):
    if numbers[i-1] <= numbers[i]:
        length += 1
    else:
        length = 1
    if max_length < length:
        max_length = length
print(max_length)