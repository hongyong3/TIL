import sys
sys.stdin = open("D3_4223_input.txt", "r")

'''
samsung
    a : 1
    g : 1
    m : 1
    n : 1
    s : 2
    u : 1
'''
a = dict()
s = 'SAMSUNG'
for i in s:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
print(a)

T = int(input())
for test_case in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        L = int(input())
        nam = input().split()
        score = int(input())
        print(L, nam, score)