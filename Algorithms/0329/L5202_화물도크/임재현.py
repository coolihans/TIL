import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_slot = [0] * 24  # 24시간 타임슬롯 배열을 만듦.
    cargo_slip = [[0, 0]]  # 1번 화물, 2번 화물 ,,,,, N번 화물까지 리스트 형변환 (화물차 신청서 리스트)
    for _ in range(N):
        cargo_slip.append(list(map(int, input().split())))
    cargo_slip.sort(key=lambda x: x[1])  # 종료 시간 순으로 정렬함.

    for idx, cargo in enumerate(cargo_slip):  # idx는 화물차의 번호를, 그리고 cargo는 화물차가 얼마나 타임슬롯을 차지할지의 신청서
        if set(time_slot[cargo[0]:cargo[1]]) == set([0]):  # 만약 화물차가 들어가고자 하는 타임 슬롯이 전부 비어 있다면,
            time_slot[cargo[0]:cargo[1]] = [idx] * (cargo[1] - cargo[0])  # 해당 화물차의 번호로 타임슬롯을 채움.
        else:  # 만약 해당 타임슬롯 중 일부라도 다른 화물차가 끼어있다면, 패-스
            continue
    print(f'#{tc} {len(set(time_slot)) - 1}')  # 화물차의 대수 출력
