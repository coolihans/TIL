import sys
sys.stdin = open('input.txt')

"""
간단한 재귀함수 구현 문제였고
러프하게 구현한 이후에 숫자를 보면서
값을 수정하니 풀리는 문제였다.
"""

def find(number1, number2):
    global cnt
    a = number1
    b = number2
    c = a - b
    if c >= 0:
        cnt += 1
        stack.append(b)
        find(b, c)
    else:
        cnt += 1
        stack.append(b)
        return

N = int(input())
num = []
max = 0
longstack = []
cnt = 0

for i in range(1, N+1):
    num.append(i)

for i in num:
    stack = [N]
    find(N, i)
    if cnt > max:
        max = cnt
    if len(stack) > len(longstack):
        longstack = stack
    cnt = 0

print(max+1)
for i in range(len(longstack)):
    print(longstack[i], end = ' ')