

scor = [40, 80, 75, 20, 96, 69, 50]
excellent = 0
failed = 0

for i in range(7):
    if scor[i] < 60:
        failed = failed + 1
    elif scor[i] > 90:
        excellent = excellent + 1

print("< 60 有", failed, "人")
print("> 90 有", excellent, "人")
