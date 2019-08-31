import sys
sys.stdin = open("5648_input.txt", "r")


T = int(input())
for test_case in range(T):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    atoms, ans, count = {}, 0, 0

    for i in range(len(atom)):
        atoms[(atom[i][0] * 2, atom[i][1] * 2)] = [[atom[i][2]], [atom[i][3]]]  # 0.5초이므로 * 2
    while count < 4000 and len(atom) > 1:
        dy = [1, -1, 0, 0]  # 상 하 좌 우
        dx = [0, 0, -1, 1]  # 상 하 좌 우
        new = {}
        for i in atoms.keys():
            if atoms[i] == 0:
                continue
            x = i[0]
            y = i[1]
            dir = atoms[i][0][0]
            energy = atoms[i][1][0]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < -2005 or ny < -2005 or nx > 2005 or ny > 2005: continue
            if (nx, ny) in new:
                new[(nx, ny)][0].append(dir)
                new[(nx, ny)][1].append(energy)
            else:
                new[(nx, ny)] = [[dir], [energy]]

        for i in new.keys():
            if len(new[i][1]) > 1:
                ans += sum(new[i][1])
                new[i] = 0
        atoms = new
        count += 1
    print("#{} {}".format(test_case + 1, ans))