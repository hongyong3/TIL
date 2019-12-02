import sys
sys.stdin = open("최소 신장 트리_input.txt", "r")

def Find_Set(x):
    if x == P[x]: return x
    else: return Find_Set(P[x])


def MST():
    global V
    c = 0   # 간선갯수
    s = 0   # 가중치의 합
    i = 0   # 제어변수
    while c < V:    # MST 구성을 위해 V개의 간선을 선택
        p1 = Find_Set(data[i][0])   # 두 노드의 대표원소 알아내기
        p2 = Find_Set(data[i][1])
        if p1 != p2:                # 사이클이 생성되지 않으면
            s += data[i][2]         # MST에 포함되므로 가중치 증가
            c += 1                  # 간선 개수 증가
            P[p2] = p1              # 대표 원소 관리(union)
        i += 1                      # 저장된 다음 간선으로 이동
    return s                        # MST 완성 후 가중치 합 반환

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]  # 시작, 끝, 가중치
    data.sort(key=lambda x: x[2])   # 간선을 가중치 기준으로
    P = list(range(V+1))            # 대표원소 초기화(make set)
    print("#{} {}".format(test_case+1, MST()))
