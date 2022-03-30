# 오른쪽이나 아래로만 이동
# 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
import sys
sys.stdin = open('input.txt')


def dfs(i, j, cnt, tmp_dist):
    global N, arr, min_dist
    # 0. 도착지점 발견! (N-1, N-1)
    if cnt >= 2*N-1:
        if i == N-1 and j == N-1:
            if tmp_dist < min_dist:
                min_dist = tmp_dist
        return
    
    # 추가 함수 호출을 막기 위한 장치
    if tmp_dist > min_dist:
        return
    
    # 1. 오른쪽 / 아래쪽으로 가는 함수 호출

    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(ni, nj, cnt+1, tmp_dist+arr[ni][nj])
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_dist = 10000000000

    # 시작지점좌표 / 이동칸수 / 합산거리
    dfs(0, 0, 1, arr[0][0])
    print(f'#{tc} {min_dist}')
    