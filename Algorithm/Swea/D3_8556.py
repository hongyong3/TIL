import sys
sys.stdin = open("D3_8556_input.txt", "r")

T = int(input())
for test_case in range(T):
    S = input()
    k = 0
    arr = ''
    while k < len(S):
        arr += S[k]
        if S[k] == 'n':
            k += 5
        else:
            k += 4
    print(arr)