min, max = map(int, input().split())
cnt, total, answer = 0, 0, 0

for i in range(1, 46):
    for j in range(i):
        cnt += 1
        total += i
        if cnt == min-1:
            answer -= total
        if cnt == max:
            answer += total
            break
print(answer)