import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    draw = True
    array = list(map(int, input().split()))
    player1 = []
    player2 = []

    for i in range(6):
        player1.append(array[i*2])
        player2.append(array[i*2+1])

        if i >= 2:
            # TRIPLET
            player1.sort()
            player2.sort()
            players = [player1, player2]
            winner_t = 0
            for idx, player in enumerate(players):
                for p in range(len(player) - 2):
                    if player[p] == player[p + 1] == player[p + 2]:
                        winner_t = idx+1

            if winner_t != 0:
                print(f"#{tc} {winner_t}")
                draw = False
                break

            # RUN
            sort1 = list(set(player1))
            sort1.sort()
            sort2 = list(set(player2))
            sort2.sort()
            winner_r = 0
            p_sorts = [sort1, sort2]
            for idx, p_sort in enumerate(p_sorts):
                for s in range(len(p_sort) - 2):
                    if p_sort[s] == p_sort[s+1]-1 == p_sort[s+2]-2:
                        winner_r = idx + 1

            if winner_r != 0:
                print(f"#{tc} {winner_r}")
                draw = False
                break

    if draw:
        print(f"#{tc} 0")


