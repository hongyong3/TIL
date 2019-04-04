import sys
sys.stdin = open("[TST]로봇_input.txt", "r")

def BFS():
    dr = [0, 0, 0, 1, -1]   # 동 서 남 북 1234
    dc = [0, 1, -1, 0, 0]
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)]
    que = []
    # 1] 시작점을 큐에 저장 (방문표시)

    while que:
        # 2] 큐에서 데이터 읽기
        for i in range(1, 4):   # go 1, 2, 3

        for j in range(2):  # Turn Left, Right



R, C = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(C)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sol = BFS()
print(sol)