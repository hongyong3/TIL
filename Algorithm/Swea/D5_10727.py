import sys
sys.stdin = open("D5_10727_input.txt", "r")
'''
업데이트 하고 해당셀이, 해당행, 해당열에서 가장 큰값이면 ans += 1
업데이트를 하기 전, 해당행, 열이 값이 작으면 false? 값을 주는 등을 이용해 불필요한 계산을 없애고,
업데이트 후, 해당 셀의 크기를 비교하여 false 값을 만들지를 결정하면???
'''

# # 20 / 29 runtime error
# T = int(input())
# for test_case in range(T):
#     N, M, Q = map(int, input().split())
#     ans = 0
#     data = [list(map(int, input().split())) for _ in range(N)]
#
#     for _ in range(Q):
#         r, c, x = map(int, input().split())
#         data[r - 1][c - 1] = x
#         # 여기에서 가지치기 필요?
#         for i in range(N):
#             chk = True
#             idx = data[i].index(max(data[i]))
#             temp = data[i][idx]
#             for j in range(N):
#                 if temp < data[j][idx]:
#                     chk = False
#                     break
#             if chk:
#                 ans += 1
#     print("#{} {}".format(test_case + 1, ans))

# T = int(input())
# for test_case in range(1):
#     N, M, Q = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
#     col, row = [0] * N, [0] * M
#     ans = 0
#
#     for i in range(N):
#         col[i] = max(data[i])
#
#     for j in range(M):
#         maxRow = 0
#         for i in range(N):
#             if maxRow < data[i][j]:
#                 maxRow = data[i][j]
#         row[j] = maxRow
#
#     for _ in range(Q):
#         r, c, x = map(int, input().split())
#         data[r - 1][c - 1] = x
#         if x > col[r - 1] and x > row[c - 1]:
#             ans += 1
#         if col[r - 1] < x:
#             col[r - 1] = x
#         if row[c - 1] < x:
#             row[c - 1] = x


# chk님의 풀이
def argmax(l):
    f = lambda x: l[x]
    return max(range(len(l)), key=f)


def checker(ridx, cidx):
    count = 0

    fidx, lidx, it = (cidx, ridx, M) if N > M else (ridx, cidx, N)

    for k in range(it):
        count += (lidx[fidx[k]] == k)
    return count


def updateToCarry(nr, nc, nx, rv, cv, ra, ca, init):
    rM = rv[nr - 1]
    cM = cv[nc - 1]
    if rM == cM:
        rv[nr - 1] = nx
        cv[nc - 1] = nx
        return init

    prev_1 = ca[ra[nr - 1]] == nr - 1
    prev_2 = ra[ca[nc - 1]] == nc - 1
    is_rn = rM < nx
    is_cn = cM < nx

    if nx < rM and nx < cM:
        return init

    if is_rn:
        rv[nr - 1] = nx
        ra[nr - 1] = nc - 1

    if is_cn:
        cv[nc - 1] = nx
        ca[nc - 1] = nr - 1

    return init - prev_1 * is_rn - prev_2 * is_cn + is_rn * is_cn


T = int(input())
for test_case in range(T):
    N, M, Q = map(int, input().split())
    ra = [0] * N
    ca = [0] * M
    rv = [0] * N
    for i in range(N):
        row = list(map(int, input().split()))
        ra[i] = argmax(row)
        rv[i] = max(row)
        if i == 0:
            cv = row
        else:
            for j in range(M):
                if row[j] > cv[j]:
                    cv[j] = row[j]
                    ca[j] = i

    init_carry = checker(ra, ca)
    ans = 0
    for _ in range(Q):
        r, c, x = map(int, input().split())
        init = updateToCarry(r, c, x, rv, cv, ra, ca, init_carry)
        ans += init
        init_carry = init

    print("#{} {}".format(test_case + 1, ans))