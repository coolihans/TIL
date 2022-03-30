import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    p1_check = [0] * 10
    p2_check = [0] * 10

    p1_run = False
    p2_run = False

    for i in range(len(cards)):

        # run이 나온 플레이어가 있다면 break
        if p1_run or p2_run:
            break

        # p1 차례
        if not i % 2:
            p1_check[cards[i]] += 1

            # triple 검사
            if p1_check[cards[i]] >= 3:
                print(f'#{tc} 1')
                break

            # run 검사
            for j in range(8):
                # 연속 3개 숫자 카드를 갖게 되면 p1_run = True
                if p1_check[j] and p1_check[j + 1] and p1_check[j + 2]:
                    p1_run = True
                    print(f'#{tc} 1')
                    break

        # p2 차례
        else:
            p2_check[cards[i]] += 1

            # triple 검사
            if p2_check[cards[i]] >= 3:
                print(f'#{tc} 2')
                break

            # run 검사
            for j in range(8):
                # 연속 3개 숫자 카드를 갖게 되면 p2_run = True
                if p2_check[j] and p2_check[j + 1] and p2_check[j + 2]:
                    p2_run = True
                    print(f'#{tc} 2')
                    break

    # 카드를 다 뽑을 때까지 승자가 없으면(==break가 되지 않으면) 무승부 처리
    else:
        # 단, 마지막 카드에서 run이 나오는 경우가 있기 때문에 조건문을 추가했다.
        # p1_run or p2_run => 둘 다 0 이어야 0 이다. / not (p1_run or p2_run) => not (0) => 1
        # 둘 다 run이 아니면 무승부고, 마지막에 run이 나왔으면 이미 승자는 출력됐고, 아래 if문에 접근할 수 없다.
        if not (p1_run or p2_run):
            print(f'#{tc} 0')