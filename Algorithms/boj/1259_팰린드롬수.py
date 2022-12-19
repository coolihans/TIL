while True:
    a = int(input())
    if a == 0:
        break
    b = str(a)

    if b == b[::-1]:
        print('yes')
    else:
        print('no')