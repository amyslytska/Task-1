def sum(list):
    total = 0
    for n in list:
        total += n
    return total


payments = [1200, 1300, 2000]
a = sum(payments)
print(a)
