#!/usr/bin/python3
"""
save_to_json_file module.

Contains a function that writes an Object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON  Object to a text file."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
