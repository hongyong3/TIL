import sys
sys.stdin =open("종이붙이기_input.txt", "r")
T = int(input())
a = []
for test_case in range(T):
    N = int(input())
    print(T)

# def paper(a):
#     for i in a:
#         if i < 2:
#             return 1
#         else:
#             return paper(i-1) + 2 * paper(i-2)

# print("#{} {}".format(test_case, paper(a)))