import sys

sys.stdin = open("input.txt")


def man_work(num):
    for i in range(1, bulb_num // num + 1):
        bulbs[num * i - 1] = 1 - bulbs[num * i - 1]


def woman_work(num):
    i = 1
    while 1:
        if num-1 - i < 0 or num-1 + i >= bulb_num:
            break
        elif bulbs[num-1 - i] != bulbs[num-1 + i]:
            break
        i += 1

    for i in range(num - i, num-1 + i):
        bulbs[i] = 1 - bulbs[i]


global bulb_num
bulb_num = int(input())
global bulbs
bulbs = list(map(int, input().split()))

student_num = int(input())
for _ in range(student_num):
    gender, number = map(int, input().split())
    if gender == 1:
        man_work(number)
    else:
        woman_work(number)

for i in range(len(bulbs)):
    if i % 20 == 19 and i != len(bulbs)-1:
        print(bulbs[i])
    else:
        print(bulbs[i], end=" ")

