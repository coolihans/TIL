import sys
sys.stdin = open('input1.txt')

N = int(input())
numbers = list(map(int, input().split()))

# N 은 1 이상 100000 이하의 정수이므로 가장 긴 길이는 적어도 1 이상이다.
max_length = 1

# 연속해서 커지는 최대 길이 구하기
ascending_length = 1
i = 0
while N-1 > i:
    # 연속해서 커지면 ascending_length += 1
    if numbers[i] <= numbers[i+1]:
        ascending_length += 1
        # ascending_length 가 max 값을 넘어서면 저장
        if ascending_length > max_length:
            max_length = ascending_length
    # 연속이 깨지면 1로 초기화
    else:
        ascending_length = 1
    # 인덱스는 계속 진행
    i += 1

# 연속해서 작아지는 최대 길이 구하기 (위와 같은 맥락)
descending_length = 1
j = 0
while N-1 > j:
    if numbers[j+1] <= numbers[j]:
        descending_length += 1
        if descending_length > max_length:
            max_length = descending_length
    else:
        descending_length = 1
    j += 1

print(max_length)