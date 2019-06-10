n = int(input())
for i in range(n):
    print(" " * (n-1-i) + "*" * (i+1))
print()
for i in range(n):
    print("*" * (n-i))