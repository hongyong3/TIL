import sys
sys.stdin = open("D3_14511_input.txt", "r")

T = int(input())
for test_case in range(1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans, odd, even = 2, 0, 0

    for i in arr:
        if i % 2:
            odd += 1
        else:
            even += 1

    if abs(odd - even) > 1:
        ans = - 1
    else:
        if N < 3:
            ans = 0

        else:
            chk = [0] * N
            # 경우 1. 짝수 = 홀수 -> [짝, 홀, 짝, 홀, 짝, 홀] or [홀, 짝, 홀, 짝, 홀, 짝]
            if odd == even:
                pass
            # 경우 2. 짝수 < 홀수 -> [홀, 짝, 홀, 짝, 홀]
            elif odd > even:
                idx = 0
                jdx = 1
                while True:
                    if idx % 2 == 0:
                        if arr[idx] % 2:
                            chk[idx] = 1
                            idx += 1
                        else:
                            pass
                    else:
                        if arr[idx] % 2 == 0:
                            chk[idx] = 1
                            idx += 1
                        else:

            # 경우 3. 짝수 > 홀수 -> [짝, 홀, 짝, 홀, 짝]
            else:
                pass
    print("#{} {}".format(test_case + 1, ans))