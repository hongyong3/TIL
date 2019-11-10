def solution(user_id, banned_id):
    answer = 0
    ans = [0] * len(banned_id)
    ans1 = 1
    for i in range(len(banned_id)):
        for j in user_id:
            if len(banned_id[i]) == len(j):
                k = - 1
                while k < len(j):
                    k += 1
                    if banned_id[i][k] == "*" or banned_id[i][k] == j[k]:
                        if k == len(j) - 1:
                            ans[i] += 1
                            break
                        continue
                    else:
                        break
    for l in ans:
        ans1 *= l
    answer = ans1
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))