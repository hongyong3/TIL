import sys
sys.stdin = open("D3_1217_Input.txt", "r")


# 방법1 재귀를 이용하지 않는 방법
# for test_case in range(10):
#     N = int(input())
#     N, M = map(int, input().split())
#     print("#{} {}".format(test_case + 1, N ** M))


# 방법2 재귀를 이용한 방법
def power(m):
    global ans
    if m == 0:
        return ans
    ans *= N
    power(m - 1)

for test_case in range(10):
    T = int(input())
    N, M = map(int, input().split())
    ans = 1
    power(M)
    print("#{} {}".format(test_case + 1, ans))