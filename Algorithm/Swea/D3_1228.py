import sys
sys.stdin = open("D3_1228_input.txt", "r")

for test_case in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    change_N = int(input())
    change_data = list([j.replace("\r", "").split(" ") for j in input().split("I ")[1:]])

    for k in range(change_N):
        x = int(change_data[k][0])
        # y = int(change_data[k][1])  # not need
        s = change_data[k][2:-1]
        data = data[:x] + s + data[x:]

    print("#{} {}".format(test_case + 1, " ".join(map(str, data[:10]))))