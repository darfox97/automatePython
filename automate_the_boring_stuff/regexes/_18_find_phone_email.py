import re
import pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                    # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [\w.%+-]+
    (@[\w.]+)
    (\.\w{2,4})                                              
)''', re.VERBOSE)

text = pyperclip.paste()

phones_list = phone_regex.findall(text)
emails_list = email_regex.findall(text)

phones_and_emails = []
for groups in phones_list:
    if not str(groups[1]).endswith(")"):
        phoneNum = '-'.join(["("+groups[1]+")", groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    phones_and_emails.append(phoneNum)

for groups in emails_list:
    phones_and_emails.append(groups[0])

if len(phones_and_emails) > 0:
    pyperclip.copy('\n'.join(phones_and_emails))
    print('Copied to clipboard:')
    print('\n'.join(phones_and_emails))
else:
    print('No phone numbers or email addresses found.')

print(phones_and_emails)
