import sys
sys.stdin = open("input.txt")
# sys.stdin.readline()

N = int((input()))
array = [0] + list(map(int, input().split()))
S = int(input())
students = [list(map(int, input().split())) for _ in range(S)]

for i in range(S):
    sex = students[i][0]
    card = students[i][1]
    
    # 남자일 때
    if sex == 1:
        for m in range(card, N+1, card):  # 배수마다
            if array[m] == 0:
                array[m] = 1
            else:
                array[m] = 0
    # 여자일 때
    else:
        # 일단 자기자신 바꾸고
        if array[card] == 0:
            array[card] = 1
        else:
            array[card] = 0
        for j in range(1, 50):  # 49이상 안 넘음
            # 범위 체크
            if card-j < 1 or card+j > N:
                break
            # 양끝이 일치하면 바꿔줌
            else:
                if array[card-j] == array[card+j]:
                    if array[card-j] == 0:
                        array[card-j] = 1
                    else:
                        array[card-j] = 0
                    if array[card+j] == 0:
                        array[card+j] = 1
                    else:
                        array[card+j] = 0
                else:
                    break

# 출력 설정
if len(array) > 20:
    for x in range(len(array)//20):
        print(*array[(20*x + 1):20*(x+1)+1])
    print(*array[20*(len(array)//20) + 1:])
else:
    print(*array[1:])
