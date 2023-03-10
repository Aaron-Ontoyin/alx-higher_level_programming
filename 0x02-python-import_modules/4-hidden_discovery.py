#!/usr/bin/python3
if __name__ = '__main__':
    import hidden_4

    for f in dir(hidden_4):
        if f[:2] != '__':
            print(f)
