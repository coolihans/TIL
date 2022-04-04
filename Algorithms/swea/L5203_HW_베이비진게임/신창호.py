import sys
sys.stdin = open('input.txt')


def func(numbers):
    # triplet 확인
    for number in numbers:
        if numbers.count(number) >= 3:
            return True
    # run을 확인하기 위해 중복을 제거하고 정렬
    numbers = list(set(numbers))
    numbers.sort()
    for idx in range(1, len(numbers) - 1):
        if numbers[idx - 1] == numbers[idx] - 1 and numbers[idx + 1] == numbers[idx] + 1:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # 각 플레이어는 2장씩 받고 시작
    player1 = cards[:4:2]
    player2 = cards[1:4:2]
    idx = 4

    winner = 0
    # 각 턴에 카드를 받고 run이나 triplet이 있는지 확인
    while idx != 12:
        turn = '2' if idx % 2 else '1'
        if turn == '1':
            player1.append(cards[idx])
            if func(player1):
                winner = 1
                break
        else:
            player2.append(cards[idx])
            if func(player2):
                winner = 2
                break
        idx += 1
    print(f'#{tc}', winner)
