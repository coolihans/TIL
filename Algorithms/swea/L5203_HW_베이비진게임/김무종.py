import sys
sys.stdin = open('input.txt')

def check(x):
    tmp = 0
    for i in range(len(x)):
        if x[i] == 3:
            return True
    for i in range(8):
        if x[i] and x[i+1] and x[i+2]:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    A = [0] * 10
    B = [0] * 10
    answer = 0
    for idx, val in enumerate(numbers):
        if idx % 2 == 0:
            A[val] += 1
            if check(A):
                answer = 1
                break
        else:
            B[val] += 1
            if check(B):
                answer = 2
                break
    print(f'#{tc}', answer)