# The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python

# shutil.copy(source, destination)
import shutil
import os
from pathlib import Path
p = Path.home()

shutil.copy(p / 'spam.txt', p / 'some_folder')

# This also copies the file at C:\Users\Al\eggs.txt
# to the folder C:\Users\Al\some_folder but gives the copied file the name eggs2.txt.
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')

# shutil.copytree() will copy an entire folder and every folder and file contained in it.
# spam_backup will have the same content as the original spam folder.
shutil.copytree(p / 'spam', p / 'spam_backup')

# shutil.move(source, destination) will move the file
#  if there is no eggs folder, then move() will rename bacon.txt to a file named eggs.
shutil.move('C:\\bacon.txt', 'C:\\eggs')
# The destination path can also specify a filename. In the following example, the source file is moved and renamed.
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')


# Permanently Deleting Files and Folders
# - Calling os.unlink(path) will delete the file at path.
# - Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# - Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
for filename in Path.home().glob('*.rxt'):
    # os.unlink(filename) # Esto borra todos los archivos .rxt
    print(filename)
