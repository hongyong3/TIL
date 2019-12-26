import sys
sys.stdin = open("D4_1808_input.txt", "r")

def solve(num, count):
    global answer
    if num == 0:
        return
    # checkList = check(num, 0)
    if check(num, 0)[0]:
        result = check(num, 0)[1] + count + 1
        if answer == - 1 or answer > result:
            answer = result
        return
    for x, y in subAnswer:
        if x != (0 or 1) and num % x == 0:
            solve(num // x, count + y + 1)
    return

def check(num, length):
    while num > 0:
        if data[num % 10] != 1:
            return (0, 0)
        length += 1
        num //= 10
    return (1, length)

T = int(input())
for test_case in range(T):
    data = list(map(int, input().split()))
    N = int(input())
    subAnswer = set()
    answer = - 1
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0 and check(i, 0)[0]:
            subAnswer.add((i, check(i, 0)[1]))

    solve(N, 0)
    print("#{} {}".format(test_case + 1, answer))