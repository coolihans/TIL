import sys
sys.stdin = open('input.txt')


def get_winner(numbers):
    player1 = []
    player2 = []

    for turn in range(0, 12, 2):

        number1 = numbers[turn]
        number2 = numbers[turn+1]
        player1.append(number1)
        player2.append(number2)

        if turn <= 2:
            continue
        # 3번째 턴 부터 run, triplet 검사
        else:
            # player1 triplet 검사
            if player1.count(number1) == 3:
                return 1
            # player1 run 검사
            # 마지막에 추가한 숫자가 제일 큰 수일때, 중간 수, 가장 작은 수 일때 모두 확인
            # 뽑은 숫자가 3이라면 [1, 2, 3], [2, 3, 4], [3, 4, 5]
            elif (number1-2 in player1 and number1-1 in player1) or (number1-1 in player1 and number1+1 in player1) or (number1+1 in player1 and number1+2 in player1):
                return 1
            # player2 triplet 검사
            elif player2.count(number2) == 3:
                return 2
            # player2 run 검사
            elif (number2-2 in player2 and number2-1 in player2) or (number2-1 in player2 and number2+1 in player2) or (number2+1 in player2 and number2+2 in player2):
                return 2
    
    return 0

T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))
    winner = get_winner(numbers)

    print(f'#{tc+1} {winner}')
