import sys
sys.stdin = open('input2.txt')

n, k = map(int, input().split())
# 입력받은 온도 리스트
temps = list(map(int, input().split()))

# 처음 k일 수 만큼의 합
conti_temps = [sum(temps[0:0+k])]
# 이후 k일수 만큼의 합 구하기
for i in range(1, n-k+1):
    sum_temps = conti_temps[-1] + temps[i+k-1] - temps[i-1]
    conti_temps.append(sum_temps)

max_temps = conti_temps[0]
for temp in conti_temps[1:]:
    if max_temps < temp:
        max_temps = temp
print(max_temps)