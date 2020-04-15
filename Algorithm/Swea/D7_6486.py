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
# def powerset(n):
#     if n == N:
#         num = 0
#         for i in range(n):
#             if checked[i]:
#                 num += data[i]
#         if num in arr:
#             arr.remove(num)
#         else:
#             arr.append(num)
#         return
#
#     checked[n] = 0
#     powerset(n + 1)
#     checked[n] = 1
#     powerset(n + 1)
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     arr = []
#     checked = [0] * N
#     powerset(0)
#     ans = arr.pop()
#
#     for i in arr:
#         ans ^= i
#     print("#{} {}".format(test_case + 1, ans))

def sort(b, a, l):
    j, k = 0, 0
    for i in range(a):
        if not b[i] >> l & 1:
            k += 1

    for i in range(a):
        if b[i] >> l & 1:
            k += 1
            t[k] = b[i]

        else:
            j += 1
            t[j] = b[i]

    for i in range(a):
        b[i] = t[i]


a = [0] * 30
c = [0] * 32768
d = [0] * 32768
t = [0] * 32768
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N):
        a[i] = data[i]

    n = N >> 1
    M = N - n
    T, R = 0, 0

    for i in range(1 << n):
        c[i] = 0
        for j in range(n):
            if i >> j & 1:
                c[i] += a[j]

    for i in range(1 << M):
        d[i] = 0
        for j in range(M):
            if i >> j & 1:
                d[i] += a[j + n]

    n = 1 << n
    M = 1 << M

    for i in range(35):
        T = (2 << i) - 1
        sort(c, n, i)
        sort(d, M, i)
        w = x = y = z = 0

        for j in range(n - 1, - 1, - 1):
            while x < M and ((c[j] & T) + (d[x] & T) >> i) < 1:
                x += 1
            while y < M and ((c[j] & T) + (d[y] & T) >> i) < 2:
                y += 1
            while z < M and ((c[j] & T) + (d[z] & T) >> i) < 3:
                z += 1
            w += y - x + M - z

        if w & 1:
            R |= 1 << i
    print(R)