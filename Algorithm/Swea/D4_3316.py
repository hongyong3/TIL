import sys
sys.stdin = open("D4_3316_input.txt", "r")

people = {"A" : 3, "B" : 2, "C" : 1, "D" : 0}

T = int(input())
for test_case in range(T):
    S = input()
    case = [[] for _ in range(len(S))]
    answer = 0

    # 첫 번째 책임자
    if S[0] == "A": # 책임자가 A인 경우
        for i in range(1, 16):
            if i & (1 << 3):
                case[0].append([i, 1])  # A(8), AD(9), AC(10), ACD(11), AB(12), ABD(13), ABC(14), ABCD(15) => 8

    else:   # 책임자가 A가 아닌 경우
        for i in range(1, 16):
            if i & (1 << 3) and i & (1 << people[S[0]]):
                case[0].append([i, 1])  # AB(12), ABD(13), ABC(14), ABCD(15) => 4

    # 두 번째부터 책임자
    for i in range(1, len(S)):
        temporary = []
        for j in range(1, 16):
            if j & (1 << people[S[i]]):
                temporary.append([j, 0])

        for x in case[i - 1]:
            for y in temporary:
                if x[0] & y[0]:
                    y[1] = (x[1] + y[1]) % 1000000007

        case[i] = temporary[:]

    for i in case[- 1]:
        answer += i[1]
        answer %= 1000000007

    print("#{} {}".format(test_case + 1, answer))