def process_solution(a, k):
    global min
    sum = 0
    for i in range(1, k+1):
        sum += data[i - 1][table[a[i]]]
    if sum < min:
        min = sum

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)




import sys
sys.stdin = open("배열 최소 합_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(data)):
        data[i] = list(map(int, input().split()))
    table = [0 for _ in range(N + 1)]
    for j in range(1, N + 1):
        table[j] = j - 1
    sum = []
    min = 100000

    MAXCANDIDATES = N + 1
    NMAX = N + 1
    a = [0] * NMAX
    backtrack(a, 0, N)
    print(f'#{test_case+1} {min}')