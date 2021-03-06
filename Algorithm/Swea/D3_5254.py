import sys
sys.stdin = open("D3_5254_input.txt", "r")

# 9 / 10 Runtime Error
# 접미어배열 공부하기..
T = int(input())
for test_case in range(T):
    N, S = input().split()
    words = set()

    idx = 0
    while idx < len(S):
        for i in range(idx + 1, len(S) + 1):
            words.add(S[idx: i])
        idx += 1
    words = sorted(list(words))
    print("#{} {} {}".format(test_case + 1, words[int(N) - 1][0], len(words[int(N) - 1])))
