import sys
sys.stdin = open("D6_7794_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, C = map(int, input().split())
    coupon = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        coupon[i][0], coupon[i][1] = map(int, input().split())  # 쿠폰 가격, 쿠폰 할인율
        coupon[i][2] = coupon[i][1] / coupon[i][0]  # 쿠폰 가격 대비 할인 효율
    coupon.sort(key= lambda x : x[2], reverse = True)
    ans = [C, C, 0]

    for i in range(N):
        ans[1] = ans[0] * (100 - coupon[i][1]) / 100
        if ans[0] + ans[2] > ans[1] + ans[2] + coupon[i][0]:
            ans[0] = ans[1]
            ans[2] += coupon[i][0]
        else:
            break
    print("#{} {}".format(test_case + 1, ans[0] + ans[2]))