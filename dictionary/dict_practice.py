"""
파이썬 dictionary 활용 기초!
"""

# dict = {
#     "대전" : 23,
#     "서울" : 30,
#     "구미" : 20
# }

# #dict.values()는 반복적으로 가져오라고 할 때
# #print(type(dict.values()))

# list = [1, 231, "123132"]
# #len은 리스트 안의 요소의 갯수를 알고자 할 때
# print(len(list))

#1. 평균을 구하세요.
scores = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}
#빈 변수가 한개 필요하다.

#방법1
total_score = 0
for score in scores.values():
    #0+87 ----- 87+92 ----- 87+92+40 이런 식으로 변수를 갱신해서 반복
    total_score = total_score + score
    #total_score += total_score
averge_score = total_score / len(scores)
print(averge_score)


#방법2
dict = score
x = sum(score.values())
print(x/3)