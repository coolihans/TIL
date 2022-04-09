import sys
sys.stdin = open("input.txt")

num_of_dice = int(input())

dices = []

for _ in range(num_of_dice):
    nums = list(map(int, input().split()))
    dice = [0] * 7
    dice[nums[0]] = nums[5]
    dice[nums[5]] = nums[0]
    dice[nums[1]] = nums[3]
    dice[nums[3]] = nums[1]
    dice[nums[2]] = nums[4]
    dice[nums[4]] = nums[2]
    dices.append(dice)

result = 0

for i in range(1, 7):
    bottom = i
    side_sum = 0
    for dice in dices:
        if bottom == 6 or dice[bottom] == 6:
            if bottom == 5 or dice[bottom] == 5:
                side_sum += 4
            else:
                side_sum += 5
        else:
            side_sum += 6
        bottom = dice[bottom]

    result = side_sum if side_sum > result else result

print(result)