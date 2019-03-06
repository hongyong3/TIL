import sys
sys.stdin = open("폭탄돌리기_input.txt", "r")
K = int(input())
quiz = int(input())
timezero = 0
ans = []

for test_case in range(quiz):
    T, Z = list(input().split())
    ans.append((T, Z))

for i in range(quiz):
    if ans[i][1] == 'T':
        K += 1
        timezero += int(ans[i][0])
        quiz -= 1
        if K == 9:
            K = 1
        if quiz == 0 or timezero >= 210:
            print(K-1)
            break

    elif ans[i][1] == 'F' or ans[i][1] == 'P':
        timezero += int(ans[i][0])
        quiz -= 1
        if quiz == 0 or timezero >= 210:
            print(K)
            break