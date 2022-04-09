import sys
sys.stdin = open('input.txt')

def combi(start, level):

    # 전체에서 2명 뽑으면 for문이 2번, 3명 뽑으면 for문이 3번이므로, level은 for문의 횟수로 볼 수 있다.
    if level == K:
        if sum(real_hobbits) == 100:
            real_hobbits.sort()
            print('\n'.join(map(str, real_hobbits)))
        return

    # 첫번째로 뽑힐 수 있는 난쟁이는 0번째 인덱스부터 N-K+level(지금 몇번째 자리의 난쟁이를 뽑는 단계인지)번째 인덱스까지 이다.
    for i in range(start, N-K+level+1):
        # 진짜 난쟁이를 모아 둘 리스트의 level번째 인덱스에 전체 난쟁이에서 i번째 인덱스 난쟁이를 저장
        real_hobbits[level] = all_hobbits[i]
        # 방금 뽑힌 난쟁이 다음번째부터 다음번째 뽑힐 진짜 난쟁이를 구하러 재귀함수
        combi(i+1, level+1)
        # 진짜 난쟁이가 나올 수 있는 경우의 수를 모두 탐색한 후, return 되면 해당 level번째 뽑혔던 난쟁이 값은 초기화해서 반복
        real_hobbits[level] = 0

# 아홉 난쟁이의 정보 받기
all_hobbits = [int(input()) for _ in range(9)]

# 난쟁이 몇명?
N = len(all_hobbits)

# 전체 난쟁이 중 7명만 뽑자
K = 7
real_hobbits = [0] * K

combi(0, 0)