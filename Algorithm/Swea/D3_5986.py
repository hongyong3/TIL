import sys
sys.stdin = open("D3_5986_input.txt", "r")

# 소수
def prime_list(n):
    # 에라토스테네스의 체 초기화: n 개의 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m= int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:    # i가 소수인 경우
            for j in range(i + i, n, i):    # i 이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def myprint(q):
    while q != 0:
        q = q - 1
        print("%d" % (T[q]), end=" ")
        answer.append(T[q])
    print()

# 중복조합
def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:
        return
    else:
        T[r - 1] = ans[n - 1]
        combination(n, r - 1, q)
        combination(n- 1, r, q)

T = int(input())
for test_case in range(1):
    N = int(input())
    ans, answer, sum, count = [], [], 0, 0
    ans = prime_list(N)

    T = [0] * 3
    combination(len(ans), 3, 3)
    for i in range(0, len(answer), 3):
        sum += i
        if sum == N:
            count +=1
    print(answer)
    print(count)