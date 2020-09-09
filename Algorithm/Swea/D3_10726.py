import sys
sys.stdin = open("D3_10726_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    num = str(bin(M))[2:][:: - 1][:N]
    print(num)
    print("#{} {}".format(test_case + 1, "ON" if not num.count('0') else "OFF"))
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     print("#{} {}".format(test_case + 1, "ON" if not str(bin(M))[2:][:: - 1][:N].count('0') else "OFF"))