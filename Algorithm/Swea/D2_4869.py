import sys
sys.stdin = open("D2_4869_input.txt", "r")

# 이전 풀이1
# def paper(a):
#     if a < 2:
#         return 1
#     else:
#         return paper(a-1) + 2 * paper(a-2)
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     a = (N//10)
#     print("#{} {}".format(test_case, paper(a)))

# 이전 풀이2
# def paper(n):
#     if n < 2:
#         return 1
#     else:
#         return paper(n - 1) + paper(n - 2) * 2
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     print("#{} {}".format(test_case, paper(N // 10)))

def paper(n):
    p = [1, 1]
    for i in range(2, n + 1):
        p.append(p[i - 1] + p[i - 2] * 2)
    return p[n]

T = int(input())
for test_case in range(T):
    N = int(input()) // 10
    print("#{} {}".format(test_case + 1, paper(N)))