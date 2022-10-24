import sys
sys.stdin = open("D3_15612_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = []
    ans = "yes"
    num = 0
    chk = [0] * 8
    for _ in range(8):
        data = list(input())
        arr.append(data)
        num += data.count('O')
    if num != 8:
        ans = "no"
    else:
        arrT = list(zip(*arr))
        for i in range(8):
            if 'O' in arr[i]:
                chk[i] += 1
            for j in range(8):
                if arrT[i][j] == 'O':
                    chk[i] += 1
        for i in chk:
            if i != 2:
                ans = "no"
                break
    print("#{} {}".format(test_case + 1, ans))