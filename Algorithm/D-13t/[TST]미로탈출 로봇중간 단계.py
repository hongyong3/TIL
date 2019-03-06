import sys
sys.stdin = open("미로탈출 로봇중간 단계_input.txt", "r")
N = int(input())
data = [[1]*(N+2) for _ in range(N+2)]  # 가장자리 1로 채움
for i in range(1, N+1): # 1행 1열부터 입력받기
    data[i] = [1] + list(map(int, input())) + [1]
Darr = list(map(int, input().split()))
Dno = 0 # 방향순서
dr = [0, 1, 0, -1, 0] # 아래1, 왼2, 위3, 오른4 방향
dc = [0, 0, -1, 0, 1]
r, c = 1, 1 # 현재좌표
count = 0
while True:
    # 좌표계산
    r = r + dr[Darr[Dno]]
    c = c + dc[Darr[Dno]]
    if data[r][c] == 0: # 0이면
        data[r][c] = 9
        count += 1
        # 방문표시하고 카운트
    elif data[r][c] == 1:
        r = r - dr[Darr[Dno]]
        c = c - dc[Darr[Dno]]
        Dno = (Dno + 1) % 4

        # 이전좌표로 이동하고 방향전환(단 방향은 로테이션)
    else:
        break   # 지나간 자리이면 탈출
print(count)