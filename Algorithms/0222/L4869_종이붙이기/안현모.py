import sys
sys.stdin = open("input.txt")


# 재귀~ 10 하고 20 일 때 1 , 3 인거 불러와서 써먹기
# 1 3 5 11 21
# f(i-2)*2 + f(i-1) = f(i) (f>=3)  => -10, -20씩해야 됨
def f(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    elif N >= 30:
        return 2*f(N-20) + f(N-10)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = f(N)

    print(f'#{tc} {answer}')
