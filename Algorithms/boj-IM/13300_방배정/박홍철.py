import sys
sys.stdin = open("input2.txt")

count = [0] * 12
N, K = map(int, input().split())

for _ in range(N):
    S, Y = map(int, input().split())
    count[S*6 + Y - 1] += 1

result = 0
for num in count:
    if num % K:
        result += (num // K + 1)
    else:
        result += num // K

print(result)
