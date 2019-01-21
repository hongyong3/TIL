def selectionSort(a):
    for i in range(0, len(a)-1):            # 최솟값

        min =  i                            # 최솟값 찾는 과정
        for j in range(i+1, len(a)):        # 최솟값 찾는 과정
            if a[min] > a[j]:               # 최솟값 찾는 과정
                min = j                     # 최솟값 찾는 과정

        a[i], a[min] = a[min], a[i]         # swap

data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)