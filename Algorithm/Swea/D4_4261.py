import sys
sys.stdin = open("D4_4261_input.txt", "r")


keypad = {{"2": "a", "b", "c"}, ['3': 'd', 'e', 'f'], {'4': "g", "h", "i"}, {'5': "j", "k", "l"}, {"6": "m", "n", "o"}, {"7":`p`}, {}, {}}
T = int(input())
for test_case in range(T):
    S, N = map(int, input().split())
    data = list(map(str, input().split()))
