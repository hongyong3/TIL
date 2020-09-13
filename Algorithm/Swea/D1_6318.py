word = 'abcdef'
mat = {}
for i in range(len(word)):
    mat[word[i]] = i

for k, v in mat.items():
    print("{}: {}".format(k, v))