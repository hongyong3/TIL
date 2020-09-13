import sys
sys.stdin = open("D4_3000_input.txt", "r")

def minPush(n):
    minHeap.append(n)
    i =  len(minHeap)

    while i > 1:
        if minHeap[i // 2 - 1] > minHeap[i - 1]:
            minHeap[i // 2 - 1], minHeap[i - 1] = minHeap[i - 1], minHeap[i // 2 - 1]
        i //= 2

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
            child = right
        else:
            child = left

    if child == - 1:
        return

    if minHeap[child] < minHeap[parent]:
        minHeap[child], minHeap[parent] = minHeap[parent], minHeap[child]
        minPopSwap(child)

def minPop():
    if not len(minHeap):
        return

    minHeap[0] = minHeap.pop(- 1)
    minPopSwap(0)

def maxPush(n):
    maxHeap.append(n)
    i = len(maxHeap)

    while i > 1:
        if maxHeap[i // 2 - 1] < maxHeap[i - 1]:
            maxHeap[i // 2 - 1], maxHeap[i - 1] = maxHeap[i - 1], maxHeap[i // 2 - 1]
        i //= 2

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

def maxPop():
    if not len(maxHeap):
        return

    maxHeap[0] = maxHeap.pop(- 1)
    maxPopSwap(0)

T = int(input())
for test_case in range(T):
    N, A = map(int, input().split())
    minHeap, maxHeap = [], []
    mid = A
    mat = 0

    for _ in range(N):
        x, y = map(int, input().split())

        if mid < x and mid < y:
            minPush(x)
            minPush(y)
            maxPush(mid)
            mid = minHeap[0]
            minPop()

        elif mid > x and mid > y:
            maxPush(x)
            maxPush(y)
            minPush(mid)
            mid = maxHeap[0]
            maxPop()

        elif x <= mid <= y:
            maxPush(x)
            minPush(y)

        elif y <= mid <= x:
            minPush(x)
            maxPush(y)

        mat = (mat + mid) % 20171109
    print("#{} {}".format(test_case + 1, mat))