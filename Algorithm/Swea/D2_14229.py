import sys
sys.stdin = open("D2_14229_input.txt", "r")

arr = sorted(list(map(int, input().split())))
print(arr[500000])
    