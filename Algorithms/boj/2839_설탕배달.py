import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

while N >= 0:           ## 0이 될때까지 돌려야됨
    if N % 5 == 0:      ## 0이 될때까지 돌려야됨
        cnt += N//5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)




# if N%5 == 3:
#     if N == 3:
#         print(1)
#     else:
#         for i in range(N // 5):
#             N -= 5
#             cnt += 1
#             if N == 3:
#                 cnt += 1
#                 break
#         print(cnt)
# else:
#     if N % 3 == 0:
#         cnt =


