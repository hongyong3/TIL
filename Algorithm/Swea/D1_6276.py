ans = [[] for _ in range(8)]
for i in range(1, 8):
    for j in range(1, 10):
        if (i + 1) * j % 3 and (i + 1) * j % 7:
            ans[i - 1].append((i + 1) * j)
print(ans)