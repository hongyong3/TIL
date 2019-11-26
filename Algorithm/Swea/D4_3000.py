import sys
sys.stdin = open("D4_3000_input.txt", "r")


def minPushSwap(size):
    if size == 1:
        return

    parent = size // 2

    if minHeap[parent - 1] < minHeap[size - 1]:
        minHeap[parent - 1], minHeap[size - 1] = minHeap[size - 1], minHeap[parent - 1]
        minPushSwap(parent)


def minPopSwap(parent):
    left, right = - 1, - 1

    if (len(minHeap)) - 1 >= parent * 2 + 1:
        left = parent * 2 + 1
    if (len(minHeap)) - 1 >= parent * 2 + 2:
        right = parent * 2 + 2

    if left == - 1 and right == - 1:
        child = - 1
    elif left != - 1 and right == - 1:
        child = left
    else:
        if minHeap[left] > minHeap[right]:
            child = left
        else:
            child = right

    if child == - 1:
        return

    if minHeap[child] > minHeap[parent]:
        minHeap[child], minHeap[parent] = minHeap[parent], minHeap[child]
        minPopSwap(child)


def minPush(n):
    minHeap.append(n)
    size = len(minHeap)
    minPushSwap(size)


def minPop():
    if not len(minHeap):
        return
    minHeap[0] = minHeap.pop(- 1)
    minPopSwap(0)

#######################################################################

def maxPushSwap(size):
    if size == 1:
        return

    parent = size // 2

    if maxHeap[parent - 1] < maxHeap[size - 1]:
        maxHeap[parent - 1], maxHeap[size - 1] = maxHeap[size - 1], maxHeap[parent - 1]
        maxPushSwap(parent)


def maxPopSwap(parent):
    left, right = - 1, - 1

    if (len(maxHeap)) - 1 >= parent * 2 + 1:
        left = parent * 2 + 1
    if (len(maxHeap)) - 1 >= parent * 2 + 2:
        right = parent * 2 + 2

    if left == - 1 and right == - 1:
        child = - 1
    elif left != - 1 and right == - 1:
        child = left
    else:
        if maxHeap[left] > maxHeap[right]:
            child = left
        else:
            child = right

    if child == - 1:
        return

    if maxHeap[child] > maxHeap[parent]:
        maxHeap[child], maxHeap[parent] = maxHeap[parent], maxHeap[child]
        maxPopSwap(child)


def maxPush(n):
    maxHeap.append(n)
    size = len(maxHeap)
    maxPushSwap(size)


def maxPop():
    if not len(maxHeap):
        return
    maxHeap[0] = maxHeap.pop(- 1)
    maxPopSwap(0)




T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    minHeap = []
    maxHeap = []
    mid = M
    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if mid <= x and mid <= y:
            minPush(- x)
            minPush(- y)
            maxPush(mid)
            mid = maxHeap[0]
        elif mid >= x and mid >= y:
            maxPush(x)
            maxPush(y)
            minPush(- mid)
            mid = maxHeap[0]
        else:
            if x < y:
                maxPush(x)
                minPush(- y)
            elif x > y:
                minPush(- x)
                maxPush(y)
        print("maxHeap :", maxHeap)
        print("minHeap :", minHeap)
        print("mid :", mid)
        # ans += mid