import sys
sys.stdin = open("D5_13550_input.txt", "r")

# 2808 / 1799854 Runtime Error
T = int(input())
for test_case in range(3):
    a, d, n = map(int, input().split())
    if n % 2:
        a1 = a
        an = a + (n - 1) * d
        am = (a1 + an) // 2
        m = am
        for i in range(n // 2, 0, - 1):
            am *= (m + i * d) * (m - i * d)
            am %= 1000003
    else:
        a2 = a + d
        an = a + (n - 1) * d
        am = (a2 + an) // 2
        m = am
        for i in range(n // 2 - 1, 0, - 1):
            am *= (m + i * d) * (m - i * d)
            am %= 1000003
        am *= a
        am %= 1000003
    print("#{} {}".format(test_case + 1, am))