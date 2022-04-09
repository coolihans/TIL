import sys
sys.stdin = open('input2.txt')



def play(A, B):
    # 그림의 개수를 카운트 하기 위한 리스트 생성
    # 순서대로 세모, 네모, 동그라미, 별의 개수
    picture_1 = [0, 0, 0, 0]
    picture_2 = [0, 0, 0, 0]
    
    # 첫번째 요소는 그림이 아닌 그림의 개수이기 때문에 1부터 반복
    for play in A[1:]:
        picture_1[play-1] += 1

    for play in B[1:]:
        picture_2[play-1] += 1
    
    # 별, 동그라미, 네모, 세모의 순으로 개수를 비교해야하기 때문에 리스트 반대로 순회
    for i in zip(picture_1[::-1], picture_2[::-1]):
        if i[0] > i[1]:
            return 'A'
        elif i[1] > i[0]:
            return 'B'
    return 'D'


N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    winner = play(A, B)
    print(winner)
    