from collections import OrderedDict

def duplicate(input_string):
    print(*OrderedDict.fromkeys(input_string))
    return None

input_string = input()
duplicate(input_string)