

data = [12, 2, 7, 5, 9]
leni = len(data)
targ = 7


def serCho(leni, data, targ):
    for i in range(leni):
        if data[i] == targ:
            return i
    return 0


result = serCho(leni, data, targ)

if result == 0:
    print(f"There is no {targ} in data.")
else:
    print("Your target's index:", result)
