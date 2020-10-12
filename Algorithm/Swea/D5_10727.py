import sys
sys.stdin = open("D5_10727_input.txt", "r")
'''
업데이트 하고 해당셀이, 해당행, 해당열에서 가장 큰값이면 ans += 1
시간초과 조심하자 
'''

# 20 / 29 runtime error
T = int(input())
for test_case in range(T):
    N, M, Q = map(int, input().split())
    ans = 0
    data = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(Q):
        r, c, x = map(int, input().split())
        data[r - 1][c - 1] = x
        # 여기에서 가지치기 필요?
        for i in range(N):
            chk = True
            idx = data[i].index(max(data[i]))
            temp = data[i][idx]
            for j in range(N):
                if temp < data[j][idx]:
                    chk = False
                    break
            if chk:
                ans += 1
    print("#{} {}".format(test_case + 1, ans))