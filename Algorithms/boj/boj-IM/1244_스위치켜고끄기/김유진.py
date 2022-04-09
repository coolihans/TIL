import sys
sys.stdin = open("input.txt")

def get_males(L, N):
    for i in range(N-1, len(L), N):
        if L[i] == 1:
            L[i] = 0
        else:
            L[i] = 1
    return L

def get_females(L, N):
    j = N-1
    Left = j-1
    Right = j+1
    L[j] = (L[j]+1) % 2
    while Left >= 0 and Right <= len(L)-1:
        if L[Left] == L[Right]:
            L[Left], L[Right] = (L[Left]+1) % 2, (L[Right]+1) %2
            Left -= 1
            Right += 1
        else:
            break
    return L

switch = int(input())
status = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, switch_num = map(int, input().split())
    if gender == 1:
        result = get_males(status, switch_num)
    else:
        result = get_females(status, switch_num)

if len(result) > 20:
    while len(result) != 0:
        print(' '.join(map(str, result[:20])))
        result = result[20:]
else:
    print(' '.join(map(str, result)))