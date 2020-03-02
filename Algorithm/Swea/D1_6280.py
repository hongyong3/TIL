import sys
sys.stdin = open("D1_6280_input.txt", "r")

# N = int(input())
# ans = []
# for i in range(1, N + 1):
#     if not N % i:
#         ans.append(i)
# print(ans)

N = int(input())
print(list(filter(lambda x: not N % x, range(1, N + 1))))