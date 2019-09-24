import sys
sys.stdin = open("D3_1221_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = str(input())
    data = list(map(str, input().split()))
    GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    GNS = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    for i in range(len(data)):
        # for j in range(len(GNS)):
        for key, value in GNS.items():
            if data[i] == GNS
            if data[i] == GNS[0]: data[i] = 0
            if data[i] == GNS[1]: data[i] = 1
            if data[i] == GNS[2]: data[i] = 2
            if data[i] == GNS[3]: data[i] = 3
            if data[i] == GNS[4]: data[i] = 4
            if data[i] == GNS[5]: data[i] = 5
            if data[i] == GNS[6]: data[i] = 6
            if data[i] == GNS[7]: data[i] = 7
            if data[i] == GNS[8]: data[i] = 8
            if data[i] == GNS[9]: data[i] = 9

    data = sorted(data)
    for i in range(len(data)):
        for j in range(len(GNS)):
            if data[i] == 0: data[i] = GNS[0]
            if data[i] == 1: data[i] = GNS[1]
            if data[i] == 2: data[i] = GNS[2]
            if data[i] == 3: data[i] = GNS[3]
            if data[i] == 4: data[i] = GNS[4]
            if data[i] == 5: data[i] = GNS[5]
            if data[i] == 6: data[i] = GNS[6]
            if data[i] == 7: data[i] = GNS[7]
            if data[i] == 8: data[i] = GNS[8]
            if data[i] == 9: data[i] = GNS[9]
    print("#{}".format(test_case + 1), *data)
