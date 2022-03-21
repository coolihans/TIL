import sys

sys.stdin = open('input.txt')

# 학생수
N = int(input())
# 첫번째 학생부터 마지막 학생까지 순서대로 뽑은 번호표
nums = list(map(int, input().split()))
# 결과
result = []

# enumerate 로 몇번째 학생인지 출력하고, go 만큼 새치기 할 수 있다.
for student, go in enumerate(nums):  # 0/0, 1/1, 2/1, 3/3, 4/2
    # 새치기 당한 학생들의 임시 수용소
    stack = []

    # go 횟수만큼 이미 줄서있던 학생들을 임시 수용소로 보낸다.
    for _ in range(go):  # 0, 1, 1, 3, 2
        stack.append(result.pop())

    # 임시 수용소에 먼저 들어온 학생이 사실 가장 마지막에 줄서있던 학생이었으므로 정렬
    for j in range(1, len(stack) // 2 + 1):
        stack[j - 1], stack[-j] = stack[-j], stack[j - 1]

    # 이미 줄서있던 학생들을 임시수용소로 보낸 상태에서 학생을 줄세운다.
    result.append(student + 1)
    # 임시수용소 학생들을 다시 줄세운다.
    result += stack

print(' '.join(map(str, result)))