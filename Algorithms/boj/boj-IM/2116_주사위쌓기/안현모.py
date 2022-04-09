import sys
sys.stdin = open("input.txt")

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
change = [5, 3, 4, 1, 2, 0]
max_sum = 0
for i in range(6):
    tmp_sum = 0
    next_i = i
    number = dices[0][next_i]
    for dice in dices:
        next_i = change[dice.index(number)]
        if number == 6 and dice[next_i] == 5:
            tmp_sum += 4
        elif number == 5 and dice[next_i] == 6:
            tmp_sum += 4
        elif number == 6 or dice[next_i] == 6:
            tmp_sum += 5
        else:
            tmp_sum += 6
        # 아래 dice 의 윗면 값을 다음 dice 의 아래로 가게끔 해줘야된다.
        number = dice[next_i]

    if tmp_sum > max_sum:
        max_sum = tmp_sum

print(max_sum)
