tmp = 0
numbers = dict()

for i in range(1, 11):
    off, on = map(int, input().split())
    tmp -= off 
    tmp += on
    numbers[tmp] = i
print(max(numbers))
