arr = [-7, -3, -2, 5, 8]
n = len(arr)    # n : 원소의 갯수
count = 0

for i in range(1, 1 << n):  # 1<<n : 부분 집합의 갯수
    sum = 0
    for j in range(n):  # # 원소의 수만큼 비트를 비교
        if i & (1 << j):        # i의 j번째 비트가 1이면 j번째 원소 출력 10진수를 2진수로
            sum += arr[j]

    if sum == 0:
        count += 1
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end = " ")
        print()
print("갯수 : {}".format(count))


