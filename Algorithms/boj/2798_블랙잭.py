from itertools import combinations


def solv(M, cards):
    card_sums = []

    for my_cards in combinations(cards, 3):
        card_sum = sum(my_cards)
        if card_sum <= M:
            card_sums.append(sum(my_cards))

    card_sums.sort()

    return card_sums[-1]


N, M = map(int, input().split())
cards = map(int, input().split())

print(solv(M, cards))

