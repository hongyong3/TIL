fruit = ['   apple    ','banana','  melon']
mat = {}
for i in fruit:
    mat[i.strip()] = len(i.strip())
print(mat)