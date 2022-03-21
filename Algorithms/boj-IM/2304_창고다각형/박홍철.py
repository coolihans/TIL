import sys

sys.stdin = open("input.txt")


num_of_building = int(input())

buildings = []

for _ in range(num_of_building):
    a, b = map(int, input().split())
    for i in range(len(buildings)+1):
        if i == len(buildings):
            buildings.append([a, b])
            break
        else:
            if a < buildings[i][0]:
                buildings.insert(i, [a, b])
                break

print(buildings)

area = 0
height = buildings[0][1]
curve_point = buildings[0][0]

for i in range(1, num_of_building):
    if buildings[i][1] >= height:
        area += (buildings[i][0] - curve_point) * height
        height = buildings[i][1]
        curve_point = buildings[i][0]

max_point = curve_point
max_height = height

if max_point != buildings[-1][0]:
    height = buildings[-1][1]
    curve_point = buildings[-1][0]

    for i in range(num_of_building-1, -1, -1):
        if buildings[i][1] >= height:
            area += (curve_point - buildings[i][0]) * height
            height = buildings[i][1]
            curve_point = buildings[i][0]
            if curve_point == max_point:
                break

area += max_height

print(area)
