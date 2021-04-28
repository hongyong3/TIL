import sys
sys.stdin = open("D3_11856_input.txt", "r")

T = int(input())
for test_case in range(T):
    S = sorted(list(input()))
    ans = "No"
    if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
        ans = "Yes"
    print("#{} {}".format(test_case +1, ans))