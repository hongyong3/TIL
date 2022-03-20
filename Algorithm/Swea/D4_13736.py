import sys
sys.stdin = open("D4_13736_input.txt", "r")

'''
A : 나연, B : 다현, K번 반복
    둘 중 사탕의 개수가 더 적은 사람을 X
    더 많은 사람이 Y
    단, 두 사람이 같은 개수의 사탕을 갖고 있다면, 나연이가 X, 다현이가 Y 
'''

# 8 / 150 Runtime Error
# T = int(input())
# for test_case in range(T):
#     A, B, K = map(int, input().split())
#     P, Q = min(A, B), max(A, B)
#     idx = 1
#     arr = []
#     while K:
#         num = P
#         P, Q = P + num, Q - num
#         val = min(Q, P)
#         if val not in arr:
#             arr.append(val)
#         else:
#             break
#         if P > Q:
#             P, Q = Q, P
#         K -= 1
#         idx += 1
#     print("#{} {}".format(test_case + 1, arr[K % idx - 1]))

# 10 / 150 Runtime Error
# T = int(input())
# for test_case in range(T):
#     A, B, K = map(int, input().split())
#     P, Q = min(A, B), max(A, B)
#     cycle = 1
#     arr = [(P, Q)]
#     while K:
#         num = P
#         P, Q = P + num, Q - num
#         if P > Q:
#             P, Q = Q, P
#         if (P, Q) not in arr:
#             arr.append((P, Q))
#         else:
#             break
#         K -= 1
#         cycle += 1
#     print("#{} {}".format(test_case + 1, arr[K % cycle - 1][0]))

# 10 / 150 Runtime Error
# T = int(input())
# for test_case in range(T):
#     A, B, K = map(int, input().split())
#     P, Q = min(A, B), max(A, B)
#     cycle = 1
#     arr = [P]
#     while K:
#         num = P
#         P, Q = P + num, Q - num
#         if P > Q:
#             P, Q = Q, P
#         if P not in arr:
#             arr.append(P)
#         else:
#             break
#         K -= 1
#         cycle += 1
#     print("#{} {}".format(test_case + 1, arr[K % cycle - 1]))

T = int(input())
for test_case in range(T):
    A, B, K = map(int, input().split())
    P, Q = min(A, B), max(A, B)
    cycle = 1
    arr = [P]
    cnt = K
    while cnt:
        num = P
        P, Q = P + num, Q - num
        if P > Q:
            P, Q = Q, P
        if P not in arr:
            arr.append(P)
        else:
            break
        cnt -= 1
        cycle += 1
    print("#{} {}".format(test_case + 1, arr[K % cycle]))