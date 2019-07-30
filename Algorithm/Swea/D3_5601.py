import sys
sys.stdin = open("D3_5601_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = ""
    for i in range(N):
        ans += "1/" + str(int(N)) + " "
        # ans += str(int(N))
    print("#{} {}".format(test_case + 1, ans))