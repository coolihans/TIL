num_switch = int(input())
switch = list(map(int,input().split()))
num_students = int(input())
students = [list(map(int,input().split())) for _ in range(num_students)]

for student in students:
    if student[0] == 1:  # 남자
        for i in range(len(switch)):
            if (i+1) % student[1] == 0:
                switch[i] = int(not switch[i])

    else:  # 여자
        position = student[1]-1
        i=0
        while i <= position and i+position <len(switch):
            if switch[position-i] == switch[position+i]:
                i+=1
            else:
                break
        for ch in range(position-i+1,position+i):
            switch[ch] = int(not switch[ch])



for i in range(1,len(switch)+1):
    print(switch[i-1],end=' ')
    if i%20 == 0:
        print()
