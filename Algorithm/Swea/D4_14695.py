import sys
sys.stdin = open("D4_14695_input.txt", "r")

'''
평면의 방정식
Ax + By + Cz + D = 0
p1 = (x1, y1, z1)
p2 = (x2, y2, z2)
p3 = (x3, y3, z3)

A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
D = x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1)
'''

# 27 // 29
def v(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    A = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2)
    B = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2)
    C = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    D = - (x1 * (y2 * z3 - y3 * z2) + x2 * (y3 * z1 - y1 * z3) + x3 * (y1 * z2 - y2 * z1))
    return A, B, C, D


T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = "TAK"
    if N > 3:
        a, b, c, d = v(*arr[0], *arr[1], *arr[2])
        for x, y, z in arr:
            s = a * x + b * y + c * z
            t = a * x + b * y + c * z + d
            # if not s:
            if not (s == t == 0):
                ans = "NIE"
                break
    print("#{} {}".format(test_case + 1, ans))