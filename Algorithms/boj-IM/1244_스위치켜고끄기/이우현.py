import sys
sys.stdin = open('input.txt')


def turn_switch(N, switch, gender, switch_number):
    if gender == 1:  # 남성
        # 받은 수의 배수에 해당하는 스위치만 보면서 바꿔줌
        for n in range(switch_number-1, N, switch_number):
            if switch[n] == 1:
                switch[n] = 0
            else:
                switch[n] = 1

    else:  # 여성
        # 일단 받은 수는 무조건 바꿈
        if switch[switch_number-1] == 1:
            switch[switch_number-1] = 0
        else:
            switch[switch_number-1] = 1
        # 받은 수의 -k, +k 항을 비교하며 같으면 바꿔주고 아니면 부시고 나감
        for k in range(1, N):
            # 인덱스 조건
            if 0 <= switch_number-1-k and switch_number-1+k < N:
                if switch[switch_number-1-k] == switch[switch_number-1+k]:
                    if switch[switch_number-1-k] == 1:
                        switch[switch_number-1-k] = switch[switch_number-1+k] = 0
                    elif switch[switch_number-1-k] == 0:
                        switch[switch_number-1-k] = switch[switch_number-1+k] = 1
                # 다를 경우, 부시고 나감
                else:
                    break
            # 인덱스 조건이 벗어나면 부시고 나감
            else:
                break


N = int(input())
switch = list(map(int, input().split()))
students_number = int(input())
for _ in range(students_number):
    gender, switch_number = list(map(int, input().split()))
    turn_switch(N, switch, gender, switch_number)

# 출력 조건 ㅋㅋㅋㅋㅋ
if N < 20:
    ans = list(map(str, switch))
    print(' '.join(ans))
elif N < 40:
    ans1 = list(map(str, switch[:20]))
    ans2 = list(map(str, switch[20:]))
    print(' '.join(ans1))
    print(' '.join(ans2))
elif N < 60:
    ans1 = list(map(str, switch[:20]))
    ans2 = list(map(str, switch[20:40]))
    ans3 = list(map(str, switch[40:]))
    print(' '.join(ans1))
    print(' '.join(ans2))
    print(' '.join(ans3))
elif N < 80:
    ans1 = list(map(str, switch[:20]))
    ans2 = list(map(str, switch[20:40]))
    ans3 = list(map(str, switch[40:60]))
    ans4 = list(map(str, switch[60:]))
    print(' '.join(ans1))
    print(' '.join(ans2))
    print(' '.join(ans3))
    print(' '.join(ans4))
else:
    ans1 = list(map(str, switch[:20]))
    ans2 = list(map(str, switch[20:40]))
    ans3 = list(map(str, switch[40:60]))
    ans4 = list(map(str, switch[60:80]))
    ans5 = list(map(str, switch[80:]))
    print(' '.join(ans1))
    print(' '.join(ans2))
    print(' '.join(ans3))
    print(' '.join(ans4))
    print(' '.join(ans5))
