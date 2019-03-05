import sys
sys.stdin = open("이진 힙_input.txt", "r")

def enQ(n):
    global last
    last += 1   # 마지막 노드번호 증가
    child = last    # 마지막 노드를 자식노드로
    parent = child//2    # 부모 노드 번호 계산
    Q[last] = n # 마지막 노드에 값 저장
    while child > 1 and Q[parent] > Q[child]:    # 루트가 아니고, 부모 노드의 값이 더 크면
        t = Q[parent]    # 저장된 값 바꿈
        Q[parent] = Q[child]
        Q[child] = t
        child = parent   # 부모를 새로운 자식노드로
        parent = parent//2

def deQ():
    global last
    r = Q[1]    # 리턴값(루트노드)
    Q[1] = Q[last]  # 마지막을 루트노드로 이동
    last -= 1   # 카운터 감소
    parent = 1
    while parent < last:
        child1 = parent * 2  # 왼쪽자식
        child2 = parent * 2 + 1  # 오른쪽자식
        if child2 <= last:  # 양쪽자식이 다 있는 경우
            if Q[child1] < Q[child2]:
                child = child1
            else:
                child = child2
            if Q[child] < Q[parent]:
                Q[child], Q[parent] = Q[parent], Q[child]
                parent = child
            else:
                break
        elif child1 <= last:    # 왼쪽자식만 있는 경우
            if Q[child1] < Q[parent]:
                Q[child1], Q[parent] = Q[parent], Q[child1]
                parent = child1
            else:
                break
    return r

T = int(input())
for test_case in range(1):
    N = int(input())
    V = list(map(int, input().split()))
    Q = [0] * (N+1)
    last = 1
    enQ(N)
    # print("#{} {}".format(test_case + 1, enQ(N)))