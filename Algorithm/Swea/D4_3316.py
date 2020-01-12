import sys
sys.stdin = open("D4_3316_input.txt", "r")

people = {"A" : 3, "B" : 2, "C" : 1, "D" : 0}

T = int(input())
for test_case in range(T):
    S = input()
    caseList = [[] for _ in range(len(S))]
    ans = 0

    if S[0] == "A":
        for i in range(1, 16):
            if i & (1 << 3):
                caseList[0].append([i, 1])
    else:
        for i in range(1, 16):
            if i & (1 << 3) and i & (1 << people[S[0]]):
                caseList[0].append([i, 1])

    for i in range(1, len(S)):
        temp = []
        for j in range(1, 16):
            if j & (1 << people[S[i]]):
                temp.append([j, 0])

        for x in caseList[i - 1]:
            for y in temp:
                if x[0] & y[0]:
                    y[1] = (x[1] + y[1]) % 1000000007

        caseList[i] = temp[:]


    for i in caseList[- 1]:
        ans += i[1]
        ans %= 1000000007

    print("#{} {}".format(test_case + 1, ans))