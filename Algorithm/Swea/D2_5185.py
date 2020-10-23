import sys
sys.stdin = open("D2_5185_input.txt", "r")

# 이전 풀이
# asc = [[0,0,0,0],   # 0
#        [0,0,0,1],   # 1
#        [0,0,1,0],   # 2
#        [0,0,1,1],   # 3
#        [0,1,0,0],   # 4
#        [0,1,0,1],   # 5
#        [0,1,1,0],   # 6
#        [0,1,1,1],   # 7
#        [1,0,0,0],   # 8
#        [1,0,0,1],   # 9
#        [1,0,1,0],   # A
#        [1,0,1,1],   # B
#        [1,1,0,0],   # C
#        [1,1,0,1],   # D
#        [1,1,1,0],   # E
#        [1,1,1,1]]   # F
#
# ans = [[0,0,1,1,0,1],    # 0
#        [0,1,0,0,1,1],    # 1
#        [1,1,1,0,1,1],    # 2
#        [1,1,0,0,0,1],    # 3
#        [1,0,0,0,1,1],    # 4
#        [1,1,0,1,1,1],    # 5
#        [0,0,1,0,1,1],    # 6
#        [1,1,1,1,0,1],    # 7
#        [0,1,1,0,0,1],    # 8
#        [1,0,1,1,1,1]]    # 9
#
# T = int(input())
# for test_case in range(T):
#     N, M = list(map(str, input().split()))
#     t = []
#
#     def aToh(c):
#         if c <= '9': return ord(c) - ord('0')
#         else: return ord(c) - ord('A') + 10
#
#     for j in range(len(M)):
#         for i in range(4):
#             t.append(asc[aToh(M[j])][i])
#     print("#{}".format(test_case + 1), end=" ")
#     for i in range(len(t)):
#         print(t[i], end="")
#         # print("#{} {}".format(test_case+1, t[i], end=""))
#     print()
#
#     result = []
#     k = len(t)-1
#     while k >= 5:
#         if t[k] == 1:
#             if t[k-5 : k+1] in ans:
#                 result.append(ans.index(t[k-5:k+1]))
#                 k -= 5
#         k -= 1

conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
              'F': 15}

def binary(n):
    temp = ''
    for i in range(4):
        m = str(n % 2)
        n //= 2
        temp = m + temp
    return temp

T = int(input())
for test_case in range(T):
    # N, data = map(str, input().split())
    N, data = input().split()
    mat = ''

    for i in data:
        mat += binary(conversion[i])
    print("#{} {}".format(test_case + 1, mat))