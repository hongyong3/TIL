import sys
sys.stdin = open("D4_5672_input.txt", "r")

temporary = input()
T = ''
for t in temporary:
    if t.isdigit():
        T += t
for test_case in range(int(T)):
    temporary = input()
    N = ''
    for t in temporary:
        if t.isdigit():
            N += t
    data = [input()[0] for _ in range(int(N))]
    newData = ''

    f, l = 0, - 1
    while data:
        if ord(data[f]) < ord(data[l]):
            newData += data.pop(0)
            f, l = 0, - 1
        elif ord(data[f]) > ord(data[l]):
            newData += data.pop(- 1)
            f, l = 0, - 1
        elif ord(data[f]) == ord(data[l]):
            f += 1
            l -= 1
        if len(data) == 1:
            newData += data.pop()
    print("#{} {}".format(test_case + 1, newData))