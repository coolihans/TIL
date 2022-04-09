import sys
sys.stdin = open('input2.txt')



def match(a_count, b_count):
    for i in range(4, -1, -1):
        if a_count[i] < b_count[i]:
            return f'B'
        elif a_count[i] > b_count[i]:
            return f'A'
        else:
            if i == 0:
                return f'D'
            else:
                continue

T = int(input())
for i in range(T):
    list_a = list(map(int, input().split()))[1:]
    list_b = list(map(int, input().split()))[1:]
    a_count = [0] * 5
    b_count = [0] * 5
    for num in list_a:
        a_count[num] += 1
    for num in list_b:
        b_count[num] += 1
    print(match(a_count, b_count))



