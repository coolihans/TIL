hgt = []
for i in range(9):
    H = int(input())
    hgt.append(H)
real = []
for i in range(2**9):
    list = []
    for j in range(9):
        if i & (1<<j):
            list.append(hgt[j])
    if len(list) == 7 and sum(list) == 100:
        real = list
for i in range(7):
    for j in range(7-i-1):
        if real[j] > real[j+1]:
            real[j], real[j+1] = real[j+1], real[j]
for i in range(7):
    print(real[i])