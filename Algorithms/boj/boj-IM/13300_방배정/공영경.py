import sys
sys.stdin = open('input1.txt')

def count_room(men_grade, women_grade):
    room_count = 0

    for grade in men_grade:
        # 방의 최대인원보다 학생수가 많을때
        while grade > k:
            grade -= k
            room_count += 1

        # 1 부터 ~ k 명까지
        if grade != 0:
            room_count += 1

    for grade in women_grade:
        while grade > k:
            grade -= k
            room_count += 1

        if grade != 0:
            room_count += 1
    return room_count

# 학생의 수, 방 최대 인원
n, k = map(int, input().split())

# 성별 학년
students = [list(map(int, input().split())) for _ in range(n)]

# 남/여로 구분
men = [student[1] for student in students if student[0] == 0]
women = [student[1] for student in students if student[0] == 1]

# 구분된 학생들의 학년을 카운트
men_grade = [0] * 6
women_grade = [0] * 6
for man in men:
    men_grade[man-1] += 1

for woman in women:
    women_grade[woman-1] += 1

# 성별, 학년이 구분된 두가지의 리스트를 함수에 입력
answer = count_room(men_grade, women_grade)
print(answer)