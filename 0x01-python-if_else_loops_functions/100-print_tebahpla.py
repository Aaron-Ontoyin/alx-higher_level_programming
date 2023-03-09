#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        l = chr(i)
    else:
        l = chr(i-32)
    print("{}".format(l), end="")
