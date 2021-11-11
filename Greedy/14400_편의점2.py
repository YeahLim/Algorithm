# 영선이는 이번에 편의점으로 창업을 하려고 계획 중이다. 
# 이번 창업을 위해 많은 준비를 하고 있는데, 아직 편의점을 세울 위치를 결정을 하지 못했다. 
# 영선이는 미리 시장조사를 하여, 주요 고객들이 어느 위치에 존재하는지 파악을 하였고, 모든 고객들의 거리의 합을 최소로 하려한다. 
# 두 위치의 거리는 |x1-x2|+|y1-y2|로 정의한다.
# n명의 주요 고객들의 위치 (xi,yi)이 주어질 때, 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력하시오.

# 입력
# 첫째 줄에는 주요 고객들의 수n이 주어진다.(1≤n≤100,000)
# 다음 n줄에는 고객들의 위치 (x,y)가 주어진다.(-1,000,000≤x,y≤1,000,000)

# 출력
# 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력하시오.

import sys
input = sys.stdin.readline
n = int(input())

# location = [sys.stdin.readline().split() for _ in range(n)]
# x, y = [], []
# for lo in location:
#     x.append(int(lo[0]))
#     y.append(int(lo[1]))

x, y = [], []
for _ in range(n):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)
x.sort()
y.sort()

x_conveni, y_conveni = x[n//2], y[n//2]
distance = 0
for i in range(n):
    distance += abs(x_conveni - x[i]) + abs(y_conveni - y[i])

print(distance)