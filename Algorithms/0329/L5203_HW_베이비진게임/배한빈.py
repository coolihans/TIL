import sys
sys.stdin = open('B.txt')


def check():
    global winner

    # player_1
    # 연속인 숫자
    for p in range(len(player_1) - 2):
        if player_1[p] != 0:
            if player_1[p+1] > 0 and player_1[p+2] > 0:
                winner = 1
                return
    # 같은 숫자
    for p in range(len(player_1)):
        if player_1[p] >= 3:
            winner = 1
            return

    # player_2
    # 연속인 숫자
    for p in range(len(player_1) - 2):
        if player_2[p] != 0:
            if player_2[p+1] > 0 and player_2[p+2] > 0:
                winner = 2
                return
    # 같은 숫자
    for p in range(len(player_1)):
        if player_1[p] >= 3:
            winner = 1
            return
        if player_2[p] >= 3:
            winner = 2
            return
    return


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player_1 = [0] * 10
    player_2 = [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        player_1[cards[i]] += 1
        player_2[cards[i+1]] += 1
        if i >= 4:
            check()
        if winner != 0:
            break

    print(f'#{tc} {winner}')
