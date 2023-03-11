import sys
sys.stdin = open("D4_16801_input.txt", "r")

# Runtime Error 6 // 17
T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arrA = sorted(list(map(int, input().split())))
    arrF = sorted(list(map(int, input().split())))[:: - 1]
    dic = {}
    for i in range(N):
        temp = arrA[i] * arrF[i]
        if temp not in dic:
            dic[temp] = [i]
        else:
            dic[temp].append(i)
    chk1, chk2 = 0, 0
    while K:
        arr = sorted(dic.items())[:: - 1]
        for i in arr[0][1]:
            arrA[i] -= 1
            t = arrA[i] * arrF[i]
            if t not in dic:
                dic[t] = [i]
            else:
                dic[t].append(i)
            K -= 1
            if K == 0:
                chk1 = 1
                if i == arr[0][- 1]:
                    del (dic[arr[0][0]])
                    chk2 = 1
                break
        else:
            del(dic[arr[0][0]])
        if chk1:
            break
    ans = arr[1][0] if chk2 else arr[0][0]
    print("#{} {}".format(test_case + 1, ans))