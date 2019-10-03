import sys
sys.stdin = open("D3_4579_input.txt", "r")

def isExist(data):
    global ans
    for i in range(int(len(data) / 2)):
        if data[i] == "*" or data[len(data) - 1 - i] == "*":
            return ans
        if data[i] != data[len(data) - 1 - i]:
            ans = "Not exist"
            return ans

T = int(input())
for test_case in range(T):
    data = str(input())
    ans = "Exist"
    isExist(data)
    print("#{} {}".format(test_case + 1, ans))