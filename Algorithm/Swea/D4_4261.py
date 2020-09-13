import sys
sys.stdin = open("D4_4261_input.txt", "r")

keypad = [[0], [0], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
T = int(input())
for test_case in range(T):
    S, N = map(str, input().split())
    data = list(map(str, input().split()))
    mat, j = 0, 0
    for i in range(int(N)):
        check = 1
        for k in data[i]:
            if k not in keypad[int(S[j])]:
                check = 0
                break
            else: j += 1
        if check: mat += 1
        j = 0
    print("#{} {}".format(test_case + 1, mat))


# def s(l,a,c=0):
#     for i in l:
#         if len(i)!=len(a):continue
#         for j in range(len(a)):
#             if a[j]!=str((ord(i[j])-1)//3-30-(1 if i[j] in "svyz" else 0)):break
#         else:c+=1
#     return c
# for i in range(int(input())):a=input().split()[0];print("#%d %d"%(i+1,s(input().split(),a)))