import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    word = input()
    sentence = input()

    print(sentence.count(word))