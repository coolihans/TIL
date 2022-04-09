import sys
sys.stdin = open('input.txt')

N = int(input())
# 문제와 다르지만 기둥을 아파트로 대체했다.
apartment = [list(map(int, input().split())) for _ in range(N)]

# 버블소트, 아파트의 위치 오름차순 정렬
for i in range(N-1, -1, -1):
    for j in range(i):
        if apartment[j][0] > apartment[j+1][0]:
            apartment[j], apartment[j+1] = apartment[j+1], apartment[j]

max_height = 0

# 시작 아파트 위치 기준을 0 으로 하여 전체 아파트 위치 재설정
for i in range(N-1, -1, -1):
    apartment[i][0] -= apartment[0][0]
    if apartment[i][1] > max_height:
        max_height = apartment[i][1]  # 가장 높은 아파트의 높이
        max_center = apartment[i][0]  # 가장 높은 아파트의 위치
        center_idx = i                # 전체 아파트 리스트에서 가장 높은 아파트의 인덱스

# 전체 아파트 단지의 가로 길이
max_width = apartment[-1][0]+1
# 가장 높은 아파트의 높이 x 전체 아파트 단지의 면적
all_area = max_height * max_width

left_apartment = apartment[:center_idx:]     # 가장 높은 아파트를 제외한 가장 높은 아파트 기준 좌측 아파트
right_apartment = apartment[center_idx+1::]  # 가장 높은 아파트를 제외한 가장 높은 아파트 기준 우측 아파트

left_max_height = 0
left_area = 0
max_left_center = max_center

while left_apartment:
    # 좌측 아파트에서 가장 높은 아파트의 높이, 위치, 인덱스 구하기
    for i in range(len(left_apartment)):
        if left_apartment[i][1] > left_max_height:
            left_max_height = left_apartment[i][1]
            left_center = left_apartment[i][0]
            left_center_idx = i

    # 가장 높은 아파트를 포함한 좌측 아파트 중 가장 높은 아파트의 [높이차이] * [위치차이] 만큼 left_area 에 저장
    left_area += (max_height-left_max_height) * (max_left_center-left_center)
    # 좌측 아파트에서 가장 높은 아파트의 위치 값을 max_left_center 에 저장
    max_left_center = left_center
    # 좌측 아파트 중 가장 높은 아파트를 제외하고 좌측 아파트 재할당
    left_apartment = left_apartment[:left_center_idx:]
    left_max_height = 0


# 위의 좌측 아파트의 식과 비슷하나, 오른쪽에 위치했다는 점을 유의하여 수정
right_max_height = 0
right_area = 0
max_right_center = max_center
while right_apartment:
    for i in range(len(right_apartment)):
        if right_apartment[i][1] > right_max_height:
            right_max_height = right_apartment[i][1]
            right_center = right_apartment[i][0]
            right_center_idx = i

    right_area += (max_height-right_max_height) * (right_center-max_right_center)
    right_apartment = right_apartment[right_center_idx+1::]
    max_right_center = right_center
    right_max_height = 0

print(all_area - left_area - right_area)
