import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    numbers = list(map(int, input().split()))
    deck_1 = [0] * 10
    deck_2 = [0] * 10
    for i in range(12):
        if not i % 2:
            deck_1[numbers[i]] += 1
            # triplet 확인
            if deck_1[numbers[i]] == 3:
                winner = 1
                break
            # run 확인
            run = 0
            for j in range(-2, 3):
                if 0 <= numbers[i] + j < 10 and deck_1[numbers[i] + j]:
                    run += 1
                else:
                    run = 0
                if run == 3:
                    winner = 1
                    break
            else:
                continue
            break
                
        else:
            deck_2[numbers[i]] += 1
            # triplet 확인
            if deck_2[numbers[i]] == 3:
                winner = 2
                break
            # run 확인
            run = 0
            for j in range(-2, 3):
                if 0 <= numbers[i] + j < 10 and deck_2[numbers[i] + j]:
                    run += 1
                else:
                    run = 0
                if run == 3:
                    winner = 2
                    break
            else:
                continue
            break
    else:
        winner = 0

    print(f'#{tc+1} {winner}')
