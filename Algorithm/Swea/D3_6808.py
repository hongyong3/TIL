import sys
sys.stdin = open("D3_6808_input.txt", "r")


def solve(depth, inSum, kyuSum):
    global ans
    if depth == 9 and inSum > kyuSum:
        ans += 1
        return

    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            if kyuArr[depth] > inArr[i]:
                solve(depth + 1, inSum, kyuSum + kyuArr[depth] + inArr[i])
            else:
                solve(depth + 1, inSum + kyuArr[depth] + inArr[i], kyuSum)
            visited[i] = 0


T = int(input())
for test_case in range(T):
    kyuArr = list(map(int, input().split()))
    inArr = []
    visited = [0] * 9
    ans = 0
    for i in range(1, 19):
        if i not in kyuArr:
            inArr.append(i)
    solve(0, 0, 0)
    print("#{} {} {}".format(test_case + 1, 362880 - ans, ans))