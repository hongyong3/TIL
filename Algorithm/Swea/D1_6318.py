word = 'abcdef'
ans = {}
for i in range(len(word)):
    ans[word[i]] = i

for k, v in ans.items():
    print("{}: {}".format(k, v))