mat = []
for i in range(200, 299):
    if not int(str(i)[0]) % 2 and not int(str(i)[1]) % 2 and not int(str(i)[2]) % 2:
        mat.append(str(i))
print(",".join(mat))