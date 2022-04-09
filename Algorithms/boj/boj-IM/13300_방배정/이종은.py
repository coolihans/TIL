import sys
sys.stdin = open('input1.txt')

# N=총학생수, K=방 최대 수용인원
N, K = map(int, input().split())
# 학년별 성별 구분 2차원 배열 생성
arr = [[0, 0] for _ in range(6)]

# 학생의 성별, 학년에 따라 해당하는 arr 인덱스에 += 1
for _ in range(N):
    gender, grade = map(int, input().split())
    arr[grade-1][gender] += 1

room = 0
# 전체 학생 정보가 저장된 2차원 배열 arr 를 순회하며 필요한 방의 개수를 구한다.
# K로 나눈 몫만큼 방이 필요하고, 나머지가 있다면 방을 하나 더 추가한다.
for i in range(6):
    for j in range(2):
        room += arr[i][j]//K
        if arr[i][j]%K:
            room += 1
print(room)