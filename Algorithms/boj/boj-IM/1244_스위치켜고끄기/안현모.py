import sys
sys.stdin = open("input.txt")


# 우선 스위치 누르는 거 따로 함수화.
def click(number):
    if switch[number] == 1:
        switch[number] = 0
    else:
        switch[number] = 1


switch_len = int(input())
# 1부터 쉽게 넘버링 하려고 0번 인덱스 추가
switch = [0] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    g, n = map(int, input().split())
    if g == 1:
        for j in range(1, switch_len+1):
            if j % n == 0:
                click(j)
    if g == 2:
        for k in range(1, switch_len//2):       # 최대 3개까지 가능 = switch_len//2 로 해도 됨.(스위치 홀수개 생각)
            if n - k < 1 or n + k > switch_len:      # 범위 밖으로 나가면 브레이크
                break
            if switch[n - k] == switch[n + k]:      # 양옆 같으면 점점 범위 넓혀서 진행
                click(n - k)
                click(n + k)
            else:                           # switch[n - k] != switch[n + k] 이면 break.
                break
        # 자기 번호도 눌러야 됨
        click(n)

# 20개씩 잘라서 프린트
for i in range(1, switch_len + 1):
    print(switch[i], end=' ')         # 20번째까지 뽑고
    if i % 20 == 0:                  # 20번째인지 확인
        print()                      # print로 짜르기


