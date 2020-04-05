import sys
sys.stdin = open("D3_5201_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     w = list(map(int, input().split()))
#     t = list(map(int, input().split()))
#     w.sort(), t.sort()
#     sum = 0
#     while len(w) > 0 and len(t) > 0:
#         if w[-1] <= t[-1]:
#             sum += w[-1]
#             w.pop(), t.pop()
#             continue
#         elif w[-1] > t[-1]:
#             w.pop()
#             continue
#     print("#{} {}".format(test_case+1, sum))

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    dataN = sorted(list(map(int, input().split())))
    dataM = sorted(list(map(int, input().split())))
    ans = 0

    while dataN and dataM:
        if dataN[- 1] <= dataM[- 1]:
            ans += dataN[- 1]
            dataN.pop(), dataM.pop()
        else:
            dataN.pop()
    print("#{} {}".format(test_case + 1, ans))