# Compressing Files with the zipfile Module

import zipfile
import os
from pathlib import Path
p = Path("C:\\Users\\david.moragarces\\vsworkspace\\automate_the_boring_stuff\\10_Organizing_Files")

# Reading ZIP Files
exampleZip = zipfile.ZipFile(p / 'prueba.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('_04_coin_flips.py')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print(f'Compressed file is {
      round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')

exampleZip.close()

# Extracting from ZIP Files
exampleZip = zipfile.ZipFile(p / 'prueba.zip')
exampleZip.extractall(p / 'zips')
exampleZip.close()

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile(p / 'new.zip', 'w')
newZip.write('_30_send2trash.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
