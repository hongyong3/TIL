import sys
sys.stdin = open("D4_1824_input.txt", "r")

import collections

dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def solve(x, y, memory, dir):
    global mat
    if ans == "YES":
        return

    while True:
        cmd = data[x][y]
        if memory not in visited[(x, y, dir)]:
            visited[(x, y, dir)].add(memory)
        else:
            return

        if cmd == "?" and any(visited[(x, y, dir2)] for dir2 in range(4) if dir2 != dir):
            return

        if cmd in "^v<>":
            dir = "^v<>".index(cmd)

        elif cmd in "_|":
            if cmd == "_":
                if not memory:
                    dir = 3
                else:
                    dir = 2
            else:
                if not memory:
                    dir = 1
                else:
                    dir = 0

        elif cmd in "0123456789":
            memory = int(cmd)

        elif cmd in "+-":
            if cmd == "+":
                memory = (memory + 1) % 16
            else:
                memory = (memory - 1) % 16

        elif cmd == ".":
            pass

        elif cmd == "@":
            ans = "YES"
            return

        else:
            for i in range(4):
                solve((x + dx[i]) % R, (y + dy[i]) % C, memory, i)
            return

        x = (x + dx[dir]) % R
        y = (y + dy[dir]) % C

T = int(input())
for test_case in range(T):
    R, C = map(int, input().split())
    data = list(input() for _ in range(R))
    visited = collections.defaultdict(set)
    mat = "NO"
    solve(0, 0, 0, 3)
    print("#{} {}".format(test_case + 1, mat))