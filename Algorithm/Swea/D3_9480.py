import sys
sys.stdin = open("D3_9480_input.txt", "r")

def addAlphabet(s):
    for i in s:
        alphabet[ord(i) - 97] += 1


def subAlphabet(s):
    for i in s:
        alphabet[ord(i) - 97] -= 1


def check():
    for i in range(26):
        if not alphabet[i]:
            return False
    return True


def dfs(idx):
    global ans
    if idx == N:
        return

    for i in range(idx, N):
        addAlphabet(word[i])
        if check():
            ans += 1
        dfs(i + 1)
        subAlphabet(word[i])


T = int(input())
for test_case in range(T):
    N = int(input())
    alphabet = [0] * 26
    word = [list(map(str, input())) for _ in range(N)]
    ans = 0
    dfs(0)
    print("#{} {}".format(test_case + 1, ans))