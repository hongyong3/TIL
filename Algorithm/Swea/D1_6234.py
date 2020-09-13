mat = []
for i in range(1, 101):
    if not i % 2:
        mat.append(i)
print(*mat)