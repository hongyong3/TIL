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

def LCP(a, b):
    minlen = min(len(a), len(b))
    cnt = 0
    for i in range(minlen):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt


T = int(input())
for test_case in range(3):
    N, S = input().split()  # 순서, 단어
    N = int(N)
    Slen = len(S)
    arr = []

    # 접미어 배열 생성
    for i in range(Slen):
        arr.append((i, S[i:]))  # (index, s[i])
    # 접미어 배열 정렬
    arr = sorted(arr, key = lambda x: x[1])

    tail = N
    lcp = 0
    idx = 0

    while idx < Slen - 1:
        suffix_idx = arr[idx][0]    # 접미사 인덱스
        curS = arr[idx][1]  # 현재 S
        nextS = arr[idx + 1][1] # 다음 S
        curSlen = len(curS) # 현재 S의 길이

        if curSlen >= tail:
            break
        else:
            lcp = LCP(curS, nextS)  # 만약 lcp가 존재한다면?
            tail -= curSlen
        idx += 1

    print("#{} {} {}".format(test_case + 1, curS[0], len(curS[:lcp + tail])))