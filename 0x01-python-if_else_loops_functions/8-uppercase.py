#!/usr/bin/python3
def uppercase(s):
    count = 1
    for c in s:
        end = '\n' if count == len(s) else ''
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end=end)
        else:
            print(c, end=end)
        count += 1
