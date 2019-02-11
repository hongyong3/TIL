import sys
sys.stdin = open("ladder_input.txt", "r")

def ladder(99, X, data):
    while X > 0:







for test_case in range(10):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    X = 0
    # print(data)
    for j in range(100):
        if data[99][j] == 2:
            X = j
    print(X)


    # print("#{} {}".format(test_case, ladder(99, X, data)))