T = int(input())
A, B, C = 300, 60, 10
count_A, count_B, count_C = 0, 0, 0

if T % 10:
    print(-1)

else:
    if T >= A:
        while T >= A:
            T = T - A
            count_A += 1
    if B <= T < A:
        while B <= T < A:
            T = T - B
            count_B += 1
    if C <= T < B:
        while C <= T < B:
            T = T - C
            count_C += 1

    print(count_A, count_B, count_C)

# 선생님 풀이
# T = int(input())
# A = T // 300
# T %= 300
# B = T // 60
# T %= 60
# C = T // 10
# T %= 10
# if T :
#     print(-1)
# else:
#     print(A, B, C)