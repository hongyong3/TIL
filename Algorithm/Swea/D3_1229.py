import sys
sys.stdin = open("D3_1229_input.txt", "r")

def solve(update):
    for i in range(len(update)):
        if update[0] == "I":
            pass
        elif update[i] == "D":
            pass

for test_case in range(1):
    N = int(input())
    data = list(map(str, input().split()))
    M = int(input())
    update = list(map(str, input().split()))
    print(data)
    solve(update)