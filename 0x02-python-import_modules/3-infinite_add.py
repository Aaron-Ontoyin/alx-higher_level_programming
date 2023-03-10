#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[1:]

    ans = 0
    for arg in argv:
        ans += int(arg)
    print(ans)
