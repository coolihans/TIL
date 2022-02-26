import sys
sys.stdin = open('input.txt')

list1 = []
for i in range(9):
    list1.append(int(input()))
target = sum(list1) - 100
target_num1 = 0
target_num2 = 0
for idx in range(9):
    num1 = list1[idx]
    for i in range(9):
        if i != idx:
            if num1 + list1[i] == target:
                target_num1 = idx
                target_num2 = i
                break
list1.pop(target_num1)
list1.pop(target_num2)
final_list = sorted(list1)
for c in final_list:
    print(c)
