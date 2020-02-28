def multiply(data):
    ans = 1
    for i in data:
        if type(i) == int:
            ans *= i
        else:
            return '에러발생'
    return ans
data = [1, 2, '4', 3]
print(multiply(data))