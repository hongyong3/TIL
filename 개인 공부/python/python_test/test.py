def my_round(float):
    int_float = int(float)
    return int_float + int((float -int_float)*2)
print(my_round(3.2))
print(my_round(3.6))