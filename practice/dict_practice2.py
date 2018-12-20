#2 반 평균을 구하시오.
# scores = {
#     "철수" : {
#         "수학" : 80,
#         "국어" : 90,
#         "음악" : 100
#     },
#     "영희" : {
#         "수학" : 70,
#         "국어" : 60,
#         "음악" : 50
#     }
# }
# #방법1) 내가 푼 방법
# total_score = 0
# for class_name in scores:
#     for score in scores[class_name].values():
#         total_score += score
#         average_score = total_score / len(scores[class_name])
# average_class = average_score / len(scores)
# print(average_class)

# #방법2) 선생님께서 푸신 방법
# total_score = 0
# for person_score in socres.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# average_score = total_score / count
# print(average_score)

# for key, value in scores.items():
#     print(key)
#     print(value)


#3. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울" : [-6, -10, 5],
    "대전" : [-3, -5, 2],
    "광주" : [0, -2, 10],
    "부산" : [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold 보다 더 추우면, cold 에 넣고
        if min(temp) < cold:
            cold =min(temp)
            cold_city = name
        # 최고 온도가 hot 보다 더 더우면, hot 에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")