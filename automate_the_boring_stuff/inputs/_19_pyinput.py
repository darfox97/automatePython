import pyinputplus as pyin

response = pyin.inputNum(prompt='Enter a number: ')
response = pyin.inputYesNo(prompt='Enter Yes or No: ')


# max, min, graterThan and lessThan:
response = pyin.inputNum('Enter num: ', min=4)
response = pyin.inputNum('Enter num: ', greaterThan=4)

# Blank keyword argument
# By default, blank input isn’t allowed
# Use blank=True if you’d like to make input optional so that the user doesn’t need to enter anything.
response = pyin.inputNum('Introduzca un número: ', blank=True)

# The limit, timeout, and default Keyword Arguments
response = pyin.inputNum(timeout=10)
# When you use these keyword arguments and also pass a default keyword argument,
# the function returns the default value instead of raising an exception.
response = pyin.inputNum(limit=2, default='N/A')

# The allowRegexes and blockRegexes Keyword Arguments
# inputNum() will accept Roman numerals in addition to the usual numbers
response = pyin.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# No permitirá introducir números acabados en 0,2,4,6 u 8:
response = pyin.inputNum(blockRegexes=[r'[02468]$'])
# The allow list overrides the block list.
response = pyin.inputStr(allowRegexes=[r'caterpillar', 'category'],
                         blockRegexes=[r'cat'])
