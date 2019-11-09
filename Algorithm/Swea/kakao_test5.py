def solution(stones, k):
    answer = 0
    if k >= len(stones):
        return max(stones)
    minn, ans = float('inf'), stones[:k]
    i = k
    while i < len(stones):
        if max(ans) > k and minn > sum(ans):
            minn, answer = sum(ans), min(ans)
        ans.pop(0)
        ans.append(stones[i])
        i += 1
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1, 7]
k = 3
print(solution(stones, k))