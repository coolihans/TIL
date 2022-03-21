import sys
sys.stdin = open("input1.txt")

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

"""for i in range(N-K+1):
    temp = 0
    for j in range(K):
        temp += temperatures[i+j]
    maximum = temp if temp > maximum else maximum

print(maximum)"""
# 로 풀면 시간초과고

maximum = 0

for i in range(K):
    maximum += temperatures[i]
temp = maximum

for i in range(K, N):
    temp = temp + temperatures[i] - temperatures[i - K]
    maximum = temp if temp > maximum else maximum

print(maximum)
