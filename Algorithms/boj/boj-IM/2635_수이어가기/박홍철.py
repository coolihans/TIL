import sys
from math import ceil, floor
sys.stdin = open("input.txt")

# 입력받은 수를 a, 다음 수를 b라고 하고 3번째 수부터 a와 b를 통해 표현해보자
# 관찰 결과 피보니차 수열과 연관됨을 알 수 있음
global fibos
fibos = [1, 1]


def fibo_go():
    num = fibos[-1] + fibos[-2]
    fibos.append(num)
    return num


a = int(input())

upperbound = 0
lowerbound = 0
check = True

while 1:
    if check:
        upperbound = floor(fibos[-2] * a / fibos[-1])
    else:
        lowerbound = ceil(fibos[-2] * a / fibos[-1])

    if upperbound <= lowerbound + 1:  # 아직 완전히 납득은 안 가지만...
        break
    else:
        check = not check
        fibo_go()

result = [a, upperbound]

while 1:
    new_one = result[-2] - result[-1]
    if new_one < 0:
        break
    else:
        result.append(new_one)

print(len(result))
print(*result, sep=" ")
