import webbrowser
import pyperclip

# 1. Gets a street address from the command line arguments or clipboard
# 2. Opens the web browser to the Google Maps page for the address

address = pyperclip.paste()
print(address)
webbrowser.open(f'https://www.google.es/maps/place/{address}')


# open_new abre una nueva ventana
# open_new_tab abre una nueva pestaña
