import sys
sys.stdin = open("D3_5948_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = list(map(int, input().split()))
    mat = []
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                sum = N[i] + N[j] + N[k]
                mat.append(sum)
    print("#{} {}".format(test_case + 1, sorted((list(set(mat))))[-5]))