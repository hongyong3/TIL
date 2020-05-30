import sys
sys.stdin = open("D5_1814_input.txt", "r")

def locationL(idx, val):
    if not locationLine:
        return 1
    # else:
        # for otherIdx, otherVal in locationLine:
            # if val < otherVal:
            #     return 1
            # elif val > otherVal:
            #     return - 1
            # else:
            #     if idx < otherIdx:
            #         return 1
            #     elif idx > otherIdx:
            #         return - 1
        # return 1
    return - 1

T = int(input())
for test_case in range(1):
    N = int(input())
    line = list(map(int, input().split()))
    row = list(map(int, input().split()))
    locationLine, locationRow = [], []

    for idx, val in enumerate(line):
        locationLine.append(locationL(idx, val))
    print(locationLine)