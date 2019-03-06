import sys
sys.stdin = open("파리 퇴치_input.txt", "r")

T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    data = [[0 for _ in range(M)] for _ in range(M)]    # 0인 M * M 행렬 가져오기
    for i in range(M):
        data[i] = list(map(int, input().split()))       # 행렬에 data 집어 넣기

        max = 0             # 최대값
        # min = 12012901      # 최소값
        for i in range(M-N+1):
            for j in range(M-N+1):
                sum = 0
                for x in range(N):
                    for y in range(N):
                        sum += data[i+x][j+y]
                        if max < sum:   # 최대값 구하기
                            max = sum
                        # if min > sum:   # 최소값 구하기
                        #     min = sum
    print(f"#{test_case+1} {max}")    # 최대값
    # print(f"#{test_case+1} {min}")    # 최소값


# 함수를 정의해서 구하기

# def get_sum(i, j):
#     global M
#     sum = 0
#     for x in range(M):
#         for x in range(M):
#             sum += data[i+x][j+y]
#     return sum