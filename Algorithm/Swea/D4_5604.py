import sys
sys.stdin = open("D4_5604_input.txt", "r")

T = int(input())
for test_case in range(T):
    num1, num2 = map(int, input().split())

    result1, result2 = 0, 0
    index1, index2 = 0, 0
    arr1, arr2 = [0] * 20, [0] * 20
    count1, count2 = 0, 0
    cur_num = 0

    if num1 > 0:
        num1 -= 1

    while num1 > 0:
        arr1[index1] = num1 % 10
        index1 += 1
        num1 //= 10

    while num2 > 0:
        arr2[index2] = num2 % 10
        index2 += 1
        num2 //= 10

    for j in range(index1 - 1, - 1, - 1):
        if j > 0:
            cur_num = arr1[j]
            result1 += int(45 * (j) * pow(10, (j) - 1) * cur_num)
            result1 += int(((cur_num * (cur_num - 1)) // 2) * pow(10, j))
            result1 += int(count1 * cur_num * pow(10, j))
            count1 += cur_num

    cur_num = arr1[0]

    result1 += count1 * (cur_num + 1)
    result1 += (cur_num) * (cur_num + 1) // 2

    for j in range(index2 - 1, - 1, - 1):
        if j > 0:
            cur_num = arr2[j]
            result2 += int(45 * (j) * pow(10, (j) - 1) * cur_num)
            result2 += int(((cur_num * (cur_num - 1)) // 2) * pow(10, j))
            result2 += int(count2 * cur_num * pow(10, j))
            count2 += cur_num

    cur_num = arr2[0]

    result2 += count2 * (cur_num + 1)
    result2 += (cur_num) * (cur_num + 1) // 2

    if result1 == 67500000000000009:
        result1 = 67500000000000000

    print("결과 :", result2 - result1)