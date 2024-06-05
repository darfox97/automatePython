# Safe Deletes with the send2trash Module
# Since Python’s built-in shutil.rmtree() function irreversibly deletes files and folders, it can be dangerous to use.
# send2trash is much safer than Python’s regular delete functions,
# because it will send folders and files to your computer’s trash or recycle bin.

import send2trash
baconFile = open('bacon.txt', 'a', encoding="UTF-8")   # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
