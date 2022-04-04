import sys
sys.stdin = open('input.txt')


def versers():
    p1, p2 = [], []

    for i in range(12):
        if not i % 2:                               # 짝수 인덱스면, p1
            p1.append(cards[i])
            temp = p1
        else:                                       # 홀수 인덱스면, p2
            p2.append(cards[i])
            temp = p2

        if len(temp) >= 3:                          # 3장 이상 받은 경우,

            for j in range(len(temp)):              # Triplet 검사
                if temp.count(temp[j]) == 3:        # 같은 카드가 3장 이상이고,
                    if not i % 2:                   # 짝수 인덱스면,
                        return 1                    # p1 승리!
                    else:                           # 홀수 인덱스면,
                        return 2                    # p2 승리!

            sorted_temp = sorted(list(set(temp)))   # 중복 제거하고 오름차순 정렬
            for j in range(len(sorted_temp)-2):     # Run 검사
                if sorted_temp[j+1] - sorted_temp[j] == 1 and sorted_temp[j+2] - sorted_temp[j] == 2:
                    if not i % 2:
                        return 1
                    else:
                        return 2

    return 0                                    # 그 외, 무승부


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    ans = versers()
    print(f'#{tc} {ans}')

