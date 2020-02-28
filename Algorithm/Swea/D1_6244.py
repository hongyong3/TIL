score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# i = 0
# while i < len(score):
#     if score[i] < 80:
#         score.pop(i)
#     else:
#         i += 1
print(sum(i for i in score if i >= 80))