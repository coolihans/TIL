import sys
sys.stdin = open('input.txt')


def atomic_bomb(atoms, n):
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]                      # 0: col, 1: row
    t = 0                                                           # 시간
    explosion = 0                                                   # 폭발한 에너지
    while n > 0 or t <= 4000:
        temp = {}                                                   # 좌표값 저장 후, 겹치는지 확인할 dict
        t += 1
        for atom in atoms:
            if atom[4] != -1:                                       # 안터진 원자만,
                atom[1], atom[0] = atom[1] + moves[atom[2]][1], atom[0] + moves[atom[2]][0]
                if 0 <= atom[0] <= 4000 and 0 <= atom[1] <= 4000:   # 좌표계 안 벗어난다면,
                    temp.setdefault((atom[1], atom[0]), [0, []])
                    temp[(atom[1], atom[0])][0] += 1                # temp에 좌표값을 키로,
                    temp[(atom[1], atom[0])][1].append(atom[4])     # 겹치는 원자 수와 원자 번호를 값으로 저장
                else:                                               # 좌표계 벗어나면 어차피 폭발못함
                    atom[4] = -1                                    # 제거
                    n -= 1                                          # 원자수 -1

        for key in temp:                                            # temp돌면서,
            if temp[key][0] > 1:                                    # 겹치는게 둘 이상이라면,
                for i in temp[key][1]:                              # 한땀한땀
                    atoms[i][4] = -1                                # 제거하고
                    explosion += atoms[i][3]                        # 폭발에너지 저장
                    n -= 1                                          # 원자 수 -1

    return explosion


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = []                  # x: (1000+x)*2, y: (1000-y)*2, 방향(0상1하2좌3우), 에너지
    for i in range(N):
        inputs = list(map(int, input().split())) + [i]
        inputs[0] = (1000 + inputs[0])*2
        inputs[1] = (1000 - inputs[1])*2
        atoms.append(inputs)
    ans = atomic_bomb(atoms, N)
    print(f'#{tc} {ans}')


