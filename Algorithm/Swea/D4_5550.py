import sys
sys.stdin = open("D4_5550_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = str(input())
    croak = [0, 0, 0, 0, 0]  # 'c', 'r', 'o', 'a', 'k'
    flag, count = True, 0

    for i in range(len(data)):
        if data[i] == 'c':
            croak[0] += 1
            continue
        if data[i] == 'r':
            croak[1] += 1
            croak[0] -= 1
            if croak[0] < 0:
                flag = False
                break
            continue
        if data[i] == 'o':
            croak[2] += 1
            croak[1] -= 1
            if croak[1] < 0:
                flag = False
                break
            continue
        if data[i] == 'a':
            croak[3] += 1
            croak[2] -= 1
            if croak[2] < 0:
                flag = False
                break
            continue
        if data[i] == 'k':
            croak[3] -= 1
            if croak[3] < 0:
                flag = False
                break
        count = max(count, croak[0] + croak[1] + croak[2] + croak[3])
    if croak[0] != 0 or croak[1] != 0 or croak[2] != 0 or croak[3] != 0:
        flag = False
    if flag:
        print("#{} {}".format(test_case + 1, count + 1))
    else:
        print("#{} {}".format(test_case + 1, -1))