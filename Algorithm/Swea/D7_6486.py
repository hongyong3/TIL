import sys
sys.stdin = open("D7_6486_input.txt", "r")

# Runtime Error (23 / 100)
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     arr = []
#
#     for i in range(1 << N):
#         temp = []
#         for j in range(N):
#             if i & (1 << j):
#                 temp.append(data[j])
#         arr.append(sum(temp))
#
#     ans = arr.pop(0)
#
#     for i in arr:
#         ans ^= i
#
#     print("#{} {}".format(test_case + 1, ans))


# Runtime Error (13 / 100)
# def powerset(seq):
#     if len(seq) <= 1:
#         yield seq
#         yield []
#     else:
#         for item in powerset(seq[1:]):
#             yield [seq[0]] + item
#             yield item
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     temp = [sum(x) for x in powerset(data)]
#     arr = []
#
#     for i in set(temp):
#         if temp.count(i) % 2:
#             arr.append(i)
#         else:
#             pass
#
#     ans = arr.pop()
#     for i in arr:
#         ans ^= i
#     print("#{} {}".format(test_case + 1, ans))

# Runtime Error (17 / 100)
def powerset(n):
    if n == N:
        num = 0
        for i in range(n):
            if checked[i]:
                num += data[i]
        if num in arr:
            arr.remove(num)
        else:
            arr.append(num)
        return

    checked[n] = 0
    powerset(n + 1)
    checked[n] = 1
    powerset(n + 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    arr = []
    checked = [0] * N
    powerset(0)
    ans = arr.pop()

    for i in arr:
        ans ^= i
    print("#{} {}".format(test_case + 1, ans))