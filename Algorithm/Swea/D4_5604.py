import sys
sys.stdin = open("D4_5604_input.txt", "r")

def solve(num, n):
    arr, idx, count = [0] * 20, 0, 0

    while num:
        arr[idx] = num % 10
        idx += 1
        num //= 10

    for i in range(idx - 1, - 1, - 1):
        if i:
            arr[n] += int(45 * i * pow(10, i - 1) * arr[i] + ((arr[i] * (arr[i] - 1)) // 2) * pow(10, i) + count * arr[i] * pow(10, i))
            # ans[n] += int(45 * (i) * pow(10, (i) - 1) * arr[i])
            # ans[n] += int(((arr[i] * (arr[i] - 1)) // 2) * pow(10, i))
            # ans[n] += int(count * arr[i] * pow(10, i))
            count += arr[i]

    arr[n] += count * (arr[0] + 1) + (arr[0] * (arr[0] + 1) // 2)

    if arr[0] == 67500000000000009:
        arr[0] -= 9

    return arr[n]

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    mat = [0, 0]

    if A:
        A -= 1

    print("#{} {}".format(test_case + 1, solve(B, 1) - solve(A, 0)))