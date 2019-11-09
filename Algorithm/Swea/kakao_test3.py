def solution(user_id, banned_id):
    answer = 0
    for i in banned_id:
        if len(i)

    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
solution(user_id, banned_id)