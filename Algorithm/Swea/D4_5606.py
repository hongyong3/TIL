import sys
sys.stdin = open("D4_5606_input.txt", "r")

# direction = [['N', 'S'], ['S', 'N'], ['E', 'W'], ['W', 'E']]
#
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr1, arr2 = input(), input()
#     count, count1, count2, flag, q = 0, 0, 0, 0, [[], []]
#
#     while count <= 20000:
#         if count1 == count2 == N:
#             flag = 1
#             break
#
#         elif count1 < N and count2 < N:
#             for i in direction:
#                 if arr1[count1] == i[0]:
#                     if arr2[count2] == i[0]:
#                         q[1].append(arr2[count2])
#                         count2 += 1
#                     elif len(q[1]) != 0 and q[1][- 1] == i[1]:
#                         q[1].pop(- 1)
#                         count2 -= 1
#                     break
#             q[0].append(arr1[count1])
#             count1 += 1
#
#         elif count1 >= N and count2 < N:
#             for i in direction:
#                 if arr2[count2] == i[0]:
#                     if len(q[0]) != 0 and q[0][- 1] == i[1]:
#                         q[0].pop(- 1)
#                         count1 -= 1
#                     break
#             q[1].append(arr2[count2])
#             count2 += 1
#
#         elif count1 < N and count2 >= N:
#             for i in direction:
#                 if arr1[count1] == i[0]:
#                     if len(q[1]) != 0 and q[1][- 1] == i[1]:
#                         q[1].pop(- 1)
#                         count2 -= 1
#                     break
#             q[0].append(arr1[count1])
#             count1 += 1
#
#         count += 1
#
#     if flag:
#         print("#{} {}".format(test_case + 1, "YES"))
#     else:
#         print("#{} {}".format(test_case + 1, "NO"))

direction = [['N', 'S'], ['S', 'N'], ['E', 'W'], ['W', 'E']]

T = int(input())
for test_case in range(T):
    N = int(input())
    arr1, arr2 = input(), input()
    count, count1, count2, flag, q = 0, 0, 0, 0, [[], []]

    while count <= 20000:
        if count1 == count2 == N:
            flag = 1
            break

        elif count1 < N and count2 < N:
            for i in direction:
                if arr1[count1] == i[0]:
                    if arr2[count2] == i[0]:
                        q[1].append(arr2[count2])
                        count2 += 1
                    elif arr2[count2] == i[1]:
                        if len(q[1]) == 0:
                            continue
                        else:
                            q[1].pop(- 1)
                            count2 -= 1
            q[0].append(arr1[count1])
            count1 += 1

        elif count1 == N and count2 < N:
            for i in direction:
                if arr2[count2] == i[0]:
                    if q[0][- 1] == i[1]:
                        q[0].pop(- 1)
                        count1 -= 1
            q[1].append(arr2[count2])
            count2 += 1

        elif count1 < N and count2 == N:
            for i in direction:
                if arr1[count1] == i[0]:
                    if q[1][- 1] == i[1]:
                        q[1].pop(- 1)
                        count2 -= 1
            q[0].append(arr1[count1])
            count1 += 1
        count += 1

    if flag:
        print("#{} {}".format(test_case + 1, "YES"))
    else:
        print("#{} {}".format(test_case + 1, "NO"))