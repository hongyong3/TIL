import sys
sys.stdin = open("Line_test4_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans, answer, dir, dir1, dir2 = [], [], 0, 0, 0
    if N == 2:
        print(1)
        continue
    for i in range(N):
        if data[i] == 1:
            ans.append(i)
    if len(ans) >= 2:
        for j in range(len(ans) - 1):
            k = j + 1
            answer.append(ans[k] - ans[j])
        print(max(answer) // 2)
    else:
        dir1 = int(ans[0])
        dir2 = int(N - int(ans[0]))
        if dir1 > dir2:
            dir = dir1 - 1
        else:
            dir = dir2 - 1
        print(dir)