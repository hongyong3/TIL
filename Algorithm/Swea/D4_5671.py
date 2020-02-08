import sys
sys.stdin = open("D4_5671_input.txt", "r")



T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())

    alphabetList = [0] * 26
    wordList = []

    for _ in range(M):
        # word = list(set(list(input())))
        word = input()
        wordList.append(word)

        # for i in range(len(word)):