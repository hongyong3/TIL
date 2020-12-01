import sys
sys.stdin = open("D4_8501_input.txt", "r")

arr = [0] * 1001
arr[2] = 1
z = 1
for i in range(3, 1001):
    z *= (i - 1)
    arr[i] = (i * arr[i - 1] + (i // 2) * z) % 1000000007
    print(arr[i])
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     print("#{} {}".format(test_case + 1, arr[N]))