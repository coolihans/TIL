import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(3):
        door_data = list(map(int, input().split()))
        data.append(door_data)
    x = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
    total_lst = []
    for now in x:
        fishing_point = [0] * 1000
        total = 0
        for i in range(3):
            door_pos = data[now[i]][0]
            number = data[now[i]][1]
            for j in range(number):
                k = 0
                while True:
                    if fishing_point[door_pos + k] == 0 and 0 < door_pos + k < N+1:
                        fishing_point[door_pos + k] = 1
                        person_pos = door_pos + k
                        total += abs(door_pos - person_pos) + 1
                        k += 1
                        break
                    elif fishing_point[door_pos - k] == 0 and 0 < door_pos - k < N+1:
                        fishing_point[door_pos - k] = 1
                        person_pos = door_pos - k
                        total += abs(door_pos - person_pos) + 1
                        k += 1
                        break
                    else:
                        k += 1
                        continue
        total_lst.append(total)

    result = min(total_lst)
    print(f'#{tc} {result}')




