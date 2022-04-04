import sys
sys.stdin = open("input.txt")

T = int(input())

# 스택으로 ...
for tc in range(1, T+1):
    words = list(input())
    stack = []  # stack -> 빈 값

    for i in range(len(words)):
        # 스택이 비었거나.
        if not stack:
            stack.append(words[i])
        # 스택 마지막 값이 words 해당값과 다를 때 스택에 푸시
        elif stack[-1] != words[i]:
            stack.append(words[i])
        else:   # 스택에 뭐 들어있음 and 스택 마지막 값이 words 해당값과 같을 때 pop 하고 append 도 실행 안하므로 겹치는 문자 다 빠짐.
            stack.pop()
        answer = len(stack)

    print(f'#{tc} {answer}')
