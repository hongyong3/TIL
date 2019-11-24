import sys
sys.stdin = open("D4_3064_input.txt", "r")

def getSum(i):
    ans = 0
    while i:
        ans += tree[i]
        # 핵심 코드
        # :: 원리 ::
        # 1100이 있다고 생각하면 1100의 2의 보수는 0011에서 + 1을 한 0100
        # 즉, 1100은 val 0100은 - val
        # 이 두개를 & 연산을 하게 된다면 0100이 되는데 이때 1은 최하위 비트 위치를 의미.
        #  위의 예시를 이용하여 일반적인 식을 도출하면 ( i & - i)을 이용하면 최하위 비트를 구할 수 있음.
        i -= (i & - i)  # 최하위 비트 지우기
    return ans

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & - i)  # 최하위 비트 더하기

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data, tree = [0], [0] * (N + 1)
    data.extend(list(map(int, input().split())))
    answer = []
    for i in range(1, N + 1):
        update(i, data[i])

    for _ in range(M):
        c, x, y = map(int, input().split())
        if c == 1:
            update(x, y)
        else:
            answer.append(getSum(y) - getSum(x - 1))
    print("#{}".format(test_case + 1), *answer)

# def calcSum(tree, i):
#     ans = 0
#     while i > 0:
#         ans += tree[i]
#
#         # 핵심 코드
#         # :: 원리 ::
#         # 1100이 있다고 생각하면 1100의 2의 보수는 0011에서 + 1을 한 0100
#         # 즉, 1100은 val 0100은 - val
#         # 이 두개를 & 연산을 하게 된다면 0100이 되는데 이때 1은 최하위 비트 위치를 의미.
#         #  위의 예시를 이용하여 일반적인 식을 도출하면 ( i & - i)을 이용하면 최하위 비트를 구할 수 있음.
#         i -= (i & - i)      # 최하위 비트 지우기
#     return ans
#
# def update(tree, i, diff):
#     while i < len(tree):
#         tree[i] += diff
#         i += (i & - i)
#
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     tree, answer = [0] * (N + 1), []
#     data = [0]
#     data.extend(list(map(int, input().split())))
#
#     for i in range(1, N + 1):
#         update(tree, i, data[i])
#
#     while M:
#         for _ in range(M):
#             C, X, Y = map(int, input().split())
#             if C == 1:
#                 diff = Y - data[X]
#                 data[X] += Y
#                 update(tree, X, diff)
#             else:
#                 answer.append(calcSum(tree, Y) - calcSum(tree, X - 1))
#             M -= 1
#     print("#{}".format(test_case + 1), *answer)