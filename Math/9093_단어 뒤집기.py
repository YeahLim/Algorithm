import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = [word[::-1]  for word in input().split()]
    print(' '.join(answer)) 