import sys
sys.stdin = open("D4_17299_input.txt", "r")

T = int(input())
for test_case in range(T):
    S = input()
    l = len(S)
    if l % 2:
        l //= 2
        ans = min(int(S[:l]) + int(S[l:]), int(S[:l + 1]) + int(S[l + 1:]))
    else:
        l //= 2
        ans = int(S[:l]) + int(S[l:])
    # print("#{} {}".format(test_case + 1, ans))
    print(f'#{test_case + 1} {ans}')