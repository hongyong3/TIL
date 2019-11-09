def solution(s):
    answer = []
    data = ""
    for i in range(len(s)):
        if s[i] == '{':
            data += '['
        elif s[i] == '}':
            data += ']'
        else:
            data += s[i]
    number = eval(data)
    number.sort(key = lambda x: len(x))
    for i in number:
        for j in i:
            if int(j) not in answer:
                answer.append(j)
                break
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))