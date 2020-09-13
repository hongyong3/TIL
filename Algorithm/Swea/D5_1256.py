import sys
sys.stdin = open("D5_1256_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    word = input()
    mat = []
    for i in range(len(word)):
        mat.append(word[i:])
    print("#{} {}".format(test_case + 1, sorted(mat)[N - 1]))