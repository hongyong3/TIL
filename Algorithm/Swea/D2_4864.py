import sys
sys.stdin = open("D2_4864_input.txt", "r")

T = int(input())
for test_case in range(T):
    pattern = input()[:: - 1]
    text = input()
    i = len(pattern) - 1
    ans = 0

    while not ans and i < len(text):
        if pattern[0] != text[i]:
            if text[i] in pattern:
                i += pattern.index(text[i])
            else:
                i += len(pattern)
        else:
            for x, y in zip(range(i, i - len(pattern), - 1), pattern):
                if text[x] == y:
                    ans = 1
                else:
                    ans, i = 0, x
                    break
    print("#{} {}".format(test_case + 1, ans))