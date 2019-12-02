def palindrome(N, M, data):
    if N == M:
        for x in range(N):
            for y in range(M):
                # 가로
                if data[x][y] == data[x][-1 -y]:
                    if y == ( N / 2 ):
                        return data[x]
                    continue
                else:
                    break
        # 세로
        inverse = []
        for y in range(M):
            inverse_str = ''
            for x in range(N):
                inverse_str += data[x][y]
            inverse.append("".join(inverse_str))
        for x in range(N):
            for y in range(M):
                if inverse[x][y] == inverse[x][-1 - y]:
                    if y == ( N / 2 ):
                        return inverse[x]
                    continue
                else:
                    break

    else:
        for x in range(len(data)):
            for y in range(len(data)):
                if data[x][y:y + M - 1] == data[x][y + M - 1:y:-1]:
                    return data[x][y:y + M - 1]

import sys
sys.stdin =open("회문_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    print("#{} {}".format(test_case, palindrome(N, M, data)))

