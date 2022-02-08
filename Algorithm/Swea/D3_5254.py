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

#######################################################################################

# def LCP(a, b):
#     minlen = min(len(a), len(b))
#     cnt = 0
#     for i in range(minlen):
#         if a[i] == b[i]:
#             cnt += 1
#         else:
#             break
#     return cnt
#
#
# T = int(input())
# for test_case in range(5):
#     N, S = input().split()  # 순서, 단어
#     N = int(N)
#     Slen = len(S)
#     arr = []
#
#     # 접미어 배열 생성
#     for i in range(Slen):
#         arr.append((i, S[i:]))  # (index, s[i])
#     # 접미어 배열 정렬
#     arr = sorted(arr, key = lambda x: x[1])
#     print(arr)
#
#     tail = N
#     lcp = 0
#     idx = 0
#
#     while idx < Slen - 1:
#         suffix_idx = arr[idx][0]    # 접미사 인덱스
#         curS = arr[idx][1]  # 현재 S
#         nextS = arr[idx + 1][1] # 다음 S
#         curSlen = len(curS) # 현재 S의 길이
#
#         if curSlen >= tail + lcp:
#             break
#         else:
#             tail -= curSlen
#             lcp = LCP(curS, nextS)
#
#             # 만약 lcp가 존재한다면? -> 1. lcp + tail >= curSlen이면 curS = nextS로
#
#         idx += 1
#
#     print("#{} {} {}".format(test_case + 1, curS[0], len(curS[:lcp + tail])))

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
for test_case in range(5):
    N, S = input().split()  # 순서, 단어
    N = int(N)
    arr = []

    for i in range(len(S)):
        arr.append(S[i:])
    arr = sorted(arr)

    tail = N
    lcp = 0
    idx = 0

    while idx < len(S) - 1:
        if len(arr[idx]) >= tail + lcp:
            break
        else:
            tail -= len(arr[idx])
            lcp = LCP(arr[idx], arr[idx + 1])
            # 만약 1. lcp + tail > arr[idx]이면 arr[idxcurS = nextS로
        idx += 1

    print("#{} {} {}".format(test_case + 1, arr[idx][0], len(arr[idx][:lcp + tail])))