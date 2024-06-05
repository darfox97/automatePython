import os

# os.path.getsize(path) will return the size in bytes
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
# os.listdir(path) will return a list of filename strings for each file in the path argument.
# print(os.listdir('C:\\Windows\\System32'))

# If I want to find the total size of all the files in this directory, I can use os.path.getsize() and os.listdir() together.
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + \
        os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
