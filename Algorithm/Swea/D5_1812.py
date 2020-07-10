import sys
sys.stdin = open("D5_1812_input.txt", "r")

# 255 / 1000
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     mTile = [[M, M]]
#     data = sorted(list(map(int, input().split())), reverse = True)
#     ans = 1
#     kTile = []
#     for i in data:
#         kTile.append(pow(2, i))
#
#     while kTile:
#         mTile = sorted(mTile)
#         for i in range(len(mTile)):
#             if mTile[i][0] == 0 or mTile[i][1] == 0:
#                 mTile.pop(i)
#                 break
#             if mTile[i][0] >= kTile[0] and mTile[i][1] >= kTile[0]:
#                 if mTile[i][1] == kTile[0]:
#                     mTile.append([mTile[i][0] - kTile[0], mTile[i][1]])
#                     mTile.pop(0)
#                     kTile.pop(0)
#                     break
#                 a, b = max(mTile[0][0] - kTile[0], kTile[0]), min(mTile[0][0] - kTile[0], kTile[0])
#                 c, d = max(mTile[0][0] - kTile[0], mTile[0][0]), min(mTile[0][0] - kTile[0], mTile[0][0])
#                 mTile.append([a, b])
#                 mTile.append([c, d])
#                 mTile.pop(0)
#                 kTile.pop(0)
#                 break
#         else:
#             mTile = [[M, M]] + mTile
#             ans += 1
#             # break
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans = 1
    mTile = [[M, M]]    # w, h
    data = sorted(list(map(int, input().split())), reverse = True)
    kTile = []
    for i in data:
        kTile.append(pow(2, i))

    for i in kTile:
        chk = True # 타일이 추가로 필요하다면 True
        for j in range(len(mTile)):
            if mTile[j][0] >= i and mTile[j][1] >= i:
                chk = False
                if mTile[j][0] - i:
                    mTile.append([mTile[j][0] - i, mTile[j][1]])
                if mTile[j][1] - i:
                    mTile.append([i, mTile[j][1] - i])
                mTile.pop(j)
                break
        if chk:
            ans += 1
            mTile.append([i, M - i])
            mTile.append([M - i, M])

    print("#{} {}".format(test_case + 1, ans))