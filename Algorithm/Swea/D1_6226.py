ans = []
for i in range(7, 197):
    if not i % 7 and i % 5:
        ans.append(str(i))
print(",".join(ans))