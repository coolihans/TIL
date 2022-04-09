import sys
sys.stdin = open("input.txt")

width, height = map(int, input().split())

num_of_cut = int(input())

width_cut = [0]
height_cut = [0]
cuts = [height_cut, width_cut]
length = [[], []]
area = 1

for _ in range(num_of_cut):
    d, w = map(int, input().split())
    if len(cuts[d]) == 1:
        cuts[d].append(w)
    else:
        for i in range(len(cuts[d])):
            if w > cuts[d][i]:
                continue
            else:
                cuts[d].insert(i, w)
                break
        else:
            cuts[d].append(w)
else:
    width_cut.append(width)
    height_cut.append(height)

for k in range(2):
    for i in range(len(cuts[k])-1):
        length[k].append(cuts[k][i+1] - cuts[k][i])
    area *= max(length[k])

print(area)

