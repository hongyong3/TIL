import sys
sys.stdin = open("ladder_input.txt", "r")

for test_case in range(10):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for y in range(100):
        if data[99][y] == 2:
            ans = y
    for x in range(1, 100):
        if ans-1 >= 0 and data[99-x][ans-1] == 1:
            data[99-x][ans] == 0
            ans = ans - 1
            while ans > 0 and data[99-x][ans-1] == 1:
                data[99-x][ans] == 0
                ans = ans - 1

        elif ans+1 <= 99 and data[99-x][ans+1] == 1:
            data[99-x][ans] == 0
            ans = ans + 1
            while ans < 99 and data[99-x][ans+1] == 1:
                data[99-x][ans] == 0
                ans = ans + 1
    print(f"#{T} {ans}")