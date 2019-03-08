import sys
sys.stdin = open("스파이 조직_input.txt", "r")
N, S = list(input().split())
count = 0
num = ['1234567890']
number = []
print(number)
ad = []
for i in range(len(S)):
    # if S[i] in num:
    #     number.append(S[i])
    if S[i] == '<':
        count += 1
        # if
        # print(count)
