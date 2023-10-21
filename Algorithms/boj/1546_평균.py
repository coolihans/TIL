import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

result = sum(scores)*100/(max(scores)*N)

print(result)