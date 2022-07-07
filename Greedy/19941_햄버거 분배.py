n, k = map(int, input().split())
array = list(input())
cnt = 0

for i in range(n):
    if array[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and array[j] == 'H':
                cnt += 1
                array[j] = 'X'
                break
print(cnt)   
