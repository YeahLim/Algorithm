dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
total = sum(dwarfs)
flag = 0


for i in range(9):
    for j in range(9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarfs[k])
            flag = 1
            break
    if flag: break
            



