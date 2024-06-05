import pyperclip
# import requests

text = pyperclip.paste()
pyperclip.copy("Texto de prueba")
print(pyperclip.paste())

print(text)


# r = requests.get("https://www.google.com")
# print(r)
