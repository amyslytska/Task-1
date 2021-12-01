def sum(*args):
    total = 0
    for arg in args:
        total+= arg

    return total

a = sum(1200, 300, 500)
print(a)
