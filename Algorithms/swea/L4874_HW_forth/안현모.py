import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    stack = []
    string = list(input().split())      # 문자열
    operate_list = ['+', '-', '*', '/']
    result = None
    for s in string:
        # 연산자일 경우
        if s in operate_list:
            # 우선 숫자 두개는 있어야됨. 아니라면 error 나고 바로 break
            if len(stack) < 2:
                result = 'error'
                break
            # 숫자 두개 뽑음 순서대로 위에서부터/ int로 변환
            s1 = int(stack.pop())
            s2 = int(stack.pop())
            if s == '+':
                result = s2 + s1
                stack.append(result)
            elif s == '-':
                result = s2 - s1
                stack.append(result)
            elif s == '*':
                result = s2 * s1
                stack.append(result)
            elif s == '/':
                result = s2 // s1
                stack.append(result)
        elif s == '.':
            # 마지막에 나왔을 때 pop으로 뽑아주기
            if len(stack) == 1:
                result = stack.pop()
            # 마지막이 아니면 error 내고 바로 break
            else:
                result = 'error'
                break
        # 피연산자일 경우 else 로 처리
        else:
            stack.append(s)

    print(f'#{tc} {result}')

