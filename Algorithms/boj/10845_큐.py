import sys
input = sys.stdin.readline
#
# N = int(input())
# queue = []
#
# for i in range(N):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         queue.append(cmd[1])
#     elif cmd[0] == 'pop':
#         if queue:
#             print(queue.pop(0))
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(queue))
#     elif cmd[0] == 'empty':
#         if queue:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == 'front':
#         if queue:
#             print(queue[0])
#         else:
#             print(-1)
#     elif cmd[0] == 'back':
#         if queue:
#             print(queue[-1])
#         else:
#             print(-1)
#     print(queue)

N = int(input())
Que = []
for i in range(N):
    A = input().split()
    if A[0] == 'push':
        Que.append(A[1])
    elif A[0] == 'pop':
        if Que:
            print(Que.pop(0))
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(Que))
    elif A[0] == 'empty':
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif A[0] == 'front':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[0])

    elif A[0] == 'back':
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[-1])