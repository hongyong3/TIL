import sys
sys.stdin = open("토너먼트 카드게임_input.txt")

def tournament(data, x, y):
    a = data[x]
    b = data[y]

    if a == b:
        return x
    elif a == 1 and  b == 2:
        return y
    elif a == 1 and b == 3:
        return x

    elif a == 2 and b == 1:
        return x
    elif a == 2 and b == 3:
        return y

    elif a == 3 and b == 1:
        return y
    elif a == 3 and b == 2:
        return x

def game(data, start, end):
    if end-start >=1:
        middle = int((start+end) // 2)
        return tournament(data, game(data, start, middle), game(data, middle+1, end))
    elif start == end:
        return start

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print(f"#{test_case+1} {game(data, 0, N-1) + 1}")