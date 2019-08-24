import sys
sys.stdin = open("D3_3975_input.txt", "r")

T = int(input())
ans = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    ans = ("ALICE" if A/B > C/D else "DRAW" if A/B == C/D else "BOB")
    print("#{} {}".format(test_case + +1, ans))
    # for i in range(len(ans)):
    #     print("#{} {}".format(test_case + +1, ans[i]))