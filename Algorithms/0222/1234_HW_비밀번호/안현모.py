import sys
sys.stdin = open("input.txt")


for tc in range(1, 11):
    # 길이. 번호 따로 받기~
    N, numbers = input().split()
    stack = []
    for i in numbers:
        # 스택이 비어있거나
        if not stack:
            stack.append(i)
        # top이 i 랑 다르다면
        elif stack[-1] != i:
            stack.append(i)
        # 스택에 뭐가 들어있고 top이 i 랑 같을 경우
        else:
            stack.pop()     # pop으로 추출, 그리고 append도 생략.

    answer = ''.join(stack)
    print(f'#{tc} {answer}')
