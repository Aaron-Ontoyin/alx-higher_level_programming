#!/usr/bin/python3
def uppercase(s):
    for c in s:
        # convert lowercase letters to uppercase by subtracting 32 from their ASCII code
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()  # print a new line at the end
