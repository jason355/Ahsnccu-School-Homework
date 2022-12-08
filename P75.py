# 我是林珈生

def change(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

numVis = [70,10,14,7,25,30,50]
print(numVis)
change(numVis, 0, 6)
print(numVis)

