import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\david.moragarces\\vsworkspace\\automate_the_boring_stuff\\10_Organizing_Files'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
