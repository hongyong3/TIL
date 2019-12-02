def palindrome(M, data):
    ans = []
    while M > 0:
        inverse = []

        # 가로
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j:j+M-1] == data[i][j+M-1:j:-1]:
                    ans.append(data[i][j:j+M])


        # 세로
        for j in range(len(data)):
            inverse_str = ''
            for i in range(len(data)):
                inverse_str += data[i][j]
            inverse.append(''.join(inverse_str))

        for i in range(len(data)):
            for j in range(len(data)):
                if inverse[i][j:j+M-1] == inverse[i][j+M-1:j:-1]:
                    ans.append(inverse[i][j:j+M])
                    
        M -= 1
    answer = []
    for i in ans:
        answer.append(len(i))
    return max(answer)

import sys
sys.stdin =open("회문2_input.txt", "r")
for test_case in range(10):
    T = int(input())
    N, M = 100, 100
    data = [input() for _ in range(N)]
    print("#{} {}".format(test_case + 1, palindrome(M, data)))