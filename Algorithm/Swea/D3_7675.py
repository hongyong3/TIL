import sys
sys.stdin = open("D3_7675_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = input().replace('!',' !').replace('.',' .').replace('?',' ?').split()
    count = 0
    res = ''
    for i in data:
        if i.isalpha() and i == i.capitalize():
            count += 1
        if i == '.' or i == '!' or i == '?':
            res += str(count) + ' '
            count = 0
    print("#{} {}".format(test_case + 1, res))