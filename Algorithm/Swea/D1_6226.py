mat = []
for i in range(7, 197):
    if not i % 7 and i % 5:
        mat.append(str(i))
print(",".join(mat))