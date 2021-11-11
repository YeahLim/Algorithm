# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
# coins = reversed([int(input()) for _ in range(n)])
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
count = 0
for c in coins:
    if k == 0:
        break
    elif k % c < k:       # if k >= c:
        count += k // c
        k %= c
    else:
        continue
print(count)

# coins.sort()
# while k > 0:
#     c = coins.pop()
#     count += k // c
#     k %= c

# i = 0
# while k > 0:
#     if k >= coins[i]:
#         count += k // coins[i]
#         k %= c
#     i += 1