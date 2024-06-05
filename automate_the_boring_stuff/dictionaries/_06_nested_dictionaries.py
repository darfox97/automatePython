allGuests = {'Alice': {'apples': 5, 'pretzels': 12, 'chips': 3},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)

    return numBrought


def obtainGuests(dictList):
    listGuests = []
    for guest in dictList:
        listGuests.append(guest)
    return listGuests


def obtainItems(dictList):
    listItems = []
    for valores in dictList.values():
        for ingrediente in valores:
            listItems.append(ingrediente)
    return listItems


def printResult(gathered_ingredients):
    print('Number of things being brought:')
    for item in gathered_ingredients:
        print(' - ' + item + ": " + str(totalBrought(allGuests, item)))


listGuests = obtainGuests(allGuests)
gatheredIngredients = obtainItems(allGuests)
# print(gatheredIngredients)
printResult(gatheredIngredients)

# Otra forma de acceder a los ingredientes:
for key, value in allGuests.items():
    for ingredientes in value:
        print("INGREDIENTE: " + ingredientes)
    # print("MOSTRAR: " + str(v))
