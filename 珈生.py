import random

def 珈生(times, times2):
    print(sbj[times2])
    for i in range(times):
        print(" 珈生", end='\n')
        print("")
        
sbj = ['生物','國文', '資訊', '化學', '英文']

for i in range(6):
    珈生(random.randrange(13), random.randrange(0, 4))
    