import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    weight = sorted(weight,reverse=True)
    truck = sorted(truck,reverse=True)

    result = 0
    for w in weight:
        if w <= truck[0]:
            result+=w
            truck.remove(truck[0])
        if not truck:
            break

    print(f'#{t+1} {result}')

