from pathlib import Path

file = Path('./reading_and_writing/helloworld.txt')
# file.write_text('New Line', encoding="UTF-8")

helloFile = open(file, encoding="UTF-8")
print(helloFile.readlines())

# Al intentar volver a leer no mostrará nada, ya que el archivo ya ha sido recorrido:
# print(helloFile.read())
helloFile.close()
