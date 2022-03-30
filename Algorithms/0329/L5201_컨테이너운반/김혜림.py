# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N 컨테이너 / M 트럭
    N, M = map(int, input().split())
    nlst = sorted(list(map(int, input().split())), reverse=True)
    mlst = sorted(list(map(int, input().split())), reverse=True)
    
    ans = 0
    for n in nlst:
        for im in range(len(mlst)):
            if n <= mlst[im]:
                ans += n
                mlst.pop(im)
                break
    print(f'#{tc} {ans}')
    
    