data = [88, 30, 61, 55, 95]
for i in range(5):
    if data[i] >= 60:
        print("{}번 학생은 {}점으로 {}입니다.".format(i + 1, data[i], "합격"))
    else:
        print("{}번 학생은 {}점으로 {}입니다.".format(i + 1, data[i], "불합격"))