import sys
sys.stdin = open('input2.txt')

N, M = list(map(int, input().split()))
L = list(map(int, input().split()))

now = sum(L[:M]) # 처음값(0번째부터~M번째까지의 합)
max = now # 처음은 M까지만큼을 max로 설정
for i in range(M, N):
    now = now + L[i] - L[i-M]
    # 큐의 맨 왼쪽 값을 빼고 오른쪽에 다음 값을 계속 더해줌
    if now > max:
        max = now
    # 그 값이 max보다 크면 변경

print(max)

"""
처음에는 간단히 sum(L[i:i+M]) 형태로 풀었는데
아뿔싸 sum이 또 다른 for문이라
2중 for문으로 되버린 것이다
범위 설정하는 문제 같은 경우에는 위와 같이
전 값을 빼고 다음 값을 넣는 식으로 for문을 최대한 줄여야
시간 내에 해결할 수 있다
특히 백준 문제는 기본적인 데이터가 10만개가 넘어서
2중 for문이면 시간제한에 100% 걸리게 된다
처음에는 완전탐색으로 푸는 건 좋지만
그 다음에는 어떻게든 시간을 줄여줘야 한다
"""