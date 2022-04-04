import sys
sys.stdin = open("D3_14218_input.txt", "r")

T = int(input())
pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
for test_case in range(T):
    N = int(input())
    print("#{} {}".format(test_case + 1, pi[:N + 2]))