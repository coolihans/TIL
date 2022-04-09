import sys
sys.stdin = open('input.txt')

width, height = map(int, input().split())
N = int(input())
shops = []
for i in range(N):
    direction, length = map(int, input().split())
    shops.append([direction, length])
men_d, men_l = map(int, input().split())
total = 0
for shop in shops:
    tmp = 0
    tmp2 = 0
    if men_d == 1:
        if shop[0] == 1:
            total += abs(shop[1] - men_l)
        elif shop[0] == 2:
            tmp = height + men_l + shop[1]
            if tmp > width + height:
                total += tmp2
            else:
                total += tmp
        elif shop[0] == 3:
            total += shop[1] + men_l
        elif shop[0] == 4:
            tmp = width - men_l
            total += shop[1] + tmp
    elif men_d == 2:
        if shop[0] == 1:
            tmp = height + men_l + shop[1]
            if tmp > width + height:
                tmp2 = (width + height) * 2 - tmp
                total += tmp2
            else:
                total += tmp
        elif shop[0] == 2:
            total += abs(shop[1] - men_l)
        elif shop[0] == 3:
            tmp = men_l + height - shop[1]
            total += tmp
        elif shop[0] == 4:
            tmp = height - shop[1] + width - men_l
    elif men_d == 3:
        if shop[0] == 1:
            total += men_l + shop[1]
        elif shop[0] == 2:
            tmp = height - men_l + shop[1]
            total += tmp
        elif shop[0] == 3:
            total += abs(shop[1] - men_l)
        elif shop[0] == 4:
            tmp = men_l + width + shop[1]
            if tmp > width + height:
                tmp2 = (width + height) * 2 - tmp
                total += tmp2
            else:
                total += tmp
    else:   # men_d == 4
        if shop[0] == 1:
            tmp = width - shop[1] + men_l
            total += tmp
        elif shop[0] == 2:
            tmp = height - men_l + width - shop[1]
            total += tmp
        elif shop[0] == 3:
            tmp = shop[1] + width + men_l
            if tmp > width + height:
                tmp2 = (width + height) * 2 - tmp
                total += tmp2
            else:
                total += tmp
        elif shop[0] == 4:
            total += abs(shop[1] - men_l)

print(total)
