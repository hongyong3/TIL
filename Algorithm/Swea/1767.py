import sys
sys.stdin = open("1767_input.txt", "r")
from collections import deque



def find_core(st,y,x) :
    if st == "up" :
        for dn in range(y) :
            if data[dn][x] == 1 : return True
    elif st== 'dw' :
        for dn in range(y+1,N) :
            if data[dn][x] == 1 : return True
    elif st== 'lf' :
        for dm in range(x) :
            if data[y][dm] == 1 : return True
    else :
        for dm in range(x+1,N) :
            if data[y][dm] == 1 : return True
    return False

def find_restrict(sy,y,x,cy,cx) :
    if st == 'up':
        if cy < y and cx < x : return (cy,cx,"rg")
        elif cy < y and cx > x : return (cy,cx,'lf')
    elif st == 'dw':
        if cy > y and cx < x: return (cy, cx, "rg")
        elif cy > y and cx > x: return (cy, cx, 'lf')
    elif st == 'lf':
        if cx < x and cy < y : return (cy,cx,"dw")
        elif cx < x and cy>y : return (cy,cx,"up")
    else:
        if cx > x and cy < y : return (cy,cx,"dw")
        elif cx > x and cy > y : return (cy,cx,"up")
    return None


T = int(input())
for t in range(T) :
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    cores = deque((i,j) for i in range(N) for j in range(N) if data[i][j]==1)

    graph = dict()
    for y,x in cores :

        if y==0 or x==0 or x==N-1 or y==N-1 :
            graph[(y,x)] = [("nr",0,[])]
            continue
        else : # 가지 않거나 가거나
            graph[(y,x)] = [("ng",0,[])]
            for st in "up", "dw", 'lf', 'rg' :
                if find_core(st, y, x) : continue
                temps = list()
                for cy,cx in cores :
                    if cy!=y and cx!=x :
                        if find_restrict(st, y, x, cy, cx) : temps.append(find_restrict(st, y, x, cy, cx))
                if st =="up" :
                    graph[(y,x)].append( ("up",y,temps))
                elif st =="dw" : graph[(y, x)].append(("dw", N - y - 1, temps))
                elif st == 'lf' : graph[(y,x)].append( ("lf",x,temps) )
                else :  graph[(y,x)].append( ("rg",N-x-1,temps))


    paths = deque()
    y,x = cores[0]
    for status, price, restrict in graph[(y,x)] :
        paths.append( [(y,x,status,price)] )

    result = list()
    while paths :
        path = paths.popleft()
        only_path = [(y,x,status) for y,x,status,price in path]
        y,x,status,price = path[-1]

        try :
            ny,nx = cores[cores.index((y,x))+1] # 다음 갈 곳 _ path에 추가할 것
            for nstatus, nprice, nrestricts in graph[(ny,nx)] :
                temp = 1
                for ry,rx,rs in nrestricts :
                    if (ry,rx,rs) in only_path : temp=0 ; break
                if temp :
                    paths.append(path+[(ny,nx,nstatus,nprice)])
        except : result.append(path)

    for i in range(len(result)) :
        result[i] = [pair[3] for pair in result[i] if pair[2]!='ng']
    result.sort(key=lambda x:(-len(x),sum(x)))

    print("#{} {}".format(t+1,sum(result[0])))