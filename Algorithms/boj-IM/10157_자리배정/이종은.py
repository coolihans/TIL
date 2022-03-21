import sys
sys.stdin = open('input1.txt')

C, R = map(int, input().split())
K = int(input())

# 사람이 좌석수 보다 많으면 0 출력
if K > C*R:
    print(0)
else:
    # 2차원 리스트로 좌석 배치도 구현
    arr = [[0]*C for _ in range(R)]

    # 스타트 값 인덱스 잡아주기
    i = R-1
    j = 0

    # 델타탐색
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    idx = 0

    human = 1
    arr[i][j] = 1

    # K번째 사람까지
    while human != K:
        ni, nj = i+dx[idx], j+dy[idx]

        # 좌석을 벗어났거나, 빈좌석이 아니라면 방향 전환
        if not R > ni >= 0 or not C > nj >= 0 or arr[ni][nj] != 0:
            ni, nj = i, j
            idx += 1
            if idx == 4:
                idx = 0

        # 몇번째 사람인지 좌석에 흔적 남기기
        else:
            arr[ni][nj] += arr[i][j] + 1
            i, j = ni, nj
            human += 1

    # 출력값 맞춰주기
    print(j+1, R-i)