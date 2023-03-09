#!/usr/bin/python3
def uppercase(s):
    count = 1
    for c in range(len(s)):
        end = '\n' if count == len(s) else ''
        if ord('a') <= ord(s[c]) <= ord('z'):
            print("{}".format(chr(ord(s[c]) - 32)), end=end)
        else:
            print("{}".format(s[c]), end=end)
        count += 1
