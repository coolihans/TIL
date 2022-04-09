import sys
sys.stdin = open('input3.txt')



T = int(input())
metrix = [[0]*1001 for _ in range(1001)]
for i in range(1, T+1):
    x, y, width, height = map(int, input().split())
    for j in range(y, y+height):
        metrix[j][x:(x+width)] = [i]*width


# 시간 복잡도 문제로 인해 무수한 53점. 결국은 지인의 도움 부분 'metrix[j][x:(x+width)] = [i]*width' 통해 해결했다.

for i in range(1, T+1):
    total = 0
    for j in range(1001):
        total += metrix[j].count(i)
    print(total)



