import sys
sys.stdin =open("Magnetic_input.txt", "r")
for test_case in range(10):
    data = int(input())
    table = [list(map(int, input().split())) for _ in range(data)]
    count = 0
    for i in range(100):
        ans = []
        for j in range(100):
            if table[j][i] == 1:
                ans.append(table[j][i])
            if table[j][i] == 2:
                if 1 in ans:
                    count += 1
                    ans = []

    print(f'#{test_case} {count}')
