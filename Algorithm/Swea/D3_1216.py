import sys
sys.stdin = open("D3_1216_input.txt", "r")

def palindrome(M, data):
    ans = []
    while M > 0:
        inverse_ans = []

        # 가로
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j:j + M - 1] == data[i][j + M - 1:j:-1]:
                    ans.append(data[i][j:j + M])

        # 세로
        for j in range(len(data)):
            inverse_str = ''
            for i in range(len(data)):
                inverse_str += data[i][j]
            inverse_ans.append(''.join(inverse_str))

        for i in range(len(data)):
            for j in range(len(data)):
                if inverse_ans[i][j:j + M - 1] == inverse_ans[i][j + M - 1:j:-1]:
                    ans.append(inverse_ans[i][j:j + M])

        M -= 1
    answer = []
    for i in ans:
        answer.append(len(i))
    return max(answer)

for test_case in range(10):
    N = int(input())
    data = [input() for _ in range(100)]
    print("#{} {}".format(test_case + 1, palindrome(100, data)))