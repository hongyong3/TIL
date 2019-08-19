import sys
sys.stdin = open("D3_5515_input.txt", "r")

T = int(input())
for test_case in range(T):
    m, d = map(int, input().split())
    daysOfMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = 0
    for i in range(m):
        days += daysOfMonth[i]
    weekday = (days + d + 3) % 7
    print("#{} {}".format(test_case + 1, weekday))