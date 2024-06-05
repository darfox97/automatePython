tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table_name, biggest_column):
    maxRows = len(table_name)

    for columna in range(4):
        for fila in range(maxRows):
            elemento = str(table_name[fila][columna])
            print(elemento.rjust(biggest_column), end="")
        print()


def calculateLongestString(table_name):
    biggest_column = 0
    for fila in table_name:
        for columna in fila:
            if biggest_column < len(columna):
                biggest_column = len(columna)
            # elemento = str(columna)
    return biggest_column


biggestColumn = calculateLongestString(tableData)
printTable(tableData, biggestColumn)
