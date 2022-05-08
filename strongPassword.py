#! python3
# determine if password in clipboard has at least one uppercase letter/digit/lowercase letter/is 8 characters long
def strongPassword(password):
    import re
    if len(password) < 8:
        print('too short password')
        exit()
    digit = re.compile(r'[0-9]')
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    if not digit.search(password):
        print('password must contain at least one digit')
        exit()
    if not upper.search(password):
        print('password must contain at least one uppercase letter')
        exit()
    if not lower.search(password):
        print('password must contain at least one lowecase letter')
        exit()

import pyperclip as pc
password = pc.paste()

strongPassword(password)