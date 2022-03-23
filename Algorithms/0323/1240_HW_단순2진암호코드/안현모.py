import sys
sys.stdin = open("input.txt")

num_pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
                '0001011']


def is_valid(code_nums):
    # 숫자로 바꾸기
    for i in range(8):
        for j in range(10):
            if code_nums[i] == num_pattern[j]:
                code_nums[i] = j
    # 홀수 * 3 + 짝 + 마지막 = 10배수
    valid_sum = 0
    sum = 0
    for i in range(8):
        sum += code_nums[i]
    for i in range(7):
        if i%2 == 0:
            valid_sum += code_nums[i] * 3
        else:
            valid_sum += code_nums[i]
    valid_sum += code_nums[7]
    if valid_sum % 10:
        return 0
    else:
        return sum


def getcode(arr):
    code = []
    for i in range(N):
        if '1' in arr[i]:
            for j in range(-1, -M - 1, -1):
                if arr[i][j] == '1':
                    code.append(arr[i][j - 55:j + 1])
                    break
    return code


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    # arr 에서 code 있는지 확인하고 빼내야함.
    code = getcode(arr)
    # list에서 빼버리기
    code = code[0]
    code_nums = []
    for i in range(0, len(code), 7):
        code_nums.append(code[i: i+7])
    answer = is_valid(code_nums)

    print(f'#{tc} {answer}')

