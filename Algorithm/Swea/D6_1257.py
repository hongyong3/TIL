import sys
sys.stdin = open("D6_1257_input.txt", "r")

'''
food는
모든 부분 문자열을 찾은 후 정렬하면 시간초과 걸릴 듯..
1개 -> f, o, o, d ->  f, o, d (중복 제거) => 3개
2개 -> fo, oo, od -> fo, od => 2개
3개 -> foo, ood => 2개
4개 -> food => 1개

----------------------------

1. 문자열에 대한 접미사
문자열     index
food        0
 ood        1
  od        2
   d        3

2. 사전순 정렬
문자열     index
   d        3
food        0
  od        2
 ood        1

이후 어찌해야하지..

'''

# 1번 시도
# T = int(input())
# for test_case in range(8):
#     N = int(input())
#     word = input()
#     perms = []
#     for i in range(len(word) + 1):
#         for j in range(i, len(word) + 1):
#             if word[i:j] not in perms:
#                 perms.append(word[i:j])
#     ans = sorted(perms)[N] if len(perms) > N else 'none'
#     print("#{} {}".format(test_case + 1, ans))


T = int(input())
for test_case in range(T):
    K = int(input())
    word = input()
    mat = set()
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            mat.add(word[i:j])
    mat = sorted(mat)[K - 1] if K <= len(mat) else 'none'
    print("#{} {}".format(test_case + 1, mat))