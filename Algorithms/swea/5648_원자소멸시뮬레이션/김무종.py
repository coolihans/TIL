import sys
sys.stdin = open('input.txt')

T = int(input())
dxs = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
for tc in range(1, T+1):
    N = int(input())
    list_A = []
    for i in range(N):
        list_A.append(list(map(int, input().split())))
    second = 1
    answer = 0
    while second < 4000:
        bang_list = []
        tmp_list = []
        bangs = []
        cnt = 0
        for i in range(len(list_A)):
            list_A[i][0] = list_A[i][0] + dxs[list_A[i][2]][0]
            list_A[i][1] = list_A[i][1] + dxs[list_A[i][2]][1]
            if [list_A[i][0], list_A[i][1]] not in tmp_list:
                tmp_list.append([list_A[i][0], list_A[i][1]])
            else:
                bangs.append([list_A[i][0], list_A[i][1]])
                cnt += 1
        cnt = cnt * 2
        for i in range(len(bangs)):
            for j in range(len(list_A)):
                if cnt > 0:
                    if bangs[i][0] == list_A[j][0] and bangs[i][1] == list_A[j][1]:
                        bang_list.append(list_A[j])
                        cnt -= 1
                else:
                    break


        '''
        for i in range(len(list_A)):
            for j in range(len(list_A)):
                if i != j and list_A[j] not in bang_list:
                    if list_A[i][0] == list_A[j][0] and list_A[i][1] == list_A[j][1]:
                        bang_list.append(list_A[i])
                        bang_list.append(list_A[j])
        '''
        list_A = list(map(tuple, list_A))
        bang_list = list(set(list(map(tuple, bang_list))))

        for bang in bang_list:
            answer += bang[3]



        list_A = list(set(list_A)-set(bang_list))
        list_A = list(map(list, list_A))
        second += 1



    print(f'#{tc}', answer)
