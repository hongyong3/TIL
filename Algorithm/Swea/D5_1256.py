import sys
sys.stdin = open("D5_1256_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    word = input()
    ans = []
    for i in range(len(word)):
        ans.append(word[i:])
    print("#{} {}".format(test_case + 1, sorted(ans)[N - 1]))