def solve(n):
    if n in data:
        print("{} => {}".format(n, True))
    else:
        print("{} => {}".format(n, False))

data = [2, 4, 6, 8, 10]
print(data)
solve(5)
solve(10)