import sys
sys.stdin = open("D4_13041_input.txt", "r")

# 7 / 28
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    time = list(map(int, input().split()))
    chk = [0] * (K + 1)
    worker = []
    for i in range(N):
        if not chk[arr[i]]:
            chk[arr[i]]= time[i]
            K -= 1
        else:
            if chk[arr[i]] < time[i]:
                worker.append(chk[arr[i]])
                chk[arr[i]] = time[i]
            else:
                worker.append(time[i])
    worker.sort()
    ans = sum(worker[:K])
    print("#{} {}".format(test_case + 1, ans))