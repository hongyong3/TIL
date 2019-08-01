import sys
sys.stdin = open("D2_1974_input.txt", "r")

def solve(data):
    # horizon
    for i in range(9):
        if len(set(data[i])) != 9:
            return 0

        # vertical
        temp = set()
        for j in range(9):
            temp.add(data[j][i])
        if len(temp) != 9:
            return 0

    array = [set(),set(),set()]
    index = 0

    # 9개 구역 검사
    for k in range(0, 81):
        x = k // 9
        y = k % 9

        # 3개 구역씩 확인 후 비우기
        if k != 0 and k % 27 == 0:
            if len(array[0]) != 9 and len(array[1]) != 9 and len(array) != 9:
                return 0

        # 3개씩 나눠담기
        if k != 0 and k % 3 == 0:
            if index == 2:
                index = -1
            index += 1

        array[index].add(data[x][y])
    return 1

T = int(input())
for test_case in range(T):
    data = [list(map(int, input().split())) for _ in range(9)]
    print("#{} {}".format(test_case + 1, solve(data)))
