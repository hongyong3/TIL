fruit = ['   apple    ','banana','  melon']
ans = {}
for i in fruit:
    ans[i.strip()] = len(i.strip())
print(ans)