import sys
sys.stdin = open('input.txt')

N = int(input())  # 스위치 개수
lights = list(map(int, input().split()))  # 스위치 상태
students = int(input())
for student in range(students):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number-1, N, number):
            if lights[i]:
                lights[i] = 0
            else:
                lights[i] = 1

    elif gender == 2:
        left = number - 2
        right = number

        if lights[number-1]:
            lights[number-1] = 0
        else:
            lights[number-1] = 1

        while left >= 0 and right < N:
            if lights[left] == lights[right]:
                if lights[left]:
                    lights[left] = 0
                    lights[right] = 0
                else:
                    lights[left] = 1
                    lights[right] = 1
                left -= 1
                right += 1
            else:
                break
start = 0
end = 20
i = 0
while len(lights)//20 >= i:
    print(' '.join(map(str, lights[start:end:])))
    start += 20
    end += 20
    i += 1