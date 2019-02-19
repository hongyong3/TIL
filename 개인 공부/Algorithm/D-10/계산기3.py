def Forth(data):
    for i in range(len(data)):
        if data[i] == 52:






import sys
sys.stdin = open("계산기3_input.txt", "r")

T = int(input())
print(T)
for test_case in range(T):
    data = input()
    operators = {'+' : 50, '*' : 51, '(' : 52}
    stack = []
    # print(f'#{test_case+1} {}')
