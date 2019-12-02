import sys
sys.stdin = open("정곤이의 단조 증가하는 수_input.txt", "r")
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = []
    answer = []

    for i in range(N):
        j = i + 1
        while j < N:
            ans.append(data[i]*data[j])
            j += 1

    for i in range(len(ans)):
        j = 0
        while j < len(str(ans[i])):
            j += 1
            if ans[i] // 10**j >= ans[i] % 10**j:
                break
            else:
                j += 1
                answer.append(ans[i])
    print("#{} {}".format(test_case+1, max(answer)))