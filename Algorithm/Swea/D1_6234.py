ans = []
for i in range(1, 101):
    if not i % 2:
        ans.append(i)
print(*ans)