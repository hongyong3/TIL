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
    global combination_list
    while q != 0:
        q = q - 1
        combination_list.append(X[q])
        if len(combination_list) == 3:
            answer.append(combination_list)
            combination_list = []

# 중복조합
def combination(n, r, q):
    if r == 0:
        myprint(q)
    elif n == 0:
        return
    else:
        X[r - 1] = ans[n - 1]
        combination(n, r - 1, q)
        combination(n- 1, r, q)

ans = prime_list(999)
T = int(input())
for test_case in range(T):
    N = int(input())
    answer, combination_list  = [], []
    count = 0

    X = [0] * 3
    combination(len(ans), 3, 3)
    for i in range(len(answer)):
        sum, j  = 0, 0
        while j < 3:
            sum += answer[i][j]
            j += 1
            if j == 3:
                if sum == N:
                    count += 1
    print("#{} {}".format(test_case + 1, count))