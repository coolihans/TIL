import sys
sys.stdin = open('input.txt', encoding='UTF-8')

def bruteforce(p, t):
    i = 0
    j = 0
    cnt = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1   # 0 에서 다시 시작.
        if j == len(p):
            cnt += 1
            j = 0   # 0에서 다시 시작
    return cnt


T = 10

for tc in range(1, T+1):
    case_number = int(input())
    pattern = input()
    text = input()

    result = bruteforce(pattern, text)

    print(f'#{tc} {result}')


