def swap(dataN, x, y):
    temp = dataN[x]
    dataN[x] = dataN[y]
    dataN[y] = temp

def compareChange(dataN, leni):
    for k in range(leni-1):
        for i in range(leni-1-k):
            if dataN[i] > dataN[i+1]:
                swap(dataN, i, i+1)
        print("第", k, "次:", num)

num = [5, 7, 6, 4, 1]

leni = len(num)

compareChange(num, leni)
print(num)


