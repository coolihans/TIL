N, K = list(map(int, input().split()))
Boy = [0]*6
Girl = [0]*6
R_cnt = 0
for i in range(N):
    S, Y = list(map(int, input().split()))
    if S == 0: # 성별이 여자일 때
        Girl[Y-1] += 1
    if S == 1: # 남자일 때
        Boy[Y-1] += 1
for i in range(6):
    if Boy[i] > 0 and Boy[i]>K:
        if Boy[i] % K > 0 :
            R_cnt += int((Boy[i])/K) +1
        else:
            R_cnt += int((Boy[i])/K)
    if Boy[i] > 0 and Boy[i]<=K:
        R_cnt += 1
    if Boy[i] == 0:
        continue
for i in range(6):
    if Girl[i] > 0 and Girl[i]>K:
        if Girl[i] % K > 0 :
            R_cnt += int((Girl[i])/K)+1
        else:
            R_cnt += int((Girl[i])/K)
    if Girl[i] > 0 and Girl[i]<=K:
        R_cnt += 1
    if Girl[i] == 0:
        continue
print(R_cnt)