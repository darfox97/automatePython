from pathlib import Path

# to work on specific files, the glob() method is simpler to use than listdir().
p = Path('C:/Users/david.moragarces/vsworkspace/automate_the_boring_stuff/reading_and_writing')
print(p.glob('*'))
print(list(p.glob('*')))

print("Archivos de texto:")
print(list(p.glob('*.txt')))


# The glob expression 'project?.docx' will return 'project1.docx' or 'project5.docx',
# but it will not return 'project10.docx', because ? only matches to one character.
print(list(p.glob('project?.docx')))
