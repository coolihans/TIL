def babyjin(hand):
    table = [0]*10
    for i in hand:
        table[i] = 1
        for j in table:
            if table[j] == 3:
                return i
            elif table[j] == 1 and table[j+1] == 1 and table[j+2] == 1:
                return i


T = int(input())

for tc in range(1,T+1):
    arr = []
    arr = list(map(int,input().split()))
    print(arr)

    player1 = []
    for i in range(12):
        if i%2 == 0:
            player1 += [arr[i]]
    p1 = 99
    p1 = babyjin(player1)

    player2 = []
    for i in range(12):
        if i%2 == 1:
            player2 += [arr[i]]

    babyjin(player2)