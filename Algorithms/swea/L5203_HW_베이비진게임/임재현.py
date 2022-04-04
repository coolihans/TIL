import sys
sys.stdin = open('input.txt')


def is_triplet(cards):
    for card in cards:
        if cards.count(card) >= 3:
            return True
    return False


def is_run(cards):
    cards.sort()
    if len(cards) < 3:
        return False
    for idx in range(1, len(cards) - 1):
        if cards[idx - 1] + 1 == cards[idx] and cards[idx] + 1 == cards[idx + 1]:
            return True
        else:
            continue
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []

    for idx in range(12):
        if idx % 2 == 0:
            player1.append(cards[idx])

            if is_triplet(player1):
                print(f'#{tc} 1')
                break
            if is_run(player1):
                print(f'#{tc} 1')
                break

        if idx % 2 == 1:
            player2.append(cards[idx])

            if is_triplet(player2):
                print(f'#{tc} 2')
                break
            if is_run(player2):
                print(f'#{tc} 2')
                break

    if not is_run(player1) and not is_triplet(player1) and not is_triplet(player2) and not is_run(player2):
        print(f'#{tc} 0')
