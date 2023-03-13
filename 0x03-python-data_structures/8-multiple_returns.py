#!/usr/bin/python3

def multiple_returns(sentence):
    l = len(sentence)
    first_char = sentence[0] if len(sentence) > 0 else None
    return (l, first_char)
