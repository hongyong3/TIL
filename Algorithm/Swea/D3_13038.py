import sys
sys.stdin = open("D3_13038_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    data += data[:6]
    cnt, idx = 7, 0
    minAns = float('inf')
    while cnt:
        temp = data[idx : idx + 7]
        tempN = N
        ans = 0
        while tempN:
            for i in temp:
                ans += 1
                if i:
                    tempN -= 1
                    if tempN == 0:
                        break
        if minAns > ans:
            minAns = ans
        cnt -= 1
        idx += 1
    print("#{} {}".format(test_case + 1, minAns))