import sys
sys.stdin = open("D4_4050_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(map(int, input().split())))
    arr = [[] for _ in range((len(data) // 3 + 1))]
    ans = 0
    for i in range(len(data)):
        j = 0
        while len(data) > 0:
            arr[j].append(data.pop(-1))
            if len(arr[j]) == 3:
                j += 1
    for j in range(len(arr)):
        ans += sum(arr[j][:2])
    print("#{} {}".format(test_case + 1, ans))