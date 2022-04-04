# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    lst.sort(key=lambda x: (x[1], x[0]))
    
    prev_et = cnt = 0
    for l in lst:
        st, et = l[0], l[1]    
        if st >= prev_et:
            cnt += 1
            prev_et = et

    print(f'#{tc} {cnt}')