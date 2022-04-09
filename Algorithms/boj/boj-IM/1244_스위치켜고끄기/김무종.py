import sys
sys.stdin = open('input.txt')


def get_man(idx, bulbs):
    tmp = idx
    while tmp < len(bulbs):
        bulbs[tmp] ^= 1
        tmp += idx
    return bulbs


def get_woman(idx, bulbs):
    right = idx + 1
    left = idx - 1

    if left < 1 or right > len(bulbs)-1:
        bulbs[idx] ^= 1
        return bulbs

    else:
        while True:
            if bulbs[left] != bulbs[right]:
                left += 1
                right -= 1
                break
            if right >= len(bulbs)-1 or left <= 1:
                break

            right += 1
            left -= 1

        for k in range(left, right+1):
            bulbs[k] ^= 1

        return bulbs

N = int(input())
bulbs = [0, *map(int, input().split())]
person = int(input())
for i in range(person):
    sex, number = map(int, input().split())
    if sex == 1:
        bulbs = get_man(number, bulbs)
    else:
        bulbs = get_woman(number, bulbs)

bulbs = bulbs[1:]
if len(bulbs) > 20:
    for l in range(0, len(bulbs), 20):
        print(' '.join(map(str, bulbs[l:l+20])))
else:
    print(' '.join(map(str, bulbs[0:])))