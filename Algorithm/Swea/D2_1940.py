import sys
sys.stdin = open("D2_1940_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)


0 0 0
2 2 2
3 3 5
3 3 8
5 5 13
4 4 17
5 5 22
5 5 27

    # 4 27