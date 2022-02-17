import sys
sys.stdin = open('input.txt', encoding='UTF-8')


# ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for tc in range(1, T+1):
    case_number, text_len = map(str, input().split())
    text_len = int(text_len)
    text = list(map(str, input().split()))

    for i in range(text_len):
        if text[i] == 'ZRO':
            text[i] = 0
        elif text[i] == 'ONE':
            text[i] = 1
        elif text[i] == 'TWO':
            text[i] = 2
        elif text[i] == 'THR':
            text[i] = 3
        elif text[i] == 'FOR':
            text[i] = 4
        elif text[i] == 'FIV':
            text[i] = 5
        elif text[i] == 'SIX':
            text[i] = 6
        elif text[i] == 'SVN':
            text[i] = 7
        elif text[i] == 'EGT':
            text[i] = 8
        else:
            text[i] = 9

    text2 = sorted(text)

    for j in range(text_len):
        if text2[j] == 0:
            text2[j] = 'ZRO'
        elif text2[j] == 1:
            text2[j] = 'ONE'
        elif text2[j] == 2:
            text2[j] = 'TWO'
        elif text2[j] == 3:
            text2[j] = 'THR'
        elif text2[j] == 4:
            text2[j] = 'FOR'
        elif text2[j] == 5:
            text2[j] = 'FIV'
        elif text2[j] == 6:
            text2[j] = 'SIX'
        elif text2[j] == 7:
            text2[j] = 'SVN'
        elif text2[j] == 8:
            text2[j] = 'EGT'
        else:
            text2[j] = 'NIN'

    print(case_number)
    print(*text2)
