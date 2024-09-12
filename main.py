import pyperclip, re

# Philippine Mobile Phone
mobileRegex = re.compile(r'''
    ^                   # Start of string
    (?:\+63|0)          # Country code (+63) or leading zero (0)
    \d{10}              # Exactly 10 digits for the mobile number
    $                   # End of string
    ''', re.VERBOSE)

# Phillippine Landline
phoneRegex = re.compile(r'''
    ^                   # Start of string
    (?:\+63|0)?         # Optional country code (+63) or leading zero (0)
    \d{1,3}             # 1-3 digits for the area code
    \d{7}               # 7 digits for the landline number
    $                   # End of atring
    ''', re.VERBOSE)

# Email Address
emailRegex = re.compile(r'''
    ^                   # Start of string
    [a-zA-Z0-9.%+-]+    # Username: Letters, digits, underscores, dots, plus, hyphens
    @                   # '@' symbol
    [a-zA-Z0-9.-]+      # Domain name
    \.[a-zA-Z]{2,}      # Dot and top-level domains (at least two letters
    $                   # End of string
    ''', re.VERBOSE)