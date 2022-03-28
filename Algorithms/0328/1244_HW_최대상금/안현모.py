import sys
sys.stdin = open('input.txt')


def DFS(cnt, num_lst):
    global answer
    # 탈출
    if cnt >= total_cnt:
        tmp_lst = list(reversed(num_lst))
        tmp_answer = 0
        for i in range(len(num_lst)):
            tmp_answer += (10**i)*tmp_lst[i]
        answer = max(tmp_answer, answer)
        return
    # 바꾸기
    for i in range(len(num_lst)):
        for j in range(i+1, len(num_lst)):
            if num_lst[i] <= num_lst[j]:
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
                DFS(cnt+1, num_lst)
                num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
    # 교환 횟수 남을 경우 처리
    if cnt < total_cnt:
        if (total_cnt - cnt) % 2:
            num_lst[-1], num_lst[-2] = num_lst[-2], num_lst[-1]
        DFS(cnt+10, num_lst)


T = int(input())
for tc in range(1, T+1):
    num, total_cnt = map(int, input().split())
    num = str(num)
    num_lst = []
    for i in range(6):
        if i < len(num):
            a = int(num[i]) % 10
            num_lst.append(a)
        else:
            break
    answer = 0
    DFS(0, num_lst)
    print(f'#{tc} {answer}')
