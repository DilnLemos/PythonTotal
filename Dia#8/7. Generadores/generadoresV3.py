def suma_generadora():
    x = 1
    yield x

    x += 1
    yield x

    x += 2
    yield x

    x += 3
    yield x


y = suma_generadora()
print(next(y))
print(next(y))
print(next(y))
print(next(y))

"""
1
2
4
7
"""