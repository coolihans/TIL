import sys
sys.stdin = open("input2.txt")


def battle(a, b):
    for idx in range(4):
        if a[idx] == b[idx]:
            continue
        elif a[idx] > b[idx]:
            return 'A'
        else:
            return 'B'
    return 'D'


num_of_round = int(input())

for i in range(num_of_round):
    count = [[0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(2):
        for mark in list(map(int, input().split()))[1:]:
            count[j][4-mark] += 1
    print(battle(count[0], count[1]))
