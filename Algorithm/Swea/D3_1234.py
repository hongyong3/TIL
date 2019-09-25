import sys
sys.stdin = open("D3_1234_input.txt", "r")

# def solve(data):
#     for i in range(len(data)):
#         if data[i] == data[i + 1]:
#             del data[i:i + 1]
#             solve(data)


for test_case in range(10):
    N, data = map(int, input().split())
    print(data)
    # solve(data)