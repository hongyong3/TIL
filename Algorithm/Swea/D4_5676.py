import sys
sys.stdin = open("D4_5676_input.txt", "r")

temporary = input()
T = ''
for t in temporary:
    if t.isdigit():
        T += t
# for test_case in range(int(T)):
for test_case in range(3):
    rectangle, line = ['', '', '', ''], ['', '', '', '']
    meet = 0

    temporary = input()
    k = 0
    for t in range(len(temporary)):
        if temporary[t] == '-':
            rectangle[k] = temporary[t]
        if temporary[t].isdigit():
            rectangle[k] += temporary[t]
            k += 1

    temporary = input()
    k = 0
    for t in range(len(temporary)):
        if temporary[t] == '-':
            line[k] = temporary[t]
        if temporary[t].isdigit():
            line[k] += temporary[t]
            k += 1

    xmin, ymin, xmax, ymax = int(rectangle[0]), int(rectangle[1]), int(rectangle[2]), int(rectangle[3])
    if xmin > xmax:
        xmin, ymin, xmax, ymax = xmax, ymax, xmin, ymin

    x1, y1, x2, y2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])

    if x1 > x2:
        x1, x2, y1, y2 = x2, y2, x1, y1

    if y1 == y2:  # y1 == y2
        if y2 < ymin or y1 > ymax:
            meet = 0
        elif ymin < y1 < y2 < ymax:
            if xmin < x1 < x2 < xmax:
                meet = 0
            if x1 <= xmin < x2 < xmax or xmin < x1 < xmax <= x2:
                meet = 1
            elif xmin <= x1 < x2 <= xmax or x1 <= xmin < xmax <= x2:
                meet = 2
        elif ymin == y1 or ymax == y1:
            if xmax < x1 or xmin > x2:
                meet = 0
            elif xmin == x2 or xmax == x1:
                meet = 1
            elif xmin < x1 < x2 < xmax or xmin <= x1 < x2 < xmax or xmin < x1 < x2 <= xmax or xmin <= x1 < x2 <= xmax:
                meet = 4

    elif x1 == x2:
        if x2 < xmin or x1 > xmax:
            meet = 0
        elif xmin < x1 < x2 < xmax:
            if ymin < y1 < y2 < ymax:
                meet = 0
            elif ymin <= y1 < y2 < ymax or ymin < y1 < y2 <= ymax or y1 < y2 <= ymin < ymax or ymin < ymax <= y1 < y2:
                meet = 1
            elif ymin <= y1 < y2 <= ymax or y1 <= ymin < ymax <= y2:
                meet = 2
        elif xmin == x1 or xmax == x2:
            if ymax < y1 or ymin > y2:
                meet = 0
            elif ymin == y2 or ymax == y1:
                meet = 1
            elif ymin < y1 < y2 < ymax or ymin <= y1 < y2 < ymax or ymin < y1 < y2 <= ymax or ymin <= y1 < y2 <= ymax:
                meet = 4

    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        pass
    print(meet)