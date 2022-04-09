import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    atoms = dict()
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        # 0.5 이동 고려
        atoms[(2 * x, 2 * y)] = [d, e]

    # 0:상 1:하 2:좌 3:우
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]

    answer = 0
    while len(atoms) > 1:
        tmp_set = set()
        new_atoms = dict()
        cnt = 0
        collisions = set()

        for key, value in atoms.items():
            x, y = key
            # 원자 이동
            new_x, new_y = x + dxs[value[0]], y + dys[value[0]]

            # 영역 밖으로 나가면 소멸
            if new_x < -2000 or new_x > 2000 or new_y < -2000 or new_y > 2000:
                continue

            new_key = (new_x, new_y)
            tmp_set.add(new_key)

            # 충돌 임시 저장
            if len(tmp_set) == cnt:
                collisions.add(new_key)
                new_atoms[new_key][1] += value[1]
            else:
                new_atoms[new_key] = value
                cnt += 1
        # 충돌 처리
        for collision in collisions:
            answer += new_atoms[collision][1]
            del new_atoms[collision]
        atoms = new_atoms
    print(f'#{tc}', answer)
