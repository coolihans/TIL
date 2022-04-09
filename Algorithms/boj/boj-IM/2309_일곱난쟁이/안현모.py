import sys
sys.stdin = open("input.txt")

from itertools import combinations

lst = []
for i in range(9):
    height = int(input())
    lst.append(height)

sevens = list(combinations(lst, 7))
for seven in sevens:
    if sum(seven) == 100:
        answer = seven
        break
answer = sorted(answer)
for i in range(7):
    print(answer[i])
