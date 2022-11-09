import sys
sys.stdin = open("D3_15758_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     S, T = input().split()
#     ans = "yes" if S * len(T) == T * len(S) else "no"
#     print("#{} {}".format(test_case + 1, ans))

for t in range(int(input())):
    S,T=input().split()
    a="yes"if S*len(T)==T*len(S) else "no"
    print("#{} {}".format(t+1,a))