import sys
sys.stdin = open("5648_input.txt", "r")


dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]  # 상 하 좌 우

T = int(input())
for test_case in range(1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * 20 for _ in range(20)]         # 테스트
    # arr = [[0] * 2000 for _ in range(2000)]   # 실제
    for i in range(len(atom)):
        arr[atom[i][1] + 9][atom[i][0] + 9] = atom[i][3]      # 테스트
        # arr[atom[i][1] + 999][atom[i][0] + 999] = atom[i][3]  # 실제
    for i in arr:
        print(i)
    # print(map)