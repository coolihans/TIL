import sys
sys.stdin = open('input.txt')


width, height = map(int, input().split())
N = int(input())
shops = []
for _ in range(N):
    shops.append(list(map(int, input().split())))

dong = list(map(int, input().split()))

print(shops, dong)