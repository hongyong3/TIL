data = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
    }
ans = sorted(data.items(), key = lambda k: k[1], reverse = True)
for i in ans:
    print("{}: {}".format(i[0], i[1]))