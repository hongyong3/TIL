# import sys
# sys.stdin = open("Kakao_test_03_input.txt", "r")

def solution(A):
    # write your code in Python 3.6
    visited = [0] * len(A)
    count = 0
    for i in A:
        visited[i - 1] = 1

        if visited[:i] == [1] * i:
            count += 1
    return count

# A = [2, 1, 3, 5, 4]
# A = [5, 4, 3, 2, 1]
# A = [5, 4, 3, 1, 2]
# A = [3, 1, 2, 4, 5]
# A = [5, 1, 4, 2, 3]
