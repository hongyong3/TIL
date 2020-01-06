import sys
sys.stdin =open("종이붙이기_input.txt", "r")

######################################

# solve1
# 주어진 테스트케이스는 통과하지만, 만약 테스트케이스가 엄청 커지면 중복 호출로 인한 stack overflow가 걸린다.
# 이를 해결하기 위해 memoization을 이용하면 수가 엄청 커져도 문제가 없고, 시간복잡도도 좋아진다.

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

######################################
# solve2
# memoization을 이용

def paper(n):
    if n in memo:
        return memo[n]
    if n in (0, 1):
        memo[n] = 1
        return 1
    result = 2 ** n - paper(n - 1)
    memo[n] = result
    return result

T = int(input())
for test_case in range(T):
    N = int(input())
    memo = dict()
    print("#{} {}".format(test_case + 1, paper(N // 10)))