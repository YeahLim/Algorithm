# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
# 둘째 줄에 N자리 숫자가 주어진다. 
# 이 수는 0으로 시작하지 않는다.

# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
number = input()
answer, _k = [], k
for i in range(n):
    while _k > 0 and answer and answer[-1] < number[i]:
        answer.pop()
        _k -= 1
    answer.append(number[i])
print(int(''.join(answer[:n-k])))

# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# number = input()
# answer = []
# start = 0
# end = n - k
# for _ in range(n-k):
#     biggest = number[start]
#     tmp = 0
#     for idx, num in enumerate(number[ start : -1*end ]):
#         if biggest < num:
#             biggest = num
#             tmp = idx
#     answer.append(biggest)
#     start += tmp + 1
#     end -= 1
# print(''.join(answer))