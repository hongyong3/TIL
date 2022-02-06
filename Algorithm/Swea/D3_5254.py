import sys
sys.stdin = open("D3_5254_input.txt", "r")

# 9 / 10 Runtime Error
# T = int(input())
# for test_case in range(T):
#     N, S = input().split()
#     N = int(N)
#     words = set()
#
#     for i in range(len(S)):
#         for j in range(i + 1, len(S) + 1):
#             words.add(S[i : j])
#     words = sorted(words)
#     print("#{} {} {}".format(test_case + 1, words[N - 1][0], len(words[N - 1])))

# SA = [''] * 1001    # Suffix Array
# g = [''] * 1001     # group
# tg = [''] * 1001    # team group
# '''
# str :: 문자열이 들어갈 배열
# t :: 단어의 위치를 보는 변수
# n :: str의 길이
# g :: 그룹
# tg :: 팀 그룹
# SA :: Suffix Array
# '''
#
# def getSA(s):
#     t = 1
#     n = len(s)
#     for i in range(n):
#         SA[i] = i
#         g[i] = s[i]
#
#     while t <= n:
#         g[n] = - 1
#         sort(SA)
#
#
# T = int(input())
# for test_case in range(1):
#     N, S = input().split()  # 순서, 단어
#     N = int(N)
#     getSA(S)

T = int(input())
for test_case in range(1):
    N, S = input().split()  # 순서, 단어
    N = int(N)
    Slen = len(S)
    arr = []
    for i in range(Slen):
        arr.append((i, S[i:]))
    print(arr)
    newArr = sorted(arr, key = lambda x: x[1])
    print(newArr)