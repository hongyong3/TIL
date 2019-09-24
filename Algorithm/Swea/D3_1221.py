import sys
sys.stdin = open("D3_1221_input.txt", "r")

# 방법1 list
# T = int(input())
# GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for test_case in range(T):
#     N = str(input())
#     data = list(map(str, input().split()))
#     for i in range(len(data)):
#         for j in range(len(GNS)):
#             if data[i] == GNS
#             if data[i] == GNS[0]: data[i] = 0
#             if data[i] == GNS[1]: data[i] = 1
#             if data[i] == GNS[2]: data[i] = 2
#             if data[i] == GNS[3]: data[i] = 3
#             if data[i] == GNS[4]: data[i] = 4
#             if data[i] == GNS[5]: data[i] = 5
#             if data[i] == GNS[6]: data[i] = 6
#             if data[i] == GNS[7]: data[i] = 7
#             if data[i] == GNS[8]: data[i] = 8
#             if data[i] == GNS[9]: data[i] = 9
#
#     data = sorted(data)
#     for i in range(len(data)):
#         for j in range(len(GNS)):
#             if data[i] == 0: data[i] = GNS[0]
#             if data[i] == 1: data[i] = GNS[1]
#             if data[i] == 2: data[i] = GNS[2]
#             if data[i] == 3: data[i] = GNS[3]
#             if data[i] == 4: data[i] = GNS[4]
#             if data[i] == 5: data[i] = GNS[5]
#             if data[i] == 6: data[i] = GNS[6]
#             if data[i] == 7: data[i] = GNS[7]
#             if data[i] == 8: data[i] = GNS[8]
#             if data[i] == 9: data[i] = GNS[9]
#     print("#{}".format(test_case + 1), *data)

# 방법2 dictionary
dict_GNS1 = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
dict_GNS2 = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
T = int(input())
for test_case in range(T):
    N = list(map(str, input().split()))
    data = list(map(str, input().split()))
    for i in range(len(data)):
        data[i] = dict_GNS1[data[i]]
    data.sort()
    for j in range(len(data)):
        data[j] = dict_GNS2[data[j]]
    print("#{}".format(test_case + 1), *data)