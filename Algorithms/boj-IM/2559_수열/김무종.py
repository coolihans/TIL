import sys
sys.stdin = open('input1.txt')

N, T = map(int, input().split())
numbers = list(map(int, input().split()))
'''
totals = []
max_total = 0
for idx in range(N+1-T):
    tmp = numbers[idx]
    for i in range(idx + 1, idx+T):
        tmp += numbers[i]
    if max_total < tmp:
        max_total = tmp
print(max_total)
'''
# 시간초과

sum0 = sum(numbers[:T])
sum_list = [sum0]
for i in range(1, N+1-T):
    tmp = sum_list[i-1] - numbers[i-1] + numbers[i+T-1]
    sum_list.append(tmp)
print(max(sum_list))