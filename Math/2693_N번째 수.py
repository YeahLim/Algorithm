from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[-3])

