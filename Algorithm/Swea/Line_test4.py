import sys
sys.stdin = open("Line_test4_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    mat, answer, dir, dir1, dir2 = [], [], 0, 0, 0
    if N == 2:
        print(1)
        continue
    for i in range(N):
        if data[i] == 1:
            mat.append(i)
    if len(mat) >= 2:
        for j in range(len(mat) - 1):
            k = j + 1
            answer.append(mat[k] - mat[j])
        print(max(answer) // 2)
    else:
        dir1 = int(mat[0])
        dir2 = int(N - int(mat[0]))
        if dir1 > dir2:
            dir = dir1 - 1
        else:
            dir = dir2 - 1
        print(dir)