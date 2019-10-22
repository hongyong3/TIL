import sys
sys.stdin = open("D4_4672_input.txt", "r")

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


T = int(input())
for test_case in range(T):
    data = input()
    count = 0
    permute(data, 0)
    print("#{} {}".format(test_case + 1, count))