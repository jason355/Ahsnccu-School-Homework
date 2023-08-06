
sco = [[100, 20, 85], [95, 99, 75], [89, 73, 92]]
stu = ['嘉明', '小美', '阿雄']
total = 0

for i in range(3):
    print(stu[i], "總分為: ", end=" ")
    for j in range(3):
        total = total + sco[i][j]
    print(total, "分", end="\n")
