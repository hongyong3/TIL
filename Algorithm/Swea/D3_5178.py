import sys
sys.stdin = open("D3_5178_input.txt", "r")

# 이전 풀이
# def postOrder(node):    # 후위 순회
#     global N
#     if node > N:        # 유효난 노드가 아니면 0 반환
#         return 0
#     else:
#         if data[node] != 0: # 리프토느인 경우 저장된 값 리턴
#             return data[node]
#         else:
#             a = postOrder(2 * node) # 왼쪽 자식으로 이동
#             b = postOrder(2 * node + 1) # 오른쪽 자식으로 이동
#             data[node] = a + b  # 양쪽의 값을 더해서 저장
#         return data[node]   # 노드에 저장된 값을 반환
#
# T = int(input())
# for test_case in range(T):
#     N, M, L = map(int, input().split()) # 노드의 수, 리프노드의 수, 값을 출력할 노드번호
#     data = [0 for i in range(N + 1)]    # 트리 생성
#
#     for i in range(M):
#         V, E = map(int, input().split())    # 리프노드 값을 입력받아 저장
#         data[V] = E
#     postOrder(1)
#     print("#{} {}".format(test_case+1, data[L]))

T = int(input())
for test_case in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    for i in range(N, 1, - 1):
        tree[i // 2] += tree[i]
    print("#{} {}".format(test_case + 1, tree[L]))