def bruteForce(text, pattern, start):
    i, j = start, 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i = i -j
            j = -1
        i = i + 1
        j = j + 1

    if j == len(pattern):
        return i - len(pattern) # 검색 성공
    else:
        return -1 # 검색 실패

def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        count = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                if(count >= len(pattern)):
                    return i
        return -1

text = "This is a book. This is a computer"
pattern = "is"