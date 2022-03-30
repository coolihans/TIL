import sys
sys.stdin = open('input.txt')


def baby_gin():
    p1_tri = 0
    p2_tri = 0

    for i in range(10):
        if p1[i] > 0:
            if p1[i] >= 3:          # player1이 triplet일 때
                return 1
            else:
                p1_tri += 1
                if p1_tri == 3:     # player1이 run일 때
                    return 1
        elif p1[i] == 0:
            p1_tri = 0

        if p2[i] > 0:
            if p2[i] >= 3:          # player2가 triplet일 때
                return 2
            else:
                p2_tri += 1
                if p2_tri == 3:     # player2가 run일 때
                    return 2
        elif p2[i] == 0:
            p2_tri = 0


T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10       # player1의 0 ~ 9 카드 숫자 카운트
    p2 = [0] * 10       # player2의 0 ~ 9 카드 숫자 카운트

    for i in range(len(cards)):
        if i % 2:       # p2
            p2[cards[i]] += 1
        else:           # p1
            p1[cards[i]] += 1

        # 숫자 카드가 하나씩 들어올 때마다 baby jin 비교
        if baby_gin():                      # 만일 승자가 나왔나면 출력 후 반복문 종료
            print(f'#{tc} {baby_gin()}')
            break
    else:                                   # 무승부일 때
        print(f'#{tc} 0')
