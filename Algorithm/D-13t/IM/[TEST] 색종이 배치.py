import sys
sys.stdin = open('색종이 배치_input.txt', 'r')

data = [[0 for _ in range(101)] for _ in range(101)]
Nx, Ny, Nl, No = map(int, input().split())
Mx, My, Ml, Mo = map(int, input().split())

x = set(range(Nx, Nx+Nl+1)) & set(range(Mx, Mx+Ml+1))
y = set(range(Ny, Ny+No+1)) & set(range(My, My+Mo+1))

if len(x) == 1 and len(y) == 1:
    print(1)
elif len(x) == 1 or len(y) == 1:
    print(2)
elif len(x) and len(y):
    print(3)
else:
    print(4)