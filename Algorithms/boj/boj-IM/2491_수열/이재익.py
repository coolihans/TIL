import sys
sys.stdin = open('input1.txt')

N = int(input())
L = list(map(int, input().split()))
big_max = 1
short_max = 1
max = 1
for i in range(N-1):
    if L[i] < L[i+1]:
        big_max += 1
        if max <= short_max:
            max = short_max
        short_max = 1
    elif L[i] == L[i+1]:
        big_max += 1
        short_max += 1
    elif L[i] > L[i+1]:
        short_max += 1
        if max <= big_max:
            max = big_max
        big_max = 1
    if i == N-2: # 위 함수만 사용하면 끝 수가 포함이 안 돼서 꼭 카운트가 -1이 부족하게 된다
        # 따라서 지금껏 높여놓은 max 값을 높여주는 함수를 찾아서 넣어줘야 한다.
        if max <= short_max:
            max = short_max
        if max <= big_max:
            max = big_max


if N > 2:
    print(max)
elif N == 2:
    print(2)
elif N == 1:
    print(1)