import sys
sys.stdin = open("암호코드 스캔_input.txt", "r")
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [[0 for _ in range(M+4)] for _ in range(M)]
    for i in range(N):
        temp = input()


def solve():
    reset = 0
    for i in range(N):
        j = M * 4 - 1 :
        while j > 0:
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                code = [0 for _ in range(8)]
                for k in range(7, -1, -1):
                    x = y = z = 0
                    while arr[i][j] == 1:
                        z += 1
                        j -= 1
                    while arr[i][j] == 0:
                        y += 1
                        j -= 1
                    while arr[i][j] == 1:
                        x += 1
                        j -= 1
                    while arr[i][j] == 0:
                        j -= 1

                    d = min(x, y, z)
                    x //= d
                    y //= d
                    z //= d

                    code[k] = scode[x][y][z]

                t = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
                if t % 10 == 0:
                    reset += code[0] + code[2] + code[4] + code[6] + code[1] + code[3] + code[7]
                j += 1

