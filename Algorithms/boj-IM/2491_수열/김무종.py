import sys
sys.stdin = open('input3.txt')

T = int(input())
numbers = list(map(int, input().split()))
cnt_up = 0
cnt_down = 0
list_up =[]
list_down = []
idx = 0
value = numbers[0]
value1 = numbers[0]
while idx < len(numbers):
    if numbers[idx] >= value:
        cnt_up += 1
        value = numbers[idx]
    else:
        value = numbers[idx]
        list_up.append(cnt_up)
        cnt_up = 1
    if idx == len(numbers) - 1:
        list_up.append(cnt_up)
    idx = idx + 1

idx = 0
while idx < len(numbers):
    if numbers[idx] <= value1:
        cnt_down += 1
        value1 = numbers[idx]
    else:
        value1 = numbers[idx]
        list_down.append(cnt_down)
        cnt_down = 1
    if idx == len(numbers)-1:
        list_down.append(cnt_down)
    idx = idx + 1

if max(list_up) >= max(list_down):
    print(max(list_up))
else:
    print(max(list_down))