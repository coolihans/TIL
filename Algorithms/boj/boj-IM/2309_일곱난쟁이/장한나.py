# from sys import stdin
import sys
sys.stdin = open("input.txt")

hobbits = [int(input()) for _ in range(9)]

# 일단 아홉 명을 다 더해서
total = 0
for hobbit in hobbits:
    total += hobbit

he_is_not = []  # 두 명씩 빼보면서 100을 찾는다
for i in range(8):
    stop = False
    for j in range(i+1, 9):
        alien = hobbits[i] + hobbits[j]
        if total - alien == 100:
            he_is_not.append(i)
            he_is_not.append(j)
            stop = True
            break
    if stop is True:
        break

real = []
for k in range(9):
    if k not in he_is_not:
        real.append(hobbits[k])

# 정렬
for n in range(7-1, 0, -1):
    for m in range(n):
        if real[m] > real[m+1]:
            real[m], real[m+1] = real[m+1], real[m]

for ans in range(7):
    print(real[ans])