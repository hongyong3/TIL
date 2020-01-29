import sys
sys.stdin = open("D4_5606_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr1 = input()
#     arr2 = input()
#     count, count1, count2, flag = 0, 0, 0, 0
#     q = [[], []]
#
#     while count <= 1000:
#         if count1 >= N and count2 >= N:
#             flag = 1
#             break
#
#         elif count1 < N and count2 < N:
#             if arr1[count1] == 'E':
#                 if arr2[count2] == 'E':
#                     q[1].append(arr2[count2])
#                     count2 += 1
#                 elif len(q[1]) != 0 and q[1][- 1] == 'W':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'W':
#                 if arr2[count2] == 'W':
#                     q[1].append(arr2[count2])
#                     count2 += 1
#                 elif len(q[1]) != 0 and q[1][- 1] == 'E':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'S':
#                 if arr2[count2] == 'S':
#                     q[1].append(arr2[count2])
#                     count2 += 1
#                 elif len(q[1]) != 0 and q[1][- 1] == 'N':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'N':
#                 if arr2[count2] == 'N':
#                     q[1].append(arr2[count2])
#                     count2 += 1
#                 elif len(q[1]) != 0 and q[1][- 1] == 'S':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             q[0].append(arr1[count1])
#             count1 += 1
#
#         elif count1 >= N and count2 < N:
#             if arr2[count2] == 'E':
#                 if len(q[0]) != 0 and q[0][- 1] == 'W':
#                     q[0].pop(- 1)
#                     count1 -= 1
#
#             elif arr2[count2] == 'W':
#                 if len(q[0]) != 0 and q[0][- 1] == 'E':
#                     q[0].pop(- 1)
#                     count1 -= 1
#
#             elif arr2[count2] == 'S':
#                 if len(q[0]) != 0 and q[0][- 1] == 'N':
#                     q[0].pop(- 1)
#                     count1 -= 1
#
#             elif arr2[count2] == 'N':
#                 if len(q[0]) != 0 and q[0][- 1] == 'S':
#                     q[0].pop(- 1)
#                     count1 -= 1
#
#             q[1].append(arr2[count2])
#             count2 += 1
#
#         elif count1 < N and count2 >= N:
#             if arr1[count1] == 'E':
#                 if len(q[1]) != 0 and q[1][- 1] == 'W':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'W':
#                 if len(q[1]) != 0 and q[1][- 1] == 'E':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'S':
#                 if len(q[1]) != 0 and q[1][- 1] == 'N':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             elif arr1[count1] == 'N':
#                 if len(q[1]) != 0 and q[1][- 1] == 'S':
#                     q[1].pop(- 1)
#                     count2 -= 1
#
#             q[0].append(arr1[count1])
#             count1 += 1
#         count += 1
#
#     if flag:
#         print("#{} {}".format(test_case + 1, "YES"))
#     else:
#         print("#{} {}".format(test_case + 1, "NO"))

direction = [['N', 'S'], ['S', 'N'], ['E','W'], ['W', 'E']]

T = int(input())
for test_case in range(T):
    N = int(input())
    arr1 = input()
    arr2 = input()
    count, count1, count2, flag = 0, 0, 0, 0
    q = [[], []]

    while count <= 20000:
        if count1 >= N and count2 >= N:
            flag = 1
            break

        elif count1 < N and count2 < N:
            for i in direction:
                if arr1[count1] == i[0]:
                    if arr2[count2] == i[0]:
                        q[1].append(arr2[count2])
                        count2 += 1
                        break
                    elif len(q[1]) != 0 and q[1][- 1] == i[1]:
                        q[1].pop(- 1)
                        count2 -= 1
                        break

            q[0].append(arr1[count1])
            count1 += 1

        elif count1 >= N and count2 < N:
            for i in direction:
                if arr2[count2] == i[0]:
                    if len(q[0]) != 0 and q[0][- 1] == i[1]:
                        q[0].pop(- 1)
                        count1 -= 1
                        break

            q[1].append(arr2[count2])
            count2 += 1

        elif count1 < N and count2 >= N:
            for i in direction:
                if arr1[count1] == i[0]:
                    if len(q[1]) != 0 and q[1][- 1] == i[1]:
                        q[1].pop(- 1)
                        count2 -= 1
                        break
            q[0].append(arr1[count1])
            count1 += 1
        count += 1

    if flag:
        print("#{} {}".format(test_case + 1, "YES"))
    else:
        print("#{} {}".format(test_case + 1, "NO"))