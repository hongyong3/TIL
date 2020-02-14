import sys
sys.stdin = open("D4_5672_input.txt", "r")

temporary = input()
T = ''
for t in temporary:
    if t.isdigit():
        T = int(t)
for test_case in range(T):
    temporary = input()
    newData = ''
    N = ''
    for t in temporary:
        if t.isdigit():
            N = int(t)
    data = [input()[0] for _ in range(N)]

    start, end = 0, N - 1
    while start != end:
        if ord(data[start]) < ord(data[end]):
            newData += data[start]
            start += 1
        elif ord(data[start]) > ord(data[end]):
            newData += data[end]
            end -= 1

        elif ord(data[start]) == ord(data[end]):
            nstart, nend = start + 1, end - 1
            same = False

            while True:
                if data[nstart] != data[nend]:
                    break
                else:
                    if nstart + 1 <= nend - 1:
                        nstart += 1
                        nend -= 1
                    else:
                        same = True
                        break

            if same:
                newData += data[start]
                start += 1

            else:
                if ord(data[nstart]) < ord(data[nend]):
                    newData += data[start]
                    start += 1
                else:
                    newData += data[end]
                    end -= 1

        if start == end:
            newData += data[start]

    print("#{} {}".format(test_case + 1, newData))