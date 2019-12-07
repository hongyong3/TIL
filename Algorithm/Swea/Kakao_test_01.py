import itertools


def solution(A, B, C, D):
    # write your code in Python 3.6
    data, ans = [], []
    data = [str(A), str(B), str(C), str(D)]

    sub_ans = (list(map(''.join, itertools.permutations(data))))

    for i in sub_ans:
        if (0 <= int(i[:2]) < 24) and (0 <= int(i[2:]) < 60) and (i not in ans):
            ans.append(i)
    print(ans)
    print(len(ans))
    return len(ans)

A, B, C, D = 1, 2, 3, 4
solution(A, B, C, D)