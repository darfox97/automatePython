#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# nuevoTexto = "* "
# for char in text:
#     if char == "\n":
#         nuevoTexto += "\n* "
#     else:
#         nuevoTexto += char

# for i in range(len(lines)):    # loop through all indexes in the "lines" list
#     lines[i] = '* ' + lines[i] # add star to each string in "lines" list
# text = '\n'.join(lines)

listsOfText = text.split("\n")
nuevo_texto = ""
for elemento in listsOfText:
    nuevo_texto += "\n* " + elemento

# print(nuevo_texto)
pyperclip.copy(nuevo_texto)
