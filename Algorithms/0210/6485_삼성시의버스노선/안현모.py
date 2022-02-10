import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    # N 받기(노선 갯수)
    N = int(input())
    # Ai, Bi 받기 = > i 번째 버스가 지나는 버정 숫자의 시작과 끝 = > 버스 노선 갯수 N개이므로 N번 반복해서 받아야됨
    first_stop = [0]*(N+1)
    last_stop = [0]*(N+1)
    for _ in range(1,N+1):
        first_stop[_], last_stop[_] = list(map(int, input().split()))
    result = [0]*5001         # 버정 개수 5000개.1부터 세려고 5001개로.. 그 중 j 버정박스는 first[i]<= j <= last[i] 일 때마다 카운트
    for i in range(1, N+1):
        for j in range(first_stop[i], last_stop[i]+1):
            result[j] += 1
    P = int(input())
    print(f'#{tc}', end='')

    for i in range(1, P):
        tmp = int(input())
        print(f' {result[tmp]}', end='')
    tmp = int(input())

#     # 정답 출력 부분
#     P = int(input())
#     print(f'#{t}', end=" ")
#     for k in range(1, P):
#         tmp = int(input())
#         print(answer[tmp], end=" ")
#     tmp = int(input())
#     print(answer[tmp])
