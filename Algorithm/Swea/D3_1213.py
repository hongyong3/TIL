import sys
sys.stdin = open("D3_1213_input.txt", "r")

# 방법 1
for test_case in range(1):
    N = int(input())
    str1 = str(input())
    data = str(input())
    count = 0
    for i  in range(len(data) - len(str1) + 1):
        if data[i:i + len(str1)] == str1:
            count += 1
    print("#{} {}".format(test_case + 1, count))

# 방법2
# for test_case in range(10):
#     N = int(input())
#     str1 = str(input())
#     data = str(input())
#     print("#{} {}".format(test_case + 1, data.count(str1)))

# 방법3
# for test_case in range(10):
#     N = int(input())
#     a = str(input())
#     print("#{} {}".format(test_case + 1, str(input()).count(a)))