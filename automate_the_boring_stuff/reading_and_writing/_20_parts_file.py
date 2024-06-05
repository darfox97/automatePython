from pathlib import Path

p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.parent)  # This is a Path object, not a string.
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

# Current working directory:
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])


# Checking Path Validity
print(p.exists())
print(p.is_file())
print(p.is_dir())
