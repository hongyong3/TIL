import sys
sys.stdin = open("D4_3234_input.txt", "r")

factorial = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]     # 0~ 9!
exponential = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]           # 2^0 ~ 2^9

def solve(x, left, right):
    global count, sum
    if x >= N:
        count += 1
        return
    if left >= sum(data) - left: # 가지치기 이미 올라가 있는 왼쪽의 추의 무게가 (전체무게 - 왼쪽저울의 무게) 보다 큰 경우
        count += exponential[N - x] * factorial[N -x]
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        solve(x + 1, left + data[i], right) # 왼쪽부터

        if left - (data[i] + right) >= 0:   # 오른쪽
            solve(x + 1, left, right + data[i])
        visited[i] = 0

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    visited, count = [0] * N, 0     # 방문한 곳을 더이상 방문하지 않도록, 즉 중복 방지, 카운트, 총 추의 무게
    solve(0, 0, 0)   # num, left, right
    print("#{} {}".format(test_case + 1, count))