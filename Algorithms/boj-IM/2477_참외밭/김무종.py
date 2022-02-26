import sys
sys.stdin = open('input.txt')

T = int(input())
list1 = [list(map(int, input().split())) for _ in range(6)]
directions = []
lengths = []
for step in range(6):
    directions.append(list1[step][0])
    lengths.append(list1[step][1])

max_lengths, box_lengths = [], []

for i in range(1, 5):
    if directions.count(i) == 1:
        max_lengths.append(lengths[directions.index(i)])
        tmp = directions.index(i) + 3
        if tmp >= 6:
            tmp -= 6
        box_lengths.append(lengths[tmp])

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(T * area)