import sys
sys.stdin = open("D5_10727_input.txt", "r")
'''
업데이트 하고 해당셀이, 해당행, 해당열에서 가장 큰값이면 ans += 1
시간초과 조심하자 
'''

T = int(input())
for test_case in range(T):
    n, m, q = map(int, input().split())
    ans = 0
    data = [list(map(int, input().split())) for _ in range(n)]
    maxArr = [[0] * m for _ in range(n)]

    for i in range(n):
        gm = max(data[i])
        k = 0
        for j in range(m):
            maxArr[i][j] = gm

    pass
