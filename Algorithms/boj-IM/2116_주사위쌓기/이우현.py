import sys
sys.stdin = open('input.txt')


def stack_dices(dices, N):
    # 각 주사위 면(인덱스)이 마주보는 면
    face_to_face = {
        0: 5,
        1: 3,
        2: 4,
        3: 1,
        4: 2,
        5: 0,
    }
    # 각 주사위 면(인덱스)을 둘러싼 면들
    side_by_top = {
        0: [1, 2, 3, 4],
        1: [0, 2, 4, 5],
        2: [0, 1, 3, 5],
        3: [0, 2, 4, 5],
        4: [0, 1, 3, 5],
        5: [1, 2, 3, 4],
    }

    side_sum_max = 0
    # 첫 주사위의 윗 면을 기준으로 나머지가 결정되기 때문에,
    # 첫 주사위의 전 면을 윗면으로 해보고 결과값을 비교
    for i in range(6):
        side_sum = 0
        top_idx = face_to_face[i]
        side_idxs = side_by_top[top_idx]
        # 옆 면들 중 가장 큰 값 찾기
        side_max = 0
        for side_idx in side_idxs:
            if side_max < dices[0][side_idx]:
                side_max = dices[0][side_idx]
        side_sum += side_max
        
        # 두번째 주사위부터 마지막까지,
        # 이전 주사위의 윗 면과 현 주사위의 아랫면의 숫자를 동일하게 맞추어 가면서,
        # 옆 면들 중 가장 큰 값을 찾아 더해줌
        for j in range(1, N):
            bottom_idx = dices[j].index(dices[j-1][top_idx])
            top_idx = face_to_face[bottom_idx]
            side_idxs = side_by_top[top_idx]
            side_max = 0
            for side_idx in side_idxs:
                if side_max < dices[j][side_idx]:
                    side_max = dices[j][side_idx]
            side_sum += side_max

        # 옆 면들의 합을 비교
        if side_sum > side_sum_max:
            side_sum_max = side_sum

    return side_sum_max


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
ans = stack_dices(dices, N)
print(ans)