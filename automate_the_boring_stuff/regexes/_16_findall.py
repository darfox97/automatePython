# The findall() method will return the strings of every match in the searched string

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
numbers_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f"Lista de números:  {numbers_list}")

# If there are groups in the regular expression, then findall() will return a list of tuples:
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
numbers_list_groups = phoneNumRegex.findall(
    'Cell: 415-555-9999 Work: 212-555-0000')
print(f"Lista de tuplas con los números divididos en grupos: {
      numbers_list_groups}")
