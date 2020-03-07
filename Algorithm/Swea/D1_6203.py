import sys
sys.stdin = open("D1_6203_input.txt", "r")

class Score:
    total = 0
    def __init__(self, subject):
        self.__subject = subject
        Score.total += subject

    def __del__(self):
        pass

data = list(map(int, input().split(', ')))
subjects = {}
a = 0
for i in data:
    subjects[a] = i
    a += 1
for subject in subjects.values():
    Score(subject)
print("국어, 영어, 수학의 총점: {}".format(Score.total))