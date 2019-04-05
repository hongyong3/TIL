import sys
sys.stdin = open("연월일 달력_input.txt", "r")

for i in range (1, int(input())+1):
    d=input()
    a=d[4:6]
    b=d[6:]
    m=int(a)
    o=int(b)
    if m>12 or m*o<1 or o>int("303232332323"[m-1])+28:
        print(f'#{i} -1')
    else:
        print(f'#{i} {d[:4]}/{a}/{b}')