arr = [[0] * 10 for _ in range(10)]
for k in range(5):
    for i in range(k, 10 - k):
        arr[k][i] = arr[i][k] = arr[9 - k][i] = arr[i][9 - k] = k + 1

for i in arr:
    print(*i)