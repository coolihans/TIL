import sys
sys.stdin = open("input1.txt")

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = w - ((p+t) % w) if ((p+t) // w) % 2 else (p+t) % w
q = h - ((q+t) % h) if ((q+t) // h) % 2 else (q+t) % h

# 3트 만에..
# d = [1, 1]

"""while 1:
    remain_w = w - p if d[0] == 1 else p
    remain_h = h - q if d[1] == 1 else q

    if remain_w == remain_h:
        if remain_w >= t:
            p = p + t * d[0]
            q = q + t * d[1]
            break
        else:
            p = w if d[0] == 1 else 0
            q = h if d[1] == 1 else 0
            d[0] = -d[0]
            d[1] = -d[1]
            t -= remain_w
    elif remain_w < remain_h:
        if remain_w >= t:
            p = p + t * d[0]
            q = q + t * d[1]
            break
        else:
            p = w if d[0] == 1 else 0
            q = q + remain_w * d[1]
            d[0] = -d[0]
            t -= remain_w
    else:
        if remain_h >= t:
            p = p + t * d[0]
            q = q + t * d[1]
            break
        else:
            q = h if d[1] == 1 else 0
            p = p + remain_h * d[0]
            d[1] = -d[1]
            t -= remain_h"""

"""    if p == 0 or p == w:
        d[0] = -d[0]
    if q == 0 or q == h:
        d[1] = -d[1]
    p += d[0]
    q += d[1]"""

print(f'{p} {q}')
