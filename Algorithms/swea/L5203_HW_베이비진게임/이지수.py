import sys
sys.stdin = open('input.txt')

# run인지 triplet인지 판별하는 함수
def is_run_or_triplet(player_cards):
    for i in range(len(player_cards)): # 첫번째 카드
        for j in range(i+1, len(player_cards)): # 첫번째가 아닌 카드
            for k in range(j+1, len(player_cards)): # 첫번째, 두번째 모두 아닌 카드
                # run
                if player_cards[i] == player_cards[j] == player_cards[k]:
                    return True
                # triplet
                sorted_cards = sorted([player_cards[i], player_cards[j], player_cards[k]])
                if sorted_cards[0] + 1 == sorted_cards[1] and sorted_cards[1] + 1 == sorted_cards[2]:
                    return True
    return False

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []
    winner = 0

    for idx in range(len(cards)):
        if idx % 2 == 0: # 인덱스값이 짝수라면
            player1.append(cards[idx])
            if len(player1) >= 3 and is_run_or_triplet(player1): # player의 카드가 세장 이상인 경우부터
                winner = 1
                break
        else:
            player2.append(cards[idx])
            if len(player2) >= 3 and is_run_or_triplet(player2):
                winner = 2
                break

    print(f'#{tc} {winner}')