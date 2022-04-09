import sys
sys.stdin = open('input.txt')

def turn_switch(switchs, gender, number):
    # 남학생일때 인덱스는 0부터 시작
    # 받은 수의 배수자리의 스위치를 변경
    if gender == 1: 
        for i in range(number, n, number+1):
            if switchs[i] == 1:
                switchs[i] = 0
            else:
                switchs[i] = 1

    else: 
        # 여학생일때
        # 인덱스 범위를 넘어가면 바로 반복중지
        # 받은 수를 중심으로 대칭일때까지 스위치 변경
        for j in range(1, n+1):
            if not(0 <= number-j < n) or not(0 <= number+j < n):
                switchs[number] = 1 if switchs[number] == 0 else 0
                break
            else:
                if switchs[number-j] == switchs[number+j]:
                    switchs[number-j] = 1 if switchs[number-j] == 0 else 0
                    switchs[number+j] = 1 if switchs[number+j] == 0 else 0
                else:
                    switchs[number] = 1 if switchs[number] == 0 else 0
                    break
    return switchs


n = int(input())
switchs = list(map(int, input().split()))

students = [list(map(int, input().split())) for _ in range(int(input()))]

for student in students:
    gender = student[0]
    number = student[1] - 1
    switchs = turn_switch(switchs, gender, number)

switchs = list(map(str, switchs))
# 20개의 스위치가 넘는다면, 20개씩 출력
answers = []
if n > 20:
    for k in range(0, n, 20):
        answers.append(' '.join(switchs[k:k+20]))
else:
    answers.append(' '.join(switchs))

for answer in answers:
    print(answer)