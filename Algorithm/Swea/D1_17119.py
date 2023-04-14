arr = [i for i in range(1, 11)]
print(*arr)
for _ in range(9):
    for i in range(10):
        arr[i] += 10
    print(*arr)