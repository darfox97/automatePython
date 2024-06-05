# All the regex functions in Python are in the re module.
# Passing a string value representing your regular expression to re.compile()
# returns a Regex pattern object (or simply, a Regex object).
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(type(phoneNumRegex))  # type 're.Pattern'

# The search() method will return None if the regex pattern is not found in the string.
# If the pattern is found, the search() method returns a Match object,
# which have a group() method that will return the actual matched text from the searched string.
# The mo variable name is just a generic name to use for Match objects
mo = phoneNumRegex.search('My number is 415-555-4442.')
if not mo:
    print("No Phone number found")
else:
    print('Phone number found: ' + mo.group())
# print('Phone number found: ' + mo.group())


# Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
# If both of them appears, it takes de first one:
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

# Solo muestra la primera coincidencia:
mo3 = batRegex.search('Batmobile lost a wheel, batbat')

print("mo3.group(): " + mo3.group())
print("mo3.group(): " + mo3.group(1))
