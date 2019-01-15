#max와 min을 구하는 문제
import sys
sys.stdin = open("Flatten_input.txt")

T = 10
for test_case in range(T):
    dump = 0
    N = int(input())
    dump = list(map(int, input().split()))
    count = 0

    for i in range(len(dump) - 1, 0, -1):
        for j in range(0, i):
            if dump[j] > dump[j + 1]:
                dump[j], dump[j + 1] = dump[j + 1], dump[j]

    while N > 0:
        dump[0] = dump[0]+1
        dump[-1] = dump[-1]-1

        for i in range(len(dump) - 1, 0, -1):
            for j in range(0, i):
                if dump[j] > dump[j + 1]:
                    dump[j], dump[j + 1] = dump[j + 1], dump[j]
        N -= 1
        count = dump[-1] - dump[0]
    print("#{} {}".format(test_case, count))
