import sys
sys.stdin = open("D4_13432_input.txt", "r")

def findPrimes():
    arr = [1] * 110
    for i in range(2, int(pow(110, 0.5))):
        if arr[i]:
            j = 2
            while i * j <= 109:
                arr[i * j] = 0
                j += 1
    return [i for i in range(2, 110) if arr[i]]

primeNum = findPrimes()

def factorization(x):
    arr = [x]
    d = 2
    while d <= x:
        if x % d:
            d += 1
        else:
            arr.append(d)
            x //= d
    return sorted(arr)

T = int(input())
for test_case in range(T):
    n, s, t = map(int, input().split())
    ans = - 1
    if s == t:
        ans = 0
    elif s == 1 or t == 1:
        ans = - 1
    else:
        sArr, tArr = factorization(s), factorization(t) # 소인수 분해
        chk = False # 서로소인지 확인 True이면 아님
        for i in sArr:
            if i in tArr:
                chk = True
                break
        if chk:
            ans = 1
        else:
            if sArr[0] * tArr[0] <= n:
                ans = 2
    print("#{} {}".format(test_case + 1, ans))