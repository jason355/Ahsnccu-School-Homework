# 我是林珈生

def count(a, b):
    if a > b:
        while(a % b != 0):
            c = a % b
            a = b
            b = c
    else:
        temp = a
        a = b
        b = temp
        while(a % b != 0):
            c = a % b
            a = b
            b = c
    return c

print(count(12, 56))

                
