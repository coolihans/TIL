from itertools import combinations
import sys

sys.stdin = open('input.txt')


def collide(a, b):
    # 테이블을 절반만 사용하기 때문에 a가 무조건 b보다 커야 한다.
    if a < b:
        a, b = b, a
    # 같은 y축 상에 있다
    if atoms[a][0] == atoms[b][0]:
        if atoms[a][2] == 0 and atoms[b][2] == 1 and atoms[a][1] < atoms[b][1]:
            collision_table_half[a][b] = round((atoms[b][1] - atoms[a][1]) / 2, 1)
        elif atoms[a][2] == 1 and atoms[b][2] == 0 and atoms[a][1] > atoms[b][1]:
            collision_table_half[a][b] = round((atoms[a][1] - atoms[b][1]) / 2, 1)
    # 같은 x축 상에 있다
    elif atoms[a][1] == atoms[b][1]:
        if atoms[a][2] == 3 and atoms[b][2] == 2 and atoms[a][0] < atoms[b][0]:
            collision_table_half[a][b] = round((atoms[b][0] - atoms[a][0]) / 2, 1)
        elif atoms[a][2] == 2 and atoms[b][2] == 3 and atoms[a][0] > atoms[b][0]:
            collision_table_half[a][b] = round((atoms[a][0] - atoms[b][0]) / 2, 1)
    # y=x 방향 대각선 상에 있다
    elif atoms[a][0] - atoms[a][1] == atoms[b][0] - atoms[b][1]:
        if (atoms[a][2] == 3 and atoms[b][2] == 1) or (atoms[a][2] == 0 and atoms[b][2] == 2) and atoms[a][0] < atoms[b][0]:
            collision_table_half[a][b] = atoms[b][0] - atoms[a][0]
        if (atoms[a][2] == 1 and atoms[b][2] == 3) or (atoms[a][2] == 2 and atoms[b][2] == 0) and atoms[a][0] > atoms[b][0]:
            collision_table_half[a][b] = atoms[a][0] - atoms[b][0]
    # y=-x 방향 대각선 상에 있다.
    elif atoms[a][0] + atoms[a][1] == atoms[b][0] + atoms[b][1]:
        if (atoms[a][2] == 3 and atoms[b][2] == 0) or (atoms[a][2] == 1 and atoms[b][2] == 2) and atoms[a][0] < atoms[b][0]:
            collision_table_half[a][b] = atoms[b][0] - atoms[a][0]
        if (atoms[a][2] == 0 and atoms[b][2] == 3) or (atoms[a][2] == 2 and atoms[b][2] == 1) and atoms[a][0] > atoms[b][0]:
            collision_table_half[a][b] = atoms[a][0] - atoms[b][0]


T = int(input())
for tc in range(T):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    # 각 원자끼리의 충돌시간을 기록하기 위한 2차원 테이블
    # row = col 축에 대해 대칭인 테이블이므로 축 아래쪽 절반만 만들고 사용한다.
    collision_table_half = [[0.0] * i for i in range(N)]
    energy = 0

    for a, b in combinations(range(N), 2):
        collide(a, b)

    atom_list = list(range(N))
    # 아무리 해도 이정도보다 많이 돌아갈 일은 없으므로
    for _ in range(N//2):
        min_time = 4000
        colliding_atoms = set()
        # 테이블을 돌며 가장 빨리 충돌하는 경우 찾기
        for row in atom_list:
            for col in atom_list:
                if col < row and collision_table_half[row][col] and collision_table_half[row][col] < min_time:
                    min_time = collision_table_half[row][col]
                    colliding_atoms = {row, col}
                elif col < row and collision_table_half[row][col] and collision_table_half[row][col] == min_time:
                    colliding_atoms |= {row, col}
        # 반복문을 돌았는데 더이상 충돌할 것이 없는 경우 break
        if min_time == 4000:
            break
        # 충돌한 원자들은 에너지 방출하고 목록에서 빠진다.
        for atom in colliding_atoms:
            energy += atoms[atom][3]
            atom_list.remove(atom)

    print(f'#{tc+1} {energy}')
