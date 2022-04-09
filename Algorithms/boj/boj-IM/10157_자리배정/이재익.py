import sys
sys.stdin = open('input3.txt')

def Seat(A, C, R, K):
    M = [[0]*(C+1) for _ in range(R+1)] # range를 C, R로 해버리면 M[x+1][y+1] 같은 형태 때문에 index 문제 발생
    x = 1 # (1,1)부터 시작해야 함
    y = 1
    direction = 0 # 0은 위, 1은 오른쪽, 2는 아래, 3은 왼쪽
    # 기본은 상승이므로 상승으로 시작함
    for i in range(1, A+1):


        if i == K:
            return print(f'{y} {x}')
        # 만약 {x}{y} 형식으로 출력하게 된다면 다음과 같은 문제가 생긴다.

"""
문제에서 원하는 것은 아래에서부터 쌓아올리는, 시계방향으로의 회전을 원했다.
하지만 아래와 같이 코드를 구현하게 되면 위에서부터 아래로 쌓아올리고, 반시계방향 회전을 하게 된다.
결과적으로는 x, y축이 뒤바뀌어서 그래프가 그려지게 되는 것이다.
이중 배열 그래프는 잘 그려내서 뭐지? 했는데, 이러한 문제가 있었다.

앞으로 디버깅을 할 때는 다음과 같은 것을 주의해야 한다.

1. 경계값 관련 문제(특히 N=1, N=0 등 쉽게 오류를 유발할 수 있는 것)를 의심해 본다.
2. 문제에서 요구하는 그래프와 다른 그래프를 그린다면, 결과값이 뒤바뀔 수 있음을 의심한다.
3. 오타가 났을 수도 있으므로 print를 통해 계속 원하는 결과값이 나오는 지 확인한다.
"""

        M[x][y] = i #값 저장

        if direction == 0: # 상승
            if 1 <= x < R: # 아직 정상 범위 안에 있을 때
                if M[x+1][y] == 0: # 다음 줄이 아직 0이라면
                    x = x+1
                else:
                    y = y+1
                    direction = 1 # 우회전
            elif x == R: # 끝줄이라면
                y = y+1
                direction = 1 # 우측이동
        elif direction == 1: # 오른쪽으로 가고 있을 때
            if 1 <= y < C:  # 아직 정상 범위 안에 있고
                if M[x][y+1] == 0:  # 다음 줄이 아직 0이라면
                    y = y + 1
                else:
                    x = x - 1
                    direction = 2 # 하강 전환
            elif y == C: # 끝에 다다르면 하강으로 전환
                x = x - 1
                direction = 2 # 하강 전환
        elif direction == 2: #하강
            if R >= x > 1:  # 아직 정상 범위 안에 있고
                if M[x-1][y] == 0:  # 다음 줄이 아직 0이라면
                    x = x - 1
                else:
                    y = y - 1
                    direction = 3 # 좌회전
            elif x == 1:
                y = y - 1
                direction = 3
        elif direction == 3: # 좌측이동
            if M[x][y-1] == 0:  # 다음 줄이 아직 0이라면
                y = y - 1
            else:
                x = x + 1
                direction = 0 # 상승으로 전환




C, R = list(map(int, input().split())) # C는 너비, R은 높이
A = C*R # 총 들어갈 수 있는 인원 수(너비 x 높이)
K = int(input()) # 입장 번호

if K > A or C < 5 or R > 1000 or C <= 0 or R <= 0: # 주어진 값이 조건과 다를 때는 무조건 0을 출력
    print(0)

else:
    Seat(A, C, R, K)
