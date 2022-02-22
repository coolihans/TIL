import sys
sys.stdin = open("input.txt")


switch_len = int(input())

switch = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    s, n = map(int, input().split())

    if s == 1:
        for j in range(1, len(switch) + 1):
            if j % n == 0:
                if switch[j-1] == 1:
                    switch[j-1] = 0
                else:
                    switch[j-1] = 1
    if s == 2:
        



