import sys
sys.stdin = open("D4_5671_input.txt", "r")

# 1번 -> input이 이상함
# T = int(input())
# for test_case in range(int(T)):
#     N, M = map(int, input().split())
#     word = [input() for _ in range(M)]
#     ans = 0
#     alphabetList = []
#     alphabet = [0] * 26
#     wordSet = set()
#
#     for i in word:
#         wordSet.update(i)
#         for j in wordSet:
#             alphabet[ord(j) - 97] += 1
#
#     while M:
#         maxCount = 0
#         maxAlphabet = 0
#         for i in range(len(alphabet)):
#             if maxCount < alphabet[i]:
#                 maxAlphabet = i
#                 maxCount = alphabet[i]
#         alphabet[maxAlphabet] = 0
#         alphabetList.append(chr(maxAlphabet + 97))
#         M -= 1
#
#     for i in word:
#         flag = True
#         for j in i:
#             if j not in alphabetList:
#                 flag = False
#                 break
#         if flag:
#             ans += 1
#     print("#{} {}".format(test_case + 1, ans))

# 2번 -> 9/50
# A = input()
# T = ''
# for i in A:
#     if i.isdigit():
#         T += i
# for test_case in range(int(T)):
#     NM = ['', '']
#     A = input()
#     k = 0
#     for i in A:
#         if i.isdigit():
#             NM[k] += i
#         if i == ' ':
#             k += 1
#
#     N, M = int(NM[0]), int(NM[1])
#
#     alphabetList = []
#     alphabet = [0] * 26
#     wordSet = set()
#     wordList = []
#     ans = 0
#
#     for _ in range(N):
#         data = input()
#         word = ''
#         for i in data:
#             if i in 'bcdfghjklnmpqrstvwxyz':
#                 word += i
#         wordList.append(word)
#         wordSet.update(word)
#         for i in wordSet:
#             alphabet[ord(i) - 97] += 1
#         wordSet.clear()
#
#     # while M:
#     #     maxCount = 0
#     #     maxAlphabet = 0
#     #     for i in range(len(alphabet)):
#     #         if maxCount < alphabet[i]:
#     #             maxAlphabet = i
#     #             maxCount = alphabet[i]
#     #     alphabet[maxAlphabet] = 0
#     #     alphabetList.append(chr(maxAlphabet + 97))
#     #     M -= 1
#
#     while M:
#         maxCount = 0
#         maxAlphabet = 0
#         maxAlphabet = alphabet.index(max(alphabet))
#         maxCount = alphabet[maxAlphabet]
#         alphabet[maxAlphabet] = 0
#         alphabetList.append(chr(maxAlphabet + 97))
#         M -= 1
#
#     for i in wordList:
#         flag = True
#         for j in i:
#             if j not in alphabetList:
#                 flag = False
#         if flag:
#             ans += 1
#     print("#{} {}".format(test_case + 1, ans))

# 3번
def solve(n, idx, count):
    global ans
    if (26 - idx < count):
        return

    if (idx == 26 and count != 0):
        return

    if count == 0:
        ans = max(ans, check(n))
        return

    if alphabet & (1 << idx) != 0:
        solve(n | (1 << idx), idx + 1, count - 1)
    solve(n, idx + 1, count)


def check(n):
    ret = 0
    for i in range(N):
        if ((n & wordList[i]) == wordList[i]):
            ret += 1
    return ret


T = int(input().replace('혻', ''))
for test_case in range(T):
    N, M = map(int, input().replace('혻', '').split())
    wordList = [0] * N
    alphabet = 0
    ans = 0

    for _ in range(N):
        word = str(input().replace('혻', ''))
        var = 0
        for i in range(len(word)):
            temp = ord(word[i]) - 97
            var |= (1 << temp)
            alphabet |= (1 << temp)
        wordList[_] = var

    wordCount = bin(alphabet).count('1')

    solve(0, 0, min(M, wordCount))
    print("#{} {}".format(test_case + 1, ans))