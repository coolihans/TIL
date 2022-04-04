import sys
sys.stdin = open('input.txt')

def woohahyang(x,y,z):
    global minimum

    if x < N and y < N and sum(z) <= minimum:

        woohahyang(x+1,y,z+[matrix[x][y]])

        woohahyang(x,y+1,z+[matrix[x][y]])

        if len(z) == N*2-2:
            if sum(z)+matrix[x][y] < minimum:
                minimum = sum(z)+matrix[x][y]
                return




T = int(input())
for tc in range(1,T+1):
    matrix = []
    minimum = 9999
    N = int(input())
    for _ in range(N):
        matrix += [list(map(int,input().split()))]
    woohahyang(0,0,[])
    print(f'#{tc} {minimum}')