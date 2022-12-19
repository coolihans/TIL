T = int(input())

for i in range(1, T+1):
    H, W, N = map(int, input().split())
    a = N // H
    b = N % H
    if b == 0:
        b = H
        a -= 1
    answer = b*100 + (a+1)
    print(answer)
