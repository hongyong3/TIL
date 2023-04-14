print(*[1] * 10)
for _ in range(8):
    print(*[1] + [0 for _ in range(8)] + [1])
print(*[1] * 10)