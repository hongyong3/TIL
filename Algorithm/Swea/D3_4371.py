# 1
import sys
sys.stdin = open("D3_4371_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    data.pop(0)
    count = 0

    for i in range(len(data)):
        if data[i] < 0:
            continue
        ans1 = data[i] - 1
        for j in range(i + 1, len(data)):
            if data[j] < 0:
                continue
            ans2 = data[j] - 1
            if ans2 // ans1 == ans2 / ans1:
                data[j] = -1
    for i in range(len(data)):
        if data[i] > 0:
            count += 1
    print("#{} {}".format(test_case + 1, count))

###############################################################################

# 2
import sys
sys.stdin = open("D3_4371_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    count = 0

    for i in range(1, N):
        if data[i] < 0:
            continue
        ans1 = data[i] - 1
        for j in range(i + 1, N):
            if data[j] < 0:
                continue
            ans2 = data[j] - 1
            if ans2 // ans1 == ans2 / ans1:
                data[j] = -1
    for i in range(1, N):
        if data[i] > 0:
            count += 1
    print("#{} {}".format(test_case + 1, count))

###############################################################################

# 3
import sys
sys.stdin = open("D3_4371_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    count = 0
    for i in range(1, N):
        if data[i] < 0: continue
        ans1 = data[i] - 1
        for j in range(i+1, N):
            if data[j] < 0: continue
            ans2 = data[j] - 1
            if ans2 % ans1 == 0: data[j] = - 1
    for i in range(1, N):
        if data[i] > 0: count += 1
    print("#{} {}".format(test_case + 1, count))