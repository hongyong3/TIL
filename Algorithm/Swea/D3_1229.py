import sys
sys.stdin = open("D3_1229_input.txt", "r")

for test_case in range(10):
    N = int(input())
    data = list(map(str, input().split()))
    C = int(input())
    cmd = list(map(str, input().split()))
    while len(cmd) > 0:
        if cmd[0] == "I":
            data[int(cmd[1]):int(cmd[1])] += cmd[3:int(cmd[2]) + 3]
            del cmd[:int(cmd[2]) + 3]
            continue
        if cmd[0] == "D":
            del data[int(cmd[1]):int(cmd[1]) + int(cmd[2])]
            del cmd[:3]
    print("#{}".format(test_case + 1), *data[:10])