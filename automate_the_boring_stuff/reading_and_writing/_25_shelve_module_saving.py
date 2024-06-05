# The shelve module will let you add Save and Open features to your program.
# For example, if you ran a program and entered some configuration settings,
# you could save those settings to a shelf file.

import shelve
shelfFile = shelve.open('./mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('./mydata')
print(shelfFile['cats'])
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() methods that will return list-like values
shelfFile = shelve.open('./mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
