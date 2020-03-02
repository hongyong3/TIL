# print(list((lambda x: x ** 2, list(filter(lambda x: x % 3 and x % 5, range(1, 21))))))
print(list(filter(lambda x: x % 15, list(map(lambda x: x ** 2, range(1, 21))))))