from itertools import permutations

N = int(input())

arr = list(map(int, input().split()))
l = len(arr)
p = list(permutations(arr, l))
# print(p)
answer = 0
for j in range(len(p)):
    tmp = 0
    for i in range(len(p[j])-1):
        tmp += abs(p[j][i]-p[j][i+1])
    if tmp >= answer:
        answer = tmp

print(answer)