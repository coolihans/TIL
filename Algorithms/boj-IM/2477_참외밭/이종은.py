import sys
sys.stdin = open('input.txt')

# 면적당 참외 개수
N = int(input())
# 문제 내용에 따르면 참외밭은 육각형
arr = [list(map(int, input().split())) for _ in range(6)]

# 참외밭에서 최대 길이를 찾는다
max_length = 0
for i in range(6):
    if arr[i][1] > max_length:
        max_length = arr[i][1]

# 최대길이 직전부터 시작하도록 queue(?) 개념을 사용한 거라 할 수 있을진 모르겠다.
while arr[1][1] != max_length:
    arr.append(arr.pop(0))

#
over_area = 1
none_length = 0
none_area = 1

# 몇번째 순서의 길이인지에 따라 연산을 달리 하기 위해 enumerate 사용 (육각형이므로 0부터 5까지)
for turn, length in enumerate(arr):

    # 위의 while 문으로 순서를 최대길이 직전부터 정렬했기 때문에 두번째 순서까진
    # 각 길이를 곱해서 실제 참외밭이 아닌 공간까지 over 한 넓이를 구한다.
    if 1 >= turn:
        over_area *= length[1]

    # turn == 2 이므로 (0, 1, 2) 세번째 순서다.
    elif turn == 2:
        # 첫번째 순서 길이가 세번째 순서 길이보다 크다면 참외밭의 존재하지 않는 길이 none_length 에 저장
        if arr[0][1] > length[1]:
            none_length = arr[0][1] - length[1]
        # 첫번째 순서 길이가 세번째 순서 길이보다 작다면 참외밭의 존재하지 않는 길이 none_length 에 저장
        else:
            none_length = length[1] - arr[0][1]

    # turn == 3 이므로 (0, 1, 2, 3) 네번째 순서다.
    elif turn == 3:
        # 반시계 방향으로 육각형이 만들어지고 있으므로
        # 네번째 순서의 길이와 앞서 구한 none_length 를 곱하면 over_area 에서 참외밭이 아닌 가짜 면적을 구할 수 있다.
        none_area = none_length * length[1]
        # turn == 2 에서, 첫번째 길이와 세번째 길이 중 무엇이 더 긴지에 따라 over_area 에서 none_area 를 더하거나 빼준다.
        if arr[0][1] > arr[2][1]:
            result = over_area - none_area
            break
        else:
            result = over_area + none_area
            break

print(result*N)