import sys
sys.stdin = open("practice_input.txt", "r")

def solution(numbers):
    answer = ''
    number = []
    numbers = list(map(str, numbers))
    for i in numbers:
        if len(i) == 4:
            number.append([i, i * 3])
        if len(i) == 3:
            number.append([i, i * 4])
        if len(i) == 2:
            number.append([i, i * 6])
        if len(i) == 1:
            number.append([i, i * 12])
    number.sort(key = lambda x:x[1], reverse = True)
    for i in number:
        answer += i[0]
    print(answer)
    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    number = []
    for i in numbers:
        number.append((i * 12, i))
    number = sorted(number, reverse = True)
    for i in number:
        answer += i[1]
    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    number = []
    for i in numbers:
        number.append((i * 12, i))
    numbers.sort(key =  lambda x : x * 12, reverse = True)
    for i in numbers:
        answer += i
    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ""
    numbers.sort(key =  lambda x : x * 12, reverse = True)
    for i in numbers:
        answer += i
    return answer




numbers1 = [6, 10, 2]
print(solution(numbers1))
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))
numbers3 = [12, 121]
print(solution(numbers3))
numbers4 = [21, 212]
print(solution(numbers4))
