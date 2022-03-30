import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 컨테이너 N, 트럭 M
    w_i = list(map(int, input().split())) # 컨테이너 무게
    t_i = list(map(int, input().split())) # 트럭 무게
    w_ii = sorted(w_i, reverse=True)  # 큰 순서대로 정렬
    t_ii = sorted(t_i, reverse=True)

    result = 0
    for i in range(M):
        w_list = []
        for j in range(N):
            if t_ii[i] >= w_ii[j]:  # 무게가 트럭 용량보다 작거나 같으면
                w_list.append(w_ii[j])  # temp에 넣어줌
        if len(w_list) != 0:  # temp에 한개라도 들어갔을 때
            result += max(w_list)  # temp에 들어있는 최대값을 ans에 더해줌
            for j in range(N):  # 최대값을 찾아서 0으로 바꾼뒤 반복문에서 나감
                if w_ii[j] == max(w_list):
                    w_ii[j] = 0
                    break
    print(f'#{tc} {result}')