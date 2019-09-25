import sys
sys.stdin = open("D3_1234_input.txt", "r")
for test_case in range(10):
    N, data = map(str, input().split())
    while True:
        ans = data
        data = data.replace("00", "").replace("11", "").replace("22", "").replace("33", "").replace("44", "").replace("55", "").replace("66", "").replace("77", "").replace("88", "").replace("99", "")
        if ans == data: break
    print("#{} {}".format(test_case + 1, data))