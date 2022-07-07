array = input()
no1 = int(array[0])
no2 = int(array[1])
i = 1
answer = 0

while True:
    print("얍", no1, no2)
    if no1 + 1 == no2:
        answer = no1
        break
    no1 *= 10**i
    no1 += no2
    no2 = int(array[1+i]) * (10**i)
    i += 1
    no2 += int(array[1+i])

print(answer)