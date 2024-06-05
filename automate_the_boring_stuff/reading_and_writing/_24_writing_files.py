# If the filename passed to open() does not exist, both write and append mode will create a new, blank file.

# W para sobrescribir
baconFile = open('reading_and_writing/bacon.txt', 'w', encoding="UTF-8")
baconFile.write('Hello, world!\n')
baconFile.close()

# a para añadir:
baconFile = open('reading_and_writing/bacon.txt', 'a', encoding="UTF-8")
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('reading_and_writing/bacon.txt', encoding="UTF-8")
content = baconFile.read()
baconFile.close()
