print(list(map(lambda x: pow(x, 2), (filter(lambda x: not x % 2, list(range(1, 11)))))))