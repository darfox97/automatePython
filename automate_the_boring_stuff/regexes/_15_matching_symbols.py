import re

# ? Symbol after parenthesis ():
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo2 = phoneRegex.search('My number is 555-4242')
print(mo1.group())
print(mo2.group())

# Zero or more with star *:
batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batman')
mo4 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
print(mo4.group())

# One or more with plus +:
batRegex = re.compile(r'Bat(wo)+man')
mo5 = batRegex.search('The Adventures of Batwowowowoman')
mo6 = batRegex.search('The Adventures of Batman')
print(mo6 == None)

# Specific repetitions with braces {}:
haRegex = re.compile(r'(Ha){3}')
mo7 = haRegex.search('HaHaHa')
print(mo7.group())
mo8 = haRegex.search('Ha')
print(mo8 == None)
# You also can set a minimum and maximum:
haRegex = re.compile(r'(Ha){2,5}')  # btw.2 & 5


# - GREEDY AND NON-GREEDY MATCHING:
# Python's regexes are greedy by default, which means they will match the longest string possible.
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo9 = greedyHaRegex.search('HaHaHaHaHa')
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  # Optional mark ?
mo10 = nongreedyHaRegex.search('HaHaHaHaHa')
print("Greedy: " + mo9.group())
print("Non-Greedy: " + mo10.group())


# - CHARACTER CLASSES: \s \w \d

# The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+),
# followed by a whitespace character (\s),
# followed by one or more letter/digit/underscore characters (\w+).
xmasRegex = re.compile(r'\d+\s\w+')
listOfXmasRegex = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(listOfXmasRegex)

# YOUR OWN CHARACTER CLASSES:
# It will match any vowel, both lowercase and uppercase:
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelsList = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowelsList)

# NEGATIVE CHARACTER ^
# We’re matching every character that isn’t a vowel
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

# CARET AND DOLLAR SIGN:
# The r'^Hello' regular expression string matches strings that begin with 'Hello'
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
beginsWithHello.search('He said hello.') == None

# The r'\d$' regular expression string matches strings that end with a numeric character.
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None

# The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12  34567890') == None

# THE WILDCARD CHARACTER .
# The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.
# To match an actual dot, escape the dot with a backslash: \..
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# Matching Everything with Dot-Star .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
