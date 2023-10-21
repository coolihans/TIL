import sys
# sys.stdin = open("input.txt")


n, t_score, p = map(int,input().split())
if n == 0:
    print(1)
else:
    score_lst = list(map(int, input().split()))
    cnt = 0
    if n == p and score_lst[-1] >= t_score:
        print(-1)
    else:
        for i in score_lst:
            cnt += 1
            if i <= t_score:
                print(cnt)
                break
        else:
            print(cnt+1)



print(score_lst)