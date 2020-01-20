import sys
sys.stdin = open("D4_1232_input.txt", "r")

# def inorder(n):
#     root = data[int(n)]
#     if len(root) == 2:
#         return root[1]
#     else:
#         ans = inorder(root[2])
#         ans = '(' + ans + ')' + root[1]
#         return ans + '(' + inorder(root[3]) + ')'
#
# for test_case in range(10):
#     N = int(input())
#     data = {}
#     for i in range(1, N + 1):
#         data[i] = input().split()
#     print(data)
#
#     print("#{} {}".format(test_case + 1, int(eval(inorder(1)))))

def inorder(n):
    root = data[int(n)]
    if len(root) == 2:
        return root[1]
    else:
        num1 = int(inorder(root[2]))
        num2 = int(inorder(root[3]))
        if root[1] == "+":
            return num1 + num2
        elif root[1] == '-':
            return num1 - num2
        elif root[1] == '*':
            return num1 * num2
        else:
            return num1 // num2

for test_case in range(10):
    N = int(input())
    data = {}
    for i in range(1, N + 1):
        data[i] = input().split()
    print("#{} {}".format(test_case + 1, inorder(1)))