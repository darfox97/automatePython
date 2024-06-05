#! python
# mcb.py - A multi-clipboard program with shelves.
import sys
import shelve
import pyperclip


def create_new_entry():
    if len(sys.argv) < 3:
        print("You must enter the name to be created")
        sys.exit()
    else:
        shelfFile[sys.argv[2]] = pyperclip.paste()


def show_all_entries():
    for key, value in shelfFile.items():
        print(f"· {key}: \n - {value}")


def search_entry(entry):
    if entry in shelfFile.keys():
        pyperclip.copy(shelfFile[entry])
        print('Text for ' + entry + ' copied to clipboard.')
    else:
        print('There is no text for ' + entry)


if len(sys.argv) < 2 or len(sys.argv) > 4:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]    # first command line arg is the keyphrase
shelfFile = shelve.open('./mcb')

if keyphrase == 'save':
    create_new_entry()
elif keyphrase == 'list':
    show_all_entries()
else:
    search_entry(keyphrase)

shelfFile.close()
