import sys
sys.stdin = open("input.txt")

# 시계방향 거리 = 시계방향 거리 if 시계방향 < 둘레-시계방향 else 둘레-시계방향

width, height = map(int, input().split())
circumference = 2 * (width + height)

num_of_store = int(input())
stores = []
for _ in range(num_of_store + 1):
    direction, move = input().split()

    if direction == '1':
        stores.append(height + int(move))
    elif direction == '2':
        stores.append(circumference - int(move))
    elif direction == '3':
        stores.append(height - int(move))
    else:
        stores.append(circumference // 2 + int(move))

distance_sum = 0
for i in range(num_of_store):
    distance = abs(stores[-1] - stores[i])
    distance_sum += distance if distance <= circumference - distance else circumference - distance

print(distance_sum)



