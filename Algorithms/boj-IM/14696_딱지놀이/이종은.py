import sys
sys.stdin = open('input1.txt')

N = int(input())
for r in range(1, N + 1):
    # A의 카드
    A = list(map(int, input().split()))
    # B의 카드
    B = list(map(int, input().split()))

    # 각 카드의 첫째값은 카드의 개수이므로 pop
    A_len = A.pop(0)
    B_len = B.pop(0)

    # 버블소트로 내림차순 정렬
    for i in range(A_len - 1, -1, -1):
        for j in range(i):
            if A[j + 1] > A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]

    for i in range(B_len - 1, -1, -1):
        for j in range(i):
            if B[j + 1] > B[j]:
                B[j + 1], B[j] = B[j], B[j + 1]

    while True:
        # A와 B의 각 첫번째 카드가 같다면 (내림차순 돼서 4, 3, 2, 1 순 정렬) pop
        if A[0] == B[0]:
            A.pop(0)
            B.pop(0)
            # 만약 A 카드가 소진 됐다면 B 우승
            if not A:
                # B 카드도 소진 됐다면 무승부
                if not B:
                    print('D')
                    break
                print('B')
                break
            # 만약 B 카드만 소진 됐다면 A 우승
            elif not B:
                print('A')
                break

        # 내림차순 정렬된 A의 첫번째 카드가 크다면 A 우승
        elif A[0] > B[0]:
            print('A')
            break
        # 내림차순 정렬된 B의 첫번째 카드가 크다면 B 우승
        elif A[0] < B[0]:
            print('B')
            break