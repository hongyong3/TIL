T= input()
stack = []
ans = 0

for i in T:
    if not stack:
        stack.append(i)
        ans += 10
    elif stack[-1] == i:
        stack.append(i)
        ans += 5
    else:
        stack.append(i)
        ans += 10

print(ans)

# 선생님 풀이
# arr = input()
# tot = 10
# for i in range(1, len(arr)):
#     if arr[i] == arr[i-1]:
#         tot += 5:
#     else:
#         tot += 10
# print(tot)