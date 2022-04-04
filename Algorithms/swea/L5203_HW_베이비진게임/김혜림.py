# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet
# 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
import sys
sys.stdin = open('input.txt')


def find_babygin(cards):
    cnts = [0]*10
    ans = 0
    for c in cards:
        cnts[c] += 1

    for idx in range(10):
        if cnts[idx] >= 3:
            ans += 1
            cnts[idx] -= 3
        if idx <= 7:
            if cnts[idx] and cnts[idx+1] and cnts[idx+2]:
                ans += 1
                cnts[idx] -= 1
                cnts[idx+1] -= 1
                cnts[idx+2] -= 1
    return ans

    
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    
    # 0. 카드 분배
    Acards = []
    Bcards = []    
    for i in range(12):
        if i % 2 == 0:
            Acards.append(lst[i])
        else:
            Bcards.append(lst[i])
        
    aans = [0, 0, 0, 0]
    bans = [0, 0, 0, 0]
    
    for i in range(4):
        endsign = 0
        
        aans[i] = find_babygin(Acards[:3+i])
        if aans[i] > bans[i]:
            print(f'#{tc} 1')
            endsign += 1
        # 승부가 나서 끝나도 된다면    
        if endsign:
            break

        bans[i] = find_babygin(Bcards[:3 + i])
        if aans[i] > bans[i]:
            print(f'#{tc} 1')
            endsign += 1
        elif aans[i] < bans[i]:
            print(f'#{tc} 2')
            endsign += 1
        elif i == 3 and aans[i] == bans[i]:
            print(f'#{tc} 0')
            endsign += 1
        # 승부가 나서 끝나도 된다면    
        if endsign:
            break
    
            