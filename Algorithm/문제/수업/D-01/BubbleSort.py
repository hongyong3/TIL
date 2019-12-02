def bubblesort(data):
    for i in range(len(data)-1, 0, -1):     # 1 2 3 4
        for j in range(0, i):               # 1 2 3 4
            if data[j] > data[j+1]:         # 오름차순
                data[j], data[j+1] = data[j+1], data[j]

data = [55, 7, 78, 12, 42]
bubblesort(data)
print(data)

def bubblesort(data):
    for i in range(len(data)-1, 0, -1):     # 4 3 2 1
        for j in range(0, i):               # 4 3 2 1
            if data[j] < data[j+1]:         # 내림차순
                data[j], data[j+1] = data[j+1], data[j]

data = [55, 7, 78, 12, 42]
bubblesort(data)
print(data)