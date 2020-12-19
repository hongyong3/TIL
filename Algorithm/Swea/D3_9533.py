import sys
sys.stdin = open("D3_9533_input.txt", "r")

T = int(input())
for test_case in range(T):
    r, c, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]  # x1, y1 출발지 행, 열; x2, y2 도착지 행, 열; time 이동 시간; waiting 배차 간격;
    # x1, y1, x2, y2, time, waiting = map(int, input().split())