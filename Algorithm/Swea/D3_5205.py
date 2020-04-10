import sys
sys.stdin = open("D3_5205_input.txt", "r")

def quickSort(data):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = data[(low + high) // 2]

        while low <= high:
            while data[low] < pivot:
                low += 1
            while data[high] > pivot:
                high -= 1

            if low <= high:
                data[low], data[high] = data[high], data[low]
                low, high = low + 1, high - 1

        return low

    return sort(0, len(data) - 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    quickSort(data)
    print("#{} {}".format(test_case + 1, data[N // 2]))