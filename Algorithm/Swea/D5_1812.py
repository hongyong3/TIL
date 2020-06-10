import sys
sys.stdin = open("D5_1812_input.txt", "r")

T = int(input())
for test_case in range(5):
    N, M = map(int, input().split())
    data = sorted((list(map(int, input().split()))), reverse= True)
    ans = 0
    tile = []
    for i in data:
        tile.append(pow(2, i))
    