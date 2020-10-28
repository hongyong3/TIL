import sys
sys.stdin = open("D3_10912_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = sorted(list(map(str, input())))
    while True:
        for i in range(len(data) - 1):
            if data[i] == data[i + 1]:
                data.pop(i)
                data.pop(i)
                break
        else:
            break

    if data:
        print("#{} {}".format(test_case + 1, ''.join(data)))
    else:
        print("#{} {}".format(test_case + 1, 'Good'))