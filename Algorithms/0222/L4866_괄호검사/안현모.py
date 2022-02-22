import sys
sys.stdin = open("input.txt")


def f(string):
    stack = []
    for i in string:
        # 안받는 거 말고 받는 거 부터 받기..
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')' or i == '}':
            if stack:               # stack 이 안 비었으면~
                top = stack.pop()
                if i == ')':
                    # { 이면 0, ( 면 지나가기~
                    if top == '{':
                        return 0
                elif i == '}':
                    # ( 이면 0, { 면 지나가기~
                    if top == '(':
                        return 0
            else:
                return 0             # stack 이 비었으면 그냥 0임
        else:
            continue
    # 뭐가 남았으면 return 0  => (((()) or ))) 이런 경우. for 문 이후 결정
    # 다 없어져야 검사 통과.
    if stack:
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    print(f'#{tc} {f(string)}')

# top = stack[-1] 이거 쓰면 안됨.. = > 빈 상태에서 '}' 받을 때 이상함.. 더 고려해야됨

