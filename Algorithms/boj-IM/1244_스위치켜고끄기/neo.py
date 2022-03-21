N = int(input())
switches = list(map(int, input().split()))
student_cnt = int(input())

for _ in range(student_cnt):
    gender, num = map(int, input().split())
    # 남자 => num 의 배수 스위치를 모두 바꾼다.
    if gender == 1:
        i = 1
        idx = num - 1
        while idx < N:
            switches[idx] ^= 1  # 비트연산자 XOR
            i += 1
            idx = (num*i) - 1

    # 여자 => num 중심으로 좌우대칭인 스위치 모두를 바꾼다.
    else:
        idx = num - 1
        switches[idx] ^= 1
        side = 1
        while 0 <= (idx-side) and (idx+side) < N:
            l, r = switches[idx-side], switches[idx+side]
            if l != r:
                break
            else:
                switches[idx-side] ^= 1
                switches[idx+side] ^= 1
                side += 1

for part_no in range(N // 20 + 1):
    print(' '.join(map(str, switches[20 * part_no: 20 * (part_no + 1)])))
