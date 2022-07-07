n = int(input())
fibo, nacci = 0, 1
if n == 0: print(0)
elif n == 1: print(1)
else:
    for _ in range(n-1):
        tmp = fibo + nacci
        fibo = nacci
        nacci = tmp
    print(tmp)