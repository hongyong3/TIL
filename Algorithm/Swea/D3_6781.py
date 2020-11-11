import sys
sys.stdin = open("D3_6781_input.txt", "r")

def solve(arr):
    while arr[0]:
        for i in range(1, 10):
            if 0 < arr[i] < 3:
                if arr[i + 1] and arr[i + 2]:
                    arr[i] -= 1
                    arr[i + 1] -= 1
                    arr[i + 2] -= 1
                    arr[0] -= 3
                    break
                else:
                    return "Continue"
            elif arr[i] >= 3:
                arr[i] -= 3
                arr[0] -= 3
                break
    return "Win"

T = int(input())
for test_case in range(T):
    data = list(map(int, input()))
    color = list(map(str, input()))
    R, G, B = [0] * 10, [0] * 10, [0] * 10
    ans = "Win"
    for n, c in zip(data, color):
        if c == 'R':
            R[0] += 1
            R[n] += 1
        elif c == 'G':
            G[0] += 1
            G[n] += 1
        else:
            B[0] += 1
            B[n] += 1
    if R[0]:
        ans = solve(R)
    if G[0]:
        ans = solve(G)
    if B[0]:
        ans = solve(B)
    print("#{} {}".format(test_case + 1, ans))