number = int(input())
num, cnt = 1, 0

while num < number:
    if num * 3 <= number:
        num *= 3
    elif num * 2 <= number:
        num *= 2
    else:
        num += 1
    cnt += 1

num, cnt_ = 1, 0
while num < number:
    if num * 2 <= number:
        num *= 2
    elif num * 3 <= number:
        num *= 3
    else:
        num += 1
    cnt_ += 1

print(cnt if cnt < cnt_ else cnt_)