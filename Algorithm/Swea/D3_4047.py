import sys
sys.stdin = open("D3_4047_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = str(input())
    count, mat = [13, 13, 13, 13], []
    x, y = 0, 0

    while y < len(data):
        y += 3
        mat.append(data[x:y])
        x = y
    if len(mat) != len(list(set(mat))):
        print("#{} {}".format(test_case + 1, "ERROR"))
        continue
    else:
        for k in mat:
            if k[0] == 'S': count[0] -= 1
            if k[0] == 'D': count[1] -= 1
            if k[0] == 'H': count[2] -= 1
            if k[0] == 'C': count[3] -= 1
    print("#{} ".format(test_case + 1), end="")
    print(*count)