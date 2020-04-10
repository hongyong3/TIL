import sys
sys.stdin = open("D3_5204_input.txt", "r")

def solve(data):
    global count

    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        if sorted(left)[- 1] > sorted(right)[- 1]:
            count += 1
        solve(left)
        solve(right)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    count = 0
    solve(data)
    print("#{} {} {}".format(test_case + 1, sorted(data)[N // 2], count))