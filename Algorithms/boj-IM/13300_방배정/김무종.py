import sys
sys.stdin = open('input2.txt')

N, K = map(int, input().split())
man = [0] * 7
woman = [0] * 7
cnt = 0

for i in range(N):
    sex, grade = map(int, input().split())
    if sex == 0:
        woman[grade] += 1
    elif sex == 1:
        man[grade] += 1

for i in range(1, 7):
    if man[i] % K == 0:
        cnt += man[i]//K
    else:
        cnt += (man[i]//K+1)
    if woman[i] % K == 0:
        cnt += woman[i] // K
    else:
        cnt += (woman[i] // K + 1)
print(cnt)
