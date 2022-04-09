import sys
sys.stdin = open("input.txt")

stu_num = int(input())

idx = 0
line = []
for num in map(int, input().split()):
    idx += 1
    if num == 0:
        line.append(idx)
        continue
    line = line[:-num] + [idx] + line[-num:]


print(*line, sep=" ")
