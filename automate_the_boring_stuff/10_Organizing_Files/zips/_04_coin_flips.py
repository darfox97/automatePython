import random

listaFlips = []
tails = 0
heads = 0
for i in range(10000):
    randNum = random.randint(0, 1)
    if randNum == 0:
        listaFlips.append("T")
        tails += 1
    elif randNum == 1:
        listaFlips.append("H")
        heads += 1

streak = 1
streaks_over_six = 0
lastFlip = ""
for i in listaFlips:
    if lastFlip == i:
        streak += 1
        if streak == 6:
            streaks_over_six += 1
    else:
        streak = 1
        lastFlip = i

# print(listaFlips)
print(f"Caras: {heads}; Cruces: {
      tails}. Rachas superiores a 6: {streaks_over_six}")
print("Probabilidad de racha: %s%%" % (streaks_over_six/100))
