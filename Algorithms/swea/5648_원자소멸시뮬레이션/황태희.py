import sys
sys.stdin = open('input.txt')


def is_collision(atom1, atom2):
    # case1
    if (atom1[2], atom2[2]) == (3, 1) or (atom1[2], atom2[2]) == (0, 2):
        if atom1[0] - atom2[0] == atom1[1] - atom2[1]:
            return float(atom2[0] - atom1[0])
    # case2
    elif (atom1[2], atom2[2]) == (3, 0) or (atom1[2], atom2[2]) == (1, 2):
        if atom1[0] - atom2[0] == -(atom1[1] - atom2[1]):
            return float(atom2[0] - atom1[0])
    # case3
    elif atom1[0] == atom2[0] and (atom1[2], atom2[2]) == (0, 1):
        return (atom2[1] - atom1[1])/2
    # case4
    elif atom1[1] == atom2[1] and (atom1[2], atom2[2]) == (3, 2):
        return (atom2[0] - atom1[0])/2


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    atoms.sort(key=lambda x: (x[0], x[1]))
    result = {}
    answer = 0

    for i in range(N):
        for j in range(i+1, N):
            collision_distance = is_collision(atoms[i], atoms[j])
            if collision_distance:
                if collision_distance in result:
                    result[collision_distance] += [(i, j)]
                else:
                    result[collision_distance] = [(i, j)]

    for distance in sorted(result.keys()):
        collision = set()
        for i, j in result[distance]:
            if atoms[i][3] and atoms[j][3]:
                collision = collision | {i, j}

        for i in collision:
            answer += atoms[i][3]
            atoms[i][3] = 0

    print(f'#{tc} {answer}')
