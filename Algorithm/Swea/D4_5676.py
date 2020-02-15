import sys
sys.stdin = open("D4_5676_input.txt", "r")

def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    global meet, ans
    tm = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
    td = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    sm = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
    sd = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)


    if td != 0 and sd != 0:
        if 0 < tm // td < 1 and 0 < sm // sd < 1:
            t, s = tm // td, sm // sd
            x = x1 + s * (x2 - x1)
            y = y1 + s * (y2 - y1)
            if [x, y] not in ans:
                ans.append([x, y])
    if tm == td == sm == sd == 0:
        meet = 4

T = int(input().replace('혻', ''))
for test_case in range(T):
    xmin, ymin, xmax, ymax = map(int, input().replace('혻', '').split())
    x1, y1, x2, y2 = map(int, input().replace('혻', '').split())

    meet = 0
    ans = []
    rectangleLine = [[xmin, ymin, xmax, ymin], [xmin, ymin, xmin, ymax], [xmin, ymax, xmax, ymax], [xmax, ymin, xmax, ymax]]

    for i in rectangleLine:
        intersection(x1, y1, x2, y2, i[0], i[1], i[2], i[3])
    print("#{} {}".format(test_case + 1, meet))