import collections

def solution(A):
    # write your code in Python 3.6
    sub_answer = collections.Counter(A)
    count = 0
    for key, value in sub_answer.items():
        if (key == value) and (count < key):
            count = key
    return count
