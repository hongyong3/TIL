import sys
sys.stdin = open("D6_5216_input.txt", "r")

def poly_times(p, q, m):
    result = set()
    for i in p:
        for j in q:
            if i + j > m:
                continue
            if i + j in result:
                result.remove(i + j)
            else:
                result.add(i + j)
    return result


def coeff(n, m):
    if m > 2 * n: return 0
    prod = [set([0]), set([0])]
    i = 0
    while n:
        if n % 2:
            prod[i // 20] = poly_times(prod[i // 20], [0, 2 ** i, 2 ** (i + 1)], m)
        i += 1
        n >>= 1
    s = 0
    for x in prod[0]:
        s += m - x in prod[1]
    return s % 2

# for m in range(10):
#     print(m, coeff(3, m))

print(coeff(2, 0))
print(coeff(4, 5))
