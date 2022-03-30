import sys

sys.stdin = open('input.txt')


def is_babygin(player):
    for i in range(10):
        if player[i] == 3:
            return True

        elif i < 8 and player[i] and player[i + 1] and player[i + 2]:
            return True


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]
    winner = 0

    for i in range(6):
        p1[arr[2*i]] += 1
        p2[arr[2*i+1]] += 1

        if i >= 2:
            if is_babygin(p1):
                winner = 1
                break
            if is_babygin(p2):
                winner = 2
                break

    print(f'#{tc} {winner}')
