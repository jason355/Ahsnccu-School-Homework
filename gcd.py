

def count(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


print(count(56, 91))
