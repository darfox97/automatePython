# Using pprint.pformat() will give you a string that you can write to a .py file.
# This file will be your very own module that you can import whenever you want to use the variable stored in it.
import myCats
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
print(pprint.pformat(cats))
fileObj = open('./reading_and_writing/myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# And since Python scripts are themselves just text files with the .py file extension,
# your Python programs can even generate other Python programs.
# import myCats:
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])
