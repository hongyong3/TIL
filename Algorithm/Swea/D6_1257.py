import sys
sys.stdin = open("D6_1257_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     K = int(input())
#     S = input()
#     words =[S[i:] for i in range(len(S))]
#     print(words)
#
#     ans = sorted(words)[:K - 1] if K <= len(words) else 'none'
#     print(ans)
T = int(input())
for test_case in range(T):
    N = int(input())
    word = input()
    ans = []
    for i in range(len(word)):
        ans.append(word[:i + 1])
    print(sorted(ans))
    # print("#{} {}".format(test_case + 1, sorted(ans)[N - 1]))