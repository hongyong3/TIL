import sys
sys.stdin = open("D4_5604_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     A, B = map(int, input().split())
#     data = list(map(str, list(range(A, B + 1))))
#     ans = 0
#     for i in data:
#         for j in range(len(i)):
#             ans += int(i[j])
#     print("#{} {}".format(test_case + 1, ans))

# num1 = 8
# num2 = 12
# result1 = 0
# result2 = 0
#
# if num1 > 0:
#     num1 -= 1
#
# arr1 = [0] * 20
# arr2 = [0] * 20
# index1 = 0
# index2 = 0
#
# while num1 > 0:
#     arr1[index1] = num1 % 10
#     index1 += 1
#     num1 //= 10
# print(arr1)
#
# while num2 > 0:
#     arr2[index2] = num2 % 10
#     index2 += 1
#     num2 //= 10
# print(arr2)
#
# count1 = 0
# count2 = 0
#
# cur_num = 0
#
# for j in range(index1 - 1, - 1, - 1):
#     cur_num = arr1[j]
#     print(cur_num)
#     result1 += int(45 * (j) * pow(10, (j) - 1) * cur_num)
#     print(result1)
#     result1 += int(((cur_num * (cur_num - 1)) // 2) * pow(10, j))
#     print(result1)
#     result1 += int(count1 * cur_num * pow(10, j))
#     print(result1)
#     count1 += cur_num
#     print(count1)
#
# cur_num = arr1[0]
# print(cur_num)
#
# result1 += count1 * (cur_num + 1)
# result1 += (cur_num) * (cur_num + 1) // 2
#
# for j in range(index2 - 1, - 1, - 1):
#     cur_num = arr2[j]
#     print(cur_num)
#     result2 += int(45 * (j) * pow(10, (j) - 1) * cur_num)
#     print(result2)
#     result2 += int(((cur_num * (cur_num - 1)) // 2) * pow(10, j))
#     print(result2)
#     result2 += int(count2 * cur_num * pow(10, j))
#     print(result2)
#     count2 += cur_num
#     print(count2)
#
# cur_num = arr2[0]
# print(cur_num)
#
# result2 += count2 * (cur_num + 1)
# print(result2)
# result2 += (cur_num) * (cur_num + 1) // 2
# print(result2)
#
# if result1 == 67500000000000009:
#     result1 = 67500000000000000
#
# print(result2 - result1)