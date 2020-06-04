import sys
sys.stdin = open("D5_5295_input.txt", "r")

# 1. 중복된 수부터 지우기 -> 어떤 중복된 수를 지울 지 알 수 없으므로 보류
# 2. 중복된 수를 지운 후 모두 포함되지 않은 수 지우기

def xQ(q):
    global ans
    while q:
        num = q.pop()
        if not erase[num]:
            idx = arr1Cnt[num]
            erase[num] = 1
            ans += 1
            arr2Cnt[arr2[idx]] -= 1
            arr3Cnt[arr3[idx]] -= 1
            if arr2Cnt[arr2[idx]] == 0:
                sQ.append(arr2[idx])
            if arr3Cnt[arr3[idx]] == 0:
                tQ.append(arr3[idx])

T = int(input())
for test_case in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))

    ans = 0
    erase = [0] * (N + 1)
    arr1Cnt = [0] * (N + 1) # index별로 순서
    arr2Cnt = [0] * (N + 1) # 각 숫자별로 몇개가 있는지
    arr3Cnt = [0] * (N + 1) # 각 숫자별로 몇개가 있는지
    sQ, tQ = [], []  # 없는 수 Q에 담기

    for i in range(N):
        arr1Cnt[arr1[i]] = i
        arr2Cnt[arr2[i]] += 1
        arr3Cnt[arr3[i]] += 1

    for i in range(1, N + 1):
        if not arr2Cnt[i]:
            sQ.append(i)
        if not arr3Cnt[i]:
            tQ.append(i)

    xQ(sQ), xQ(tQ)

    print("#{} {}".format(test_case + 1, ans))