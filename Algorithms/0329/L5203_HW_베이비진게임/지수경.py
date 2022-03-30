import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    cards = list(map(int,input().split()))
    player1 = [cards[0],cards[2]]
    player2 = [cards[1],cards[3]]
    winner = []

    for i in range(4,12):
        if i%2 == 0:  # 플레이어1
            player1.append(cards[i])
            player1.sort()
            set_player1 = list(set(player1))
            set_player1.sort()

            for j in range(len(player1)):  # 같은 숫자 판별
                if player1[j] == player1[j-1] and player1[j-1]== player1[j-2]:
                    winner.append(i)

            if len(set_player1) >= 3:  # 연속인 숫자 판별
                for s in range(len(set_player1)-2):
                    if set_player1[s] == set_player1[s+1]-1 and set_player1[s+1] == set_player1[s+2]-1:
                        winner.append(i)

        else:  # 플레이어2
            player2.append(cards[i])
            player2.sort()
            set_player2 = list(set(player2))
            set_player2.sort()

            for j in range(len(player2)):  # 같은 숫자 판별
                if player2[j] == player2[j - 1] and player2[j - 1] == player2[j - 2]:
                    winner.append(i)

            if len(set_player2) >= 3:  # 연속인 숫자 판별
                for s in range(len(set_player2)-2):
                    if set_player2[s] == set_player2[s+1]-1 and set_player2[s+1] == set_player2[s+2]-1:
                        winner.append(i)

        if winner:  # winner가 나오면 break
            break

    if winner:
        if winner[0]%2 == 0:  # 첫번째 위너가 짝수면 플레이어1 승
            answer = 1
        else:  #첫번째 위너가 홀수면 플레이어2 승
            answer = 2
    else:  # 위너가 없으면 0 출력
        answer = 0

    print(f'#{t+1} {answer}')


