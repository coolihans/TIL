import sys
input = sys.stdin.readline


E, S, M = map(int, input().split())
X = 1
while X:

  if X%15 == E and X%28 == S and X%19 ==M:
    break

  X += 1

print(X)