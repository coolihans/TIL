import sys
sys.stdin = open('input.txt')
'''
def choice(cargo, cnt):
    end = cargo[1]
    global answer
    for i in range(len(cargos)):
        if end <= cargos[i][0] and i not in used:
            used[i] = 1
            choice(cargos[i], cnt+1)
            used[i] = 0
    if answer < cnt:
        answer = cnt
    return
'''
# 처음에는 제귀 코드를 짯는데 어느 부분이 잘못 되었는지 모르겠음

T = int(input())
for tc in range(1, T+1):
    cargos = []
    N = int(input())
    for i in range(N):
        cargos.append(list(map(int, input().split())))
    cargos = sorted(cargos, key=lambda x: x[1], reverse=True)
    answer = 1
    start, end = cargos.pop()
    while cargos:
        next_start, next_end = cargos.pop()
        if end <= next_start:
            end = next_end
            answer += 1

    '''
    used = [0] * len(cargos)
    for idx, val in enumerate(cargos):
        used[idx] = 1
        choice(val, 1)
        used[idx] = 0'''
    print(f'#{tc}', answer)