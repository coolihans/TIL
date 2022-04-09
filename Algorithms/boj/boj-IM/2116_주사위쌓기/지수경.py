# 1. 입력
N= int(input())
dice = [list(map(int,input().split())) for _ in range(N)]
dict = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0} # 주사위 마주보는 면
result = []

# 2. 주사위 쌓는 경우 구하기 (마주보는 수)
for idx in range(6):
    dice_num =[]
    dice_num.append(dice[0][idx])
    for i in range(N-1):
        next_idx = dict[idx]
        next_num = dice[i][next_idx]
        idx = dice[i+1].index(next_num)
        dice_num.append(next_num)
    dice_num.append(dice[N-1][dict[dice[N-1].index(next_num)]])
    result.append(dice_num)

# 3. 주사위 기둥의 옆면 합 구하기
max_sum=0
for case in result:
    sum = 0
    for i in range(N):
        if case[i] !=6 and case[i+1] != 6:  # 위아래 모두 6이 아닌 경우,
            sum += 6
        elif case[i]==6:  # 아래가 6인 경우,
            if case[i+1] != 5:
                sum+=5
            else:        # 아래가 6이고 윗면이 5인 경우,
                sum+=4
        elif case[i] == 5:  # 그 외에는 모두 5를 더해줌
            sum+=4
        else:
            sum+=5

# 4. 합의 최대값 구하기
    if sum > max_sum:
        max_sum = sum
print(max_sum)


