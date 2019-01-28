import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for test_case in range(T):

    temp = input()  #dummy
    data = list(map(str, input().split()))
    count = [0] * 10
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', "NIN"]

    for i in data:
        if i == 'ZRO':
            count[0] += 1
        elif i == 'ONE':
            count[1] += 1
        elif i == 'TWO':
            count[2] += 1
        elif i == 'THR':
            count[3] += 1
        elif i == 'FOR':
            count[4] += 1
        elif i == 'FIV':
            count[5] += 1
        elif i == 'SIX':
            count[6] += 1
        elif i == 'SVN':
            count[7] += 1
        elif i == 'EGT':
            count[8] += 1
        else:
            count[9] += 1


    print(f'#{test_case+1}')
    for i in range(len(count)):
        ans = count[i]
        while ans > 0:
            print(num[i], end=" ")
            ans -=1