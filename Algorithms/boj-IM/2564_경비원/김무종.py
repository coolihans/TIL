import sys
sys.stdin = open('input.txt')

def get_positon(direction, position):
    shop_position = []
    if direction == 1:
        shop_position.append(position)
        shop_position.append(height)
    elif direction == 2:
        shop_position.append(position)
        shop_position.append(0)

    elif direction == 3:
        shop_position.append(0)
        shop_position.append(height-position)
    elif direction == 4:
        shop_position.append(width)
        shop_position.append(height-position)
    return shop_position

def get_distance(x, y, shop_x, shop_y):
    tmp1 = 0
    tmp2 = 0
    if x == 0 and shop_x == width:
        tmp1 = y + shop_y + width
        tmp2 = height-y + height-shop_y + width
        if tmp1 < tmp2:
            distance = tmp1
            return distance
        else:
            distance = tmp2
            return distance
    elif x == width and shop_x == 0:
        tmp1 = y + shop_y + width
        tmp2 = height - y + height - shop_y + width
        if tmp1 < tmp2:
            distance = tmp1
            return distance
        else:
            distance = tmp2
            return distance

    elif y == 0 and shop_y == height:
        tmp1 = x + shop_x + height
        tmp2 = width - x + width - shop_x + height
        if tmp1 < tmp2:
            distance = tmp1
            return distance
        else:
            distance = tmp2
            return distance
    elif y == height and shop_y == 0:
        tmp1 = x + shop_x + height
        tmp2 = width - x + width - shop_x + height
        if tmp1 < tmp2:
            distance = tmp1
            return distance
        else:
            distance = tmp2
            return distance
    else:
        distance = abs(shop_x - x)+abs(shop_y-y)
        return distance



width, height = map(int, input().split())
T = int(input())
shops = []
for i in range(T):
    direction, position = map(int, input().split())
    shops.append(get_positon(direction, position))
d, p = map(int, input().split())
guards = get_positon(d, p)
x = guards[0]
y = guards[1]
total = 0
for i in range(T):
    shop_x = shops[i][0]
    shop_y = shops[i][1]
    total += get_distance(x, y, shop_x, shop_y)
print(total)
