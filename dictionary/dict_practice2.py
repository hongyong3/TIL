#2 반 평균을 구하시오.
scores = {
    "철수" : {
        "수학" : 80,
        "국어" : 90,
        "음악" : 100
    },
    "영희" : {
        "수학" : 70,
        "국어" : 60,
        "음악" : 50
    }
}

#방법1) 내가 푼 방법
# total_score = 0
# for class_name in scores:
#     for score in scores[class_name].values():
#         total_score += score
#         average_score = total_score / len(scores[class_name])
# average_class = average_score / len(scores)
# print(average_class)

#방법2) 선생님께서 푸신 방법
# total_score = 0
# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# average_score = total_score / count
# print(average_score)

# for key, value in scores.items():
#     print(key)
#     print(value)


# 3 도시 중 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울" : [-6 -10, -5],
    "대전" : [-3 -5, -2],
    "광주" : [0 -2, 10],
    "부산" : [2 -2, 9]
}
#max min

for key, value in cities.items():
    print(key)
    print(value)

# for name in cities:
#     for temp in cities.values():
#         temp_min = min(list(cities.values())
#         # temp_max = max(list(cities.values())