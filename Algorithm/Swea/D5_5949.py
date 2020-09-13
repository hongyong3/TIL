import sys
sys.stdin = open("D5_5949_input.txt", "r")

# S와 T의 두 문자열의 a, b의 갯수는 동일
# 완전검색은 O(N^2) 시간초과
# S, T의 각 인덱스의 문자가 같다면 pass?
# 첫 번째 틀린 문자와 다음 첫 번째 틀린 문자를 교환?
# 두 번째 틀린 문자와 다음 두 번째 틀린 문자를 교환한다면?
# O(N)?

T = int(input())
for test_case in range(T):
    S = input()
    T = input()
    mat, aCount, bCount = 0, 0, 0
    a, b = [0] * len(S), [0] * len(T)
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i] == 'a':
            a[aCount] = i
            aCount += 1
        else:
            b[bCount] = i
            bCount += 1

    for i in range(aCount):
        mat += (a[i] - b[i] if a[i] > b[i] else b[i] - a[i])
    print("#{} {}".format(test_case + 1, mat))