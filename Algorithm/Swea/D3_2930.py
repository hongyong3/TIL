import sys
sys.stdin = open("D3_2930_input.txt", "r")

def heapPushSwap(size):
    if size == 1:
        return

    parent = size // 2

    if heapArr[parent - 1] < heapArr[size - 1]:
        heapArr[parent - 1], heapArr[size - 1] = heapArr[size - 1], heapArr[parent - 1]
        heapPushSwap(parent)


def heapPopSwap(parent):
    left, right = - 1, - 1

    if (len(heapArr)) - 1 >= parent * 2 + 1:
        left = parent * 2 + 1
    if (len(heapArr)) - 1 >= parent * 2 + 2:
        right = parent * 2 + 2

    if left == - 1 and right == - 1:
        child = - 1
    elif left != - 1 and right == - 1:
        child = left
    else:
        if heapArr[left] > heapArr[right]:
            child = left
        else:
            child = right

    if child == - 1:
        return

    if heapArr[child] > heapArr[parent]:
        heapArr[child], heapArr[parent] = heapArr[parent], heapArr[child]
        heapPopSwap(child)


def heapPush(n):
    heapArr.append(n)
    size = len(heapArr)
    heapPushSwap(size)


def heapPop():
    if not len(heapArr):
        return - 1
    elif len(heapArr) == 1:
        return heapArr.pop()
    answer = heapArr[0]
    heapArr[0] = heapArr.pop(- 1)
    heapPopSwap(0)
    return answer

T = int(input())
for test_case in range(T):
    N = int(input())
    heapArr = []
    ans = []
    for i in range(N):
        data = list(map(int, input().split()))
        if len(data) == 2:
            heapPush(data[1])
        else:
            ans.append(heapPop())
    print("#{}".format(test_case + 1), *ans)