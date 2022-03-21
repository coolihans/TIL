import sys
sys.stdin = open('input.txt')

from itertools import combinations

def solution(kids):
    # 아홉난쟁이 중 일곱 난쟁이로만 이루어진 조합 생성
    seven_kids = list(combinations(kids, 7))
    for kid in seven_kids:
        # 일곱 난쟁이의 합이 백이면 정렬
        if sum(kid) == 100:
            return sorted(kid)

kids = [int(input()) for _ in range(9)]
answers= solution(kids)

for answer in answers:
    print(answer)