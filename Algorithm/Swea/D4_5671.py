import sys
sys.stdin = open("D4_5671_input.txt", "r")

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

A = input()
T = ''
for i in A:
    if i.isdigit():
        T += i
for test_case in range(int(T)):
    NM = ['', '']
    A = input()
    k = 0
    for i in A:
        if i.isdigit():
            NM[k] += i
        if i == ' ':
            k += 1

    N, M = int(NM[0]), int(NM[1])

    alphabetList = []
    alphabet = [0] * 26
    wordSet = set()
    wordList = []
    ans = 0

    for _ in range(N):
        data = input()
        word = ''
        for i in data:
            if i in 'bcdfghjklnmpqrstvwxyz':
                word += i
        wordList.append(word)
        wordSet.update(word)
        for i in wordSet:
            alphabet[ord(i) - 97] += 1
        wordSet.clear()

    # while M:
    #     maxCount = 0
    #     maxAlphabet = 0
    #     for i in range(len(alphabet)):
    #         if maxCount < alphabet[i]:
    #             maxAlphabet = i
    #             maxCount = alphabet[i]
    #     alphabet[maxAlphabet] = 0
    #     alphabetList.append(chr(maxAlphabet + 97))
    #     M -= 1

    while M:
        maxCount = 0
        maxAlphabet = 0
        maxAlphabet = alphabet.index(max(alphabet))
        maxCount = alphabet[maxAlphabet]
        alphabet[maxAlphabet] = 0
        alphabetList.append(chr(maxAlphabet + 97))
        M -= 1

    for i in wordList:
        flag = True
        for j in i:
            if j not in alphabetList:
                flag = False
        if flag:
            ans += 1
    print("#{} {}".format(test_case + 1, ans))