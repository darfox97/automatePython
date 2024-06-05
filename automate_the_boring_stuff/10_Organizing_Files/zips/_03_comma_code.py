spam = ['apples', 'bananas', 'tofu', 'cats']

if not spam:
    print("Lista vacía.")
else:
    for word in spam:
        if word == spam[-1]:
            print("and " + word, end=".")
        else:
            print(word, end=", ")
