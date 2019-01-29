def palindrome(N, M, data):
    ans = []
    while M > 0:

        # 가로
        for x in range(len(data)):
            for y in range(len(data)):
                if data[x][y:y+M-1] == data[x][y+M-1:y:-1]:
                    ans.append(data[x][y:y+M])



        # 세로
        inverse = []
        for y in range(len(data)):
            inverse_str = ''
            for x in range(len(data)):
                inverse_str += data[x][y]
            inverse.append("".join(inverse_str))

        for x in range(len(data)):
            for y in range(len(data)):
                if inverse[x][y : y+len(data)-1] == inverse[x][y+len(data)-1 : y : -1]:
                    ans.data.append(data[x][y: y + len(data) - 1])
        M -= 1
    answer = []
    for i in ans:
        answer.append(len(i))
    return max(answer)

import sys
sys.stdin =open("회문2_input.txt", "r")
for test_case in range(1, 11):
    T = int(input())
    N, M = 100, 100
    data = [input() for _ in range(N)]
    # print(data)
    print("#{} {}".format(test_case, palindrome(N, M, data)))