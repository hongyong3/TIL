import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for test_case in range(T):
    temp = input()  #dummy
    data = list(map(str, input().split()))
    count = [0] * 10
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', "NIN"]

    for i in data:
        for j in range(len(num)):
            for k in range(len(count)):
                if i == num[j]:
                    count[k] +=1
        # ans =count[k]*num[j]
    print(count)
    # print(count)